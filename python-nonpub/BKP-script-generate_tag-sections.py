#!/usr/bin/env python3
from __future__ import annotations

import itertools
import re
import shutil
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("Manca PyYAML. Installa con: python -m pip install pyyaml")

CLEAN_REFERENCE_TOPICS = True
CLEAN_TTP = True
REBUILD_TAG_INDEX = True
REBUILD_INDEX = True

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CONTENT_DIR = PROJECT_ROOT / "content"
SEMINARI_DIR = CONTENT_DIR / "Lista-Seminari"
REFERENCE_TOPICS_DIR = CONTENT_DIR / "Topics"
TTP_DIR = PROJECT_ROOT / "TTP-nonpub"

TAG_INDEX_SOURCE_FILE = PROJECT_ROOT / "tag-index-source-nonpub.md"
TAG_INDEX_FILE = CONTENT_DIR / "tag-index.html"
INDEX_FILE = CONTENT_DIR / "index.md"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)

TAG_LINE_RE = re.compile(r"^- (#[A-Za-z0-9/_-]+)\s*$")
PROPERTY_LINE_RE = re.compile(
    r"^\s{2,}- \*\*([A-Za-z][A-Za-z0-9 _-]*)\*\*:\s*(.+?)\s*$"
)
SECTION_LINE_RE = re.compile(r"^# (.+)$")

LEGACY_BLOCK_STARTS = {
    "<!-- AUTO TAXONOMY TAGS START -->",
    "<!-- AUTO TAG FAMILIES START -->",
}
LEGACY_BLOCK_ENDS = {
    "<!-- AUTO TAXONOMY TAGS END -->",
    "<!-- AUTO TAG FAMILIES END -->",
}


class TagIndexSyntaxError(Exception):
    pass


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def cleanup_folder(folder: Path) -> None:
    ensure_dir(folder)
    for child in folder.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        elif child.is_file():
            child.unlink()


def cleanup_file(path: Path) -> None:
    if path.exists():
        path.unlink()


def parse_frontmatter(md_text: str) -> tuple[dict, str]:
    match = FRONTMATTER_RE.match(md_text)
    if not match:
        return {}, md_text
    raw_yaml = match.group(1)
    body = md_text[match.end():]
    data = yaml.safe_load(raw_yaml) or {}
    if not isinstance(data, dict):
        data = {}
    return data, body


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"[^a-z0-9\-_àèéìòù/]", "-", value)
    value = value.replace("/", "-")
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def normalize_tag_list(raw_tags) -> list[str]:
    if isinstance(raw_tags, str):
        raw_tags = [raw_tags]
    if not isinstance(raw_tags, list):
        raw_tags = []

    normalized = []
    for tag in raw_tags:
        tag_s = str(tag).strip().lstrip("#")
        if tag_s:
            normalized.append(tag_s)

    return sorted(set(normalized), key=lambda x: x.casefold())


def wiki_link(relative_path: str, title: str) -> str:
    return f"[[{relative_path}|{title}]]"


def parse_scalar(value_text: str, line_no: int, source_path: Path) -> str:
    try:
        parsed = yaml.safe_load(value_text)
    except Exception as e:
        raise TagIndexSyntaxError(
            f"Errore in {source_path}, riga {line_no}: valore non valido -> {value_text!r} ({e})"
        )
    if parsed is None:
        return ""
    return str(parsed)


def canonical_prop_name(raw_name: str) -> str:
    name = raw_name.strip().lower()
    name = re.sub(r"\s+", "_", name)
    return name


def normalize_hash_tag(value: str, line_no: int, source_path: Path) -> str:
    value = value.strip()
    if not value.startswith("#ob/"):
        raise TagIndexSyntaxError(
            f"Errore in {source_path}, riga {line_no}: TopicTag deve iniziare con '#ob/'"
        )
    return value.lstrip("#").strip()


def finalize_tag_block(
    tag_defs: dict[str, dict[str, str]],
    entries: list[dict],
    current_tag: str | None,
    current_props: dict[str, str],
    current_tag_line: int | None,
    current_section: str | None,
    source_path: Path,
) -> None:
    if current_tag is None:
        return

    missing = [field for field in ("title", "description", "topictag") if not current_props.get(field)]
    if missing:
        missing_str = ", ".join(missing)
        raise TagIndexSyntaxError(
            f"Errore in {source_path}, riga {current_tag_line}: "
            f"il tag #{current_tag} non ha i campi obbligatori: {missing_str}"
        )

    if current_tag in tag_defs:
        raise TagIndexSyntaxError(
            f"Errore in {source_path}, riga {current_tag_line}: tag duplicato #{current_tag}"
        )

    data = dict(current_props)
    tag_defs[current_tag] = data
    entries.append(
        {
            "tag": current_tag,
            "title": data["title"],
            "description": data["description"],
            "topictag": data["topictag"],
            "section": current_section or "",
        }
    )


def parse_tag_index_source(path: Path) -> tuple[dict[str, dict[str, str]], list[dict]]:
    if not path.exists():
        raise FileNotFoundError(f"File non trovato: {path}")

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    tag_defs: dict[str, dict[str, str]] = {}
    entries: list[dict] = []

    current_tag: str | None = None
    current_props: dict[str, str] = {}
    current_tag_line: int | None = None
    current_section: str | None = None
    inside_legacy_block = False

    for idx, raw_line in enumerate(lines, start=1):
        line = raw_line.rstrip("\n")

        if "\t" in line:
            raise TagIndexSyntaxError(
                f"Errore in {path}, riga {idx}: i TAB non sono ammessi. Usa solo spazi."
            )

        stripped = line.strip()

        if stripped in LEGACY_BLOCK_STARTS:
            finalize_tag_block(tag_defs, entries, current_tag, current_props, current_tag_line, current_section, path)
            current_tag = None
            current_props = {}
            current_tag_line = None
            inside_legacy_block = True
            continue

        if stripped in LEGACY_BLOCK_ENDS:
            inside_legacy_block = False
            continue

        if inside_legacy_block:
            continue

        if stripped == "":
            finalize_tag_block(tag_defs, entries, current_tag, current_props, current_tag_line, current_section, path)
            current_tag = None
            current_props = {}
            current_tag_line = None
            continue

        section_match = SECTION_LINE_RE.match(stripped)
        if section_match:
            finalize_tag_block(tag_defs, entries, current_tag, current_props, current_tag_line, current_section, path)
            current_tag = None
            current_props = {}
            current_tag_line = None
            current_section = section_match.group(1).strip()
            continue

        tag_match = TAG_LINE_RE.match(line)
        if tag_match:
            finalize_tag_block(tag_defs, entries, current_tag, current_props, current_tag_line, current_section, path)

            raw_tag = tag_match.group(1)
            normalized_tag = raw_tag.lstrip("#").strip()

            current_tag = normalized_tag
            current_props = {}
            current_tag_line = idx
            continue

        prop_match = PROPERTY_LINE_RE.match(line)
        if prop_match:
            if current_tag is None:
                raise TagIndexSyntaxError(
                    f"Errore in {path}, riga {idx}: proprietà trovata fuori da un blocco tag."
                )

            raw_key = prop_match.group(1).strip()
            key = canonical_prop_name(raw_key)
            value_text = prop_match.group(2).strip()

            if key == "topictag":
                value = normalize_hash_tag(parse_scalar(value_text, idx, path), idx, path)
            else:
                value = parse_scalar(value_text, idx, path)

            current_props[key] = value
            continue

        if current_tag is None:
            continue

        raise TagIndexSyntaxError(
            f"Errore in {path}, riga {idx}: sintassi non valida dentro il blocco del tag "
            f"#{current_tag}. Atteso formato: '  - **Title**: ...', "
            f"'  - **Description**: ...' o '  - **TopicTag**: ...'"
        )

    finalize_tag_block(tag_defs, entries, current_tag, current_props, current_tag_line, current_section, path)

    if not tag_defs:
        raise TagIndexSyntaxError(
            f"Errore in {path}: nessun tag valido trovato. Attesa sintassi tipo:\n"
            f"- #ob/esempio\n"
            f"  - **Title**: Titolo\n"
            f"  - **Description**: Descrizione\n"
            f"  - **TopicTag**: #ob/esempio"
        )

    return tag_defs, entries


def tag_title(tag: str, tag_defs: dict) -> str:
    info = tag_defs.get(tag, {})
    return str(info.get("title", tag)) if isinstance(info, dict) else tag


def tag_description(tag: str, tag_defs: dict) -> str:
    info = tag_defs.get(tag, {})
    return str(info.get("description", "")) if isinstance(info, dict) else ""


def combo_slug(combo: tuple[str, ...]) -> str:
    return "+".join(slugify(tag) for tag in combo)


def combo_title(combo: tuple[str, ...], tag_defs: dict) -> str:
    return "+".join(tag_title(tag, tag_defs) for tag in combo)


def combo_description(combo: tuple[str, ...], tag_defs: dict) -> str:
    if len(combo) == 1:
        desc = tag_description(combo[0], tag_defs)
        if desc:
            return desc
    return f"Contenuti associati alla combinazione di tag: {combo_title(combo, tag_defs)}."


def format_inline_tags(tags: list[str], tag_defs: dict) -> str:
    return " - ".join(tag_title(tag, tag_defs) for tag in sorted(set(tags), key=lambda x: x.casefold()))


def all_nonempty_tag_combinations(tags: list[str]) -> list[tuple[str, ...]]:
    tags_sorted = sorted(set(tags), key=lambda x: x.casefold())
    combos: list[tuple[str, ...]] = []
    for r in range(1, len(tags_sorted) + 1):
        combos.extend(itertools.combinations(tags_sorted, r))
    return combos


def get_note_metadata(md_path: Path) -> dict | None:
    text = md_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    title = str(fm.get("title") or md_path.stem)
    description = str(fm.get("description", ""))
    tags = normalize_tag_list(fm.get("tags", []))
    rel_path = md_path.relative_to(CONTENT_DIR).as_posix()

    return {
        "title": title,
        "description": description,
        "tags": tags,
        "relative_path": rel_path,
        "source_path": md_path,
        "source_name": md_path.name,
        "body": body,
        "frontmatter": fm,
    }


def collect_notes() -> list[dict]:
    notes = []
    for md_path in sorted(SEMINARI_DIR.rglob("*.md")):
        meta = get_note_metadata(md_path)
        if meta:
            notes.append(meta)
    notes.sort(key=lambda x: x["title"].casefold())
    return notes


def collect_notes_by_combo(notes: list[dict]) -> dict[tuple[str, ...], list[dict]]:
    notes_by_combo: dict[tuple[str, ...], list[dict]] = defaultdict(list)
    for note in notes:
        for combo in all_nonempty_tag_combinations(note["tags"]):
            notes_by_combo[combo].append(note)

    for combo in notes_by_combo:
        notes_by_combo[combo].sort(key=lambda x: x["title"].casefold())

    return notes_by_combo


def sorted_combos(combos) -> list[tuple[str, ...]]:
    return sorted(combos, key=lambda c: ([t.casefold() for t in c], len(c)))


def generate_index(notes: list[dict], tag_defs: dict) -> str:
    all_tags = sorted(
        set(tag_defs.keys()) | {tag for note in notes for tag in note["tags"]},
        key=lambda x: x.casefold(),
    )

    lines = [
        "---",
        'title: "Index"',
        'description: "Home del sito e indice dei contenuti."',
        "---",
        "",
        "# Index",
        "",
        "## Tag disponibili",
        "",
        format_inline_tags(all_tags, tag_defs) if all_tags else "_Nessun tag disponibile._",
        "",
        "## Lista Seminari",
        "",
    ]

    if not notes:
        lines.append("_Nessun seminario disponibile._")
    else:
        for note in notes:
            desc = f" — {note['description']}" if note["description"] else ""
            lines.append(f"- {wiki_link(note['relative_path'], note['title'])}{desc}")
            tag_line = format_inline_tags(note["tags"], tag_defs)
            if tag_line:
                lines.append(f"  - Tags: {tag_line}")

    lines.extend([
        "",
        "## Altri indici",
        "",
        "- [[tag-index|Tag Index]]",
        "",
    ])

    return "\n".join(lines)


def generate_reference_topic_page(
    combo: tuple[str, ...],
    tag_defs: dict,
    notes: list[dict],
) -> str:
    slug = combo_slug(combo)
    human_description = combo_description(combo, tag_defs)

    lines = [
        "---",
        f'title: "{slug}"',
        f'description: "{human_description}"',
        "---",
        "",
        f"# {slug}",
        "",
        human_description,
        "",
        "## Contenuti collegati",
        "",
    ]

    if not notes:
        lines.append("_Nessun contenuto associato a questa sezione._")
    else:
        for note in notes:
            suffix = f" — {note['description']}" if note["description"] else ""
            lines.append(f"- {wiki_link(note['relative_path'], note['title'])}{suffix}")

    lines.append("")
    return "\n".join(lines)

def build_replicated_note(note: dict, combo: tuple[str, ...], tag_defs: dict) -> str:
    source_text = note["source_path"].read_text(encoding="utf-8")
    fm, body = parse_frontmatter(source_text)
    fm = dict(fm)
    fm["replicated_from"] = note["relative_path"]
    fm["topic_section"] = combo_title(combo, tag_defs)
    fm["tag_combo"] = list(combo)

    frontmatter = yaml.safe_dump(
        fm,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).strip()

    banner = (
        f"> Copia generata automaticamente per il topic **{combo_title(combo, tag_defs)}**.\n"
        f"> Sorgente: `/{note['relative_path']}`\n\n"
    )

    return f"---\n{frontmatter}\n---\n\n{banner}{body.lstrip()}"


def generate_ttp_index(combo: tuple[str, ...], tag_defs: dict, notes: list[dict]) -> str:
    title = combo_title(combo, tag_defs)
    description = combo_description(combo, tag_defs)

    lines = [
        "---",
        f'title: "{title}"',
        f'description: "{description}"',
        "---",
        "",
        f"# {title}",
        "",
        description,
        "",
        "## File replicati in questo topic",
        "",
    ]

    if not notes:
        lines.append("_Nessun file disponibile._")
    else:
        for note in notes:
            lines.append(f"- [[{note['source_name']}|{note['title']}]]")

    lines.append("")
    return "\n".join(lines)


def build_reference_topics(notes_by_combo: dict[tuple[str, ...], list[dict]], tag_defs: dict) -> None:
    ensure_dir(REFERENCE_TOPICS_DIR)
    for combo in sorted_combos(notes_by_combo.keys()):
        slug = combo_slug(combo)
        page = generate_reference_topic_page(combo, tag_defs, notes_by_combo[combo])
        (REFERENCE_TOPICS_DIR / f"{slug}.md").write_text(page, encoding="utf-8")


def build_ttp(notes_by_combo: dict[tuple[str, ...], list[dict]], tag_defs: dict) -> None:
    ensure_dir(TTP_DIR)
    for combo in sorted_combos(notes_by_combo.keys()):
        slug = combo_slug(combo)
        folder = TTP_DIR / slug
        ensure_dir(folder)

        index_text = generate_ttp_index(combo, tag_defs, notes_by_combo[combo])
        (folder / "index.md").write_text(index_text, encoding="utf-8")

        for note in notes_by_combo[combo]:
            replica_text = build_replicated_note(note, combo, tag_defs)
            (folder / note["source_name"]).write_text(replica_text, encoding="utf-8")

def tag_public_link(tag: str) -> str:
    return f'<a href="/tags/{tag}/"><code>&#35;{tag}</code></a>'

def taxonomy_tags(entries: list[dict]) -> list[str]:
    topics = {entry["topictag"] for entry in entries}
    return sorted(topics, key=lambda x: x.casefold())

def generate_public_tag_index(entries: list[dict]) -> str:
    taxonomy_line = " - ".join(tag_public_link(tag) for tag in taxonomy_tags(entries))

    lines = [
        "---",
        'title: "Tag Index"',
        'description: "Indice pubblico dei tag e delle loro descrizioni."',
        "---",
        "",
        "## Topic Tags",
        "",
        taxonomy_line if taxonomy_line else "_Nessun topic tag disponibile._",
        "",
        "## Alphabetical Taxonomy Tags",
        "",
    ]

    current_section = None

    for entry in entries:
        section = entry["section"]
        if section != current_section:
            current_section = section
            if current_section:
                lines.extend([
                    f"### {current_section}",
                    "",
                ])

        lines.extend([
            f"- {tag_public_link(entry['tag'])}",
            f"  - **Title:** {entry['title']}",
            f"  - **Description:** {entry['description']}",
            "",
        ])

    return "\n".join(lines)

def main() -> None:
    if not CONTENT_DIR.exists():
        raise FileNotFoundError(f"Cartella 'content' non trovata: {CONTENT_DIR}")
    if not SEMINARI_DIR.exists():
        raise FileNotFoundError(f"Cartella 'content/Lista-Seminari' non trovata: {SEMINARI_DIR}")
    if not TAG_INDEX_SOURCE_FILE.exists():
        raise FileNotFoundError(f"File non trovato: {TAG_INDEX_SOURCE_FILE}")

    try:
        tag_defs, entries = parse_tag_index_source(TAG_INDEX_SOURCE_FILE)
    except TagIndexSyntaxError as e:
        raise SystemExit(str(e))

    notes = collect_notes()
    notes_by_combo = collect_notes_by_combo(notes)

    if CLEAN_REFERENCE_TOPICS:
        cleanup_folder(REFERENCE_TOPICS_DIR)
    else:
        ensure_dir(REFERENCE_TOPICS_DIR)

    if CLEAN_TTP:
        cleanup_folder(TTP_DIR)
    else:
        ensure_dir(TTP_DIR)

    build_reference_topics(notes_by_combo, tag_defs)
    build_ttp(notes_by_combo, tag_defs)

    if REBUILD_TAG_INDEX:
        cleanup_file(TAG_INDEX_FILE)
        TAG_INDEX_FILE.write_text(
            generate_public_tag_index(entries),
            encoding="utf-8",
        )

    if REBUILD_INDEX:
        cleanup_file(INDEX_FILE)
        INDEX_FILE.write_text(
            generate_index(notes, tag_defs),
            encoding="utf-8",
        )

    print("Generazione completata.")
    print(f"Reference Topics rigenerati in: {REFERENCE_TOPICS_DIR}")
    print(f"TTP rigenerato in: {TTP_DIR}")
    if REBUILD_TAG_INDEX:
        print(f"Tag index pubblico rigenerato in: {TAG_INDEX_FILE}")
    if REBUILD_INDEX:
        print(f"Index rigenerato in: {INDEX_FILE}")


if __name__ == "__main__":
    main()