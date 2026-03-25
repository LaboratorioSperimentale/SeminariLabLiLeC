#!/usr/bin/env python3

"""
Genera pagine-tag per un vault Obsidian.

Cosa fa:
- Scansiona i file .md del vault
- Estrae i tag dal frontmatter YAML (campo tags:)
- Estrae anche i tag inline nel corpo (#tag)
- Crea una pagina markdown per ogni tag
- Inserisce nella pagina l'elenco delle note collegate come wikilink Obsidian

Uso:
    python3 generate_tag_sections.py

Uso con parametri:
    python3 generate_tag_sections.py /percorso/del/vault /percorso/output/tag-pages

Esempio:
    python3 generate_tag_sections.py . tags

Note:
- Lancia lo script dalla root del vault, oppure passa il path del vault come primo argomento.
- Le pagine tag vengono create/aggiornate nella cartella di output.
- I file nella cartella di output NON vengono riletti come note sorgente.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple

# -----------------------------
# CONFIGURAZIONE BASE
# -----------------------------

DEFAULT_OUTPUT_DIRNAME = "tags"

# Se vuoi descrizioni personalizzate per alcuni tag, mettile qui.
# Chiave = tag tecnico
# Valore = descrizione leggibile
TAG_DESCRIPTIONS: Dict[str, str] = {
    # "uno": "Pagina introduttiva del tag Uno.",
    # "pedagogia": "Materiali e note relativi alla pedagogia.",
    # "seminari": "Raccolta delle note collegate ai seminari.",
}

# Se vuoi ignorare certi tag, mettili qui
IGNORED_TAGS: Set[str] = {
    # "tmp",
    # "draft",
}

# Cartelle da ignorare durante la scansione
IGNORED_DIR_NAMES: Set[str] = {
    ".obsidian",
    ".git",
    ".trash",
    ".quartz-cache",
    "node_modules",
    DEFAULT_OUTPUT_DIRNAME,  # evita di rileggere le pagine tag generate
}

# -----------------------------
# REGEX
# -----------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
INLINE_TAG_RE = re.compile(r"(?<![\w/])#([A-Za-z0-9_/\-]+)")
YAML_LIST_ITEM_RE = re.compile(r"^\s*-\s+(.+?)\s*$")
YAML_TAGS_INLINE_LIST_RE = re.compile(r"^\s*tags\s*:\s*\[(.*?)\]\s*$", re.IGNORECASE)
YAML_TAGS_KEY_RE = re.compile(r"^\s*tags\s*:\s*$", re.IGNORECASE)
YAML_SIMPLE_KEYVAL_RE = re.compile(r"^\s*([A-Za-z0-9_-]+)\s*:\s*(.*?)\s*$")

# -----------------------------
# UTILITY
# -----------------------------

def normalize_tag(tag: str) -> str:
    """Normalizza il tag togliendo #, spazi esterni e slash finali."""
    tag = tag.strip().lstrip("#").strip()
    tag = tag.strip("/")
    return tag

def slug_to_title(tag: str) -> str:
    """
    Trasforma un tag tecnico in titolo leggibile.
    Esempio: 'capitolo-uno' -> 'Capitolo Uno'
    """
    parts = re.split(r"[-_/]+", tag)
    return " ".join(p.capitalize() for p in parts if p)

def safe_tag_filename(tag: str) -> str:
    """
    Converte il tag in nome file sicuro.
    Mantiene lettere, numeri, -, _, / trasformando / in __
    """
    filename = tag.replace("/", "__")
    filename = re.sub(r"[^A-Za-z0-9_\-]+", "-", filename).strip("-")
    return filename or "tag-senza-nome"

def extract_frontmatter_and_body(text: str) -> Tuple[str, str]:
    """Restituisce (frontmatter, body). Se non c'è frontmatter, il primo è vuoto."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return "", text
    frontmatter = match.group(1)
    body = text[match.end():]
    return frontmatter, body

def extract_tags_from_frontmatter(frontmatter: str) -> Set[str]:
    """
    Estrae i tag dal frontmatter YAML in modo semplice, senza dipendere da PyYAML.
    Supporta:
        tags:
          - uno
          - due
        tags: [uno, due]
        tags: uno
    """
    tags: Set[str] = set()
    if not frontmatter.strip():
        return tags

    lines = frontmatter.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        # Caso: tags: [uno, due]
        inline_list_match = YAML_TAGS_INLINE_LIST_RE.match(line)
        if inline_list_match:
            raw_items = inline_list_match.group(1)
            for item in raw_items.split(","):
                tag = normalize_tag(item.strip().strip('"').strip("'"))
                if tag:
                    tags.add(tag)
            i += 1
            continue

        # Caso:
        # tags:
        #   - uno
        #   - due
        if YAML_TAGS_KEY_RE.match(line):
            i += 1
            while i < len(lines):
                item_line = lines[i]

                # Se trovo una nuova chiave YAML, esco
                keyval = YAML_SIMPLE_KEYVAL_RE.match(item_line)
                listitem = YAML_LIST_ITEM_RE.match(item_line)

                if keyval and not listitem:
                    break

                if listitem:
                    raw = listitem.group(1).strip().strip('"').strip("'")
                    tag = normalize_tag(raw)
                    if tag:
                        tags.add(tag)

                i += 1
            continue

        # Caso: tags: uno
        keyval = YAML_SIMPLE_KEYVAL_RE.match(line)
        if keyval and keyval.group(1).lower() == "tags":
            raw = keyval.group(2).strip().strip('"').strip("'")
            tag = normalize_tag(raw)
            if tag:
                tags.add(tag)

        i += 1

    return tags

def extract_inline_tags(body: str) -> Set[str]:
    """Estrae i tag inline dal corpo della nota."""
    tags = {normalize_tag(m.group(1)) for m in INLINE_TAG_RE.finditer(body)}
    return {t for t in tags if t}

def note_title_from_path(md_path: Path) -> str:
    """Per wikilink Obsidian semplice: usa il nome file senza estensione."""
    return md_path.stem

def should_ignore_path(path: Path, output_dir: Path) -> bool:
    """Ignora cartelle tecniche e la cartella di output."""
    parts = set(path.parts)
    if output_dir.name in parts:
        return True
    return any(part in IGNORED_DIR_NAMES for part in parts)

def collect_markdown_files(vault_root: Path, output_dir: Path) -> List[Path]:
    """Raccoglie tutti i file .md del vault, esclusa la cartella di output."""
    result: List[Path] = []
    for path in vault_root.rglob("*.md"):
        if should_ignore_path(path, output_dir):
            continue
        result.append(path)
    return sorted(result)

def build_tag_index(vault_root: Path, output_dir: Path) -> Dict[str, List[Path]]:
    """
    Costruisce una mappa:
        tag -> [lista file markdown che possiedono quel tag]
    """
    tag_index: Dict[str, List[Path]] = defaultdict(list)
    md_files = collect_markdown_files(vault_root, output_dir)

    for md_file in md_files:
        try:
            text = md_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            # prova di fallback
            text = md_file.read_text(encoding="latin-1")

        frontmatter, body = extract_frontmatter_and_body(text)

        tags = set()
        tags.update(extract_tags_from_frontmatter(frontmatter))
        tags.update(extract_inline_tags(body))

        tags = {
            normalize_tag(t)
            for t in tags
            if t and normalize_tag(t) not in IGNORED_TAGS
        }

        for tag in sorted(tags):
            tag_index[tag].append(md_file)

    # dedup e sort finale
    for tag, files in tag_index.items():
        unique_sorted = sorted(set(files), key=lambda p: p.stem.lower())
        tag_index[tag] = unique_sorted

    return dict(sorted(tag_index.items(), key=lambda item: item[0].lower()))

def render_tag_page(tag: str, note_paths: List[Path], vault_root: Path) -> str:
    """
    Crea il contenuto markdown della pagina tag.
    Usa wikilink Obsidian: [[NomeNota]]
    """
    title = slug_to_title(tag)
    description = TAG_DESCRIPTIONS.get(tag, f"Pagina del tag {title}.")
    note_count = len(note_paths)

    lines: List[str] = []

    lines.append("---")
    lines.append(f'title: "{title}"')
    lines.append(f'tag-id: "{tag}"')
    lines.append(f'description: "{description}"')
    lines.append("---")
    lines.append("")
    lines.append(f"# {title}")
    lines.append("")
    lines.append(description)
    lines.append("")
    lines.append(f"**Numero note:** {note_count}")
    lines.append("")
    lines.append("## Note collegate")
    lines.append("")

    if not note_paths:
        lines.append("_Nessuna nota collegata._")
        lines.append("")
        return "\n".join(lines)

    for note_path in note_paths:
        note_name = note_title_from_path(note_path)
        rel_path = note_path.relative_to(vault_root).as_posix()
        lines.append(f"- [[{note_name}]]")
        lines.append(f"  - `{rel_path}`")

    lines.append("")
    return "\n".join(lines)

def write_tag_pages(tag_index: Dict[str, List[Path]], vault_root: Path, output_dir: Path) -> None:
    """Scrive una pagina markdown per ogni tag."""
    output_dir.mkdir(parents=True, exist_ok=True)

    for tag, note_paths in tag_index.items():
        filename = safe_tag_filename(tag) + ".md"
        out_file = output_dir / filename
        content = render_tag_page(tag, note_paths, vault_root)
        out_file.write_text(content, encoding="utf-8")

def write_index_page(tag_index: Dict[str, List[Path]], output_dir: Path) -> None:
    """
    Crea un index.md nella cartella tags con elenco inline dei tag,
    ordinati alfabeticamente e separati da ' - '.
    """
    tags_sorted = sorted(tag_index.keys(), key=str.lower)

    lines: List[str] = []
    lines.append("---")
    lines.append('title: "Indice dei tag"')
    lines.append('description: "Indice delle sezioni generate dai tag."')
    lines.append("---")
    lines.append("")
    lines.append("# Indice dei tag")
    lines.append("")
    lines.append("## Tag disponibili")
    lines.append("")

    if tags_sorted:
        inline_links = []
        for tag in tags_sorted:
            page_name = safe_tag_filename(tag)
            label = slug_to_title(tag)
            inline_links.append(f"[[{output_dir.name}/{page_name}|{label}]]")
        lines.append(" - ".join(inline_links))
    else:
        lines.append("_Nessun tag trovato._")

    lines.append("")
    (output_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")

def main() -> None:
    vault_root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    output_dir = (
        Path(sys.argv[2]).resolve()
        if len(sys.argv) > 2
        else (vault_root / DEFAULT_OUTPUT_DIRNAME).resolve()
    )

    if not vault_root.exists() or not vault_root.is_dir():
        print(f"ERRORE: vault non trovato o non valido: {vault_root}")
        sys.exit(1)

    print(f"Vault:   {vault_root}")
    print(f"Output:  {output_dir}")

    tag_index = build_tag_index(vault_root, output_dir)

    if not tag_index:
        print("Nessun tag trovato nelle note.")
        sys.exit(0)

    write_tag_pages(tag_index, vault_root, output_dir)
    write_index_page(tag_index, output_dir)

    total_tags = len(tag_index)
    total_links = sum(len(v) for v in tag_index.values())

    print(f"Generate {total_tags} pagine tag.")
    print(f"Totale collegamenti tag -> note: {total_links}")
    print("Fatto.")

if __name__ == "__main__":
    main()