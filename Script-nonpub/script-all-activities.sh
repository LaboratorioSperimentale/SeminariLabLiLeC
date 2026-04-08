#!/usr/bin/env bash
set -Eeuo pipefail

# ============================================================
# publish-site-on-gh-pages.sh
#
# Scopo:
#   1. Facoltativamente preprocessa il vault per i tag
#   2. Facoltativamente genera il sito Quartz
#   3. Fa commit e push del vault/sorgenti su branch main
#      (escludendo output compilati Quartz)
#   4. Sincronizza quartz-site/quartz-4/public/ nella worktree
#      ../SeminariLabLiLeC-pages
#   5. Preserva .git e .nojekyll
#   6. Fa commit e push sul branch gh-pages
#
# Uso tipico:
#   Solo pubblicazione del public già generato:
#     ./Script-nonpub/publish-site-on-gh-pages.sh
#
#   Preprocess + build + pubblicazione:
#     ./Script-nonpub/publish-site-on-gh-pages.sh --all
#
#   Solo build + pubblicazione:
#     ./Script-nonpub/publish-site-on-gh-pages.sh --build
#
#   Solo preprocess + pubblicazione:
#     ./Script-nonpub/publish-site-on-gh-pages.sh --preprocess
# ============================================================

log() {
  printf '\n==> %s\n' "$*"
}

die() {
  printf '\n[ERRORE] %s\n' "$*" >&2
  exit 1
}

usage() {
  cat <<'EOF'
Uso:
  publish-site-on-gh-pages.sh [opzioni]

Opzioni:
  --preprocess          Esegue script-generate_tag-sections.py prima della pubblicazione
  --build               Esegue script-generate-quartz-site prima della pubblicazione
  --all                 Esegue preprocess + build + pubblicazione
  -m, --message         Messaggio commit per gh-pages
  --main-message        Messaggio commit per main
  -h, --help            Mostra questo aiuto

Esempi:
  ./Script-nonpub/publish-site-on-gh-pages.sh
  ./Script-nonpub/publish-site-on-gh-pages.sh --build
  ./Script-nonpub/publish-site-on-gh-pages.sh --all
  ./Script-nonpub/publish-site-on-gh-pages.sh --all -m "Publish updated seminar site"
  ./Script-nonpub/publish-site-on-gh-pages.sh --all --main-message "Update vault sources"
EOF
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "Comando non trovato: $1"
}

# ------------------------------------------------------------
# Path principali ricavati automaticamente
# ------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
PARENT_DIR="$(cd "${VAULT_DIR}/.." && pwd)"

# Path modificabili via variabili d'ambiente, se un giorno ti servisse
PAGES_DIR="${PAGES_DIR:-${PARENT_DIR}/SeminariLabLiLec-pages}"
PUBLIC_DIR="${PUBLIC_DIR:-${VAULT_DIR}/quartz-site/quartz-4/public}"

PREPROCESS_SCRIPT="${PREPROCESS_SCRIPT:-${SCRIPT_DIR}/script-generate_tag-sections.py}"
BUILD_SCRIPT="${BUILD_SCRIPT:-${SCRIPT_DIR}/script-generate-quartz-site}"

RUN_PREPROCESS=0
RUN_BUILD=0
PAGES_COMMIT_MESSAGE="Update published site"
MAIN_COMMIT_MESSAGE="Update Obsidian vault sources"

# Output compilati da NON committare su main
MAIN_EXCLUDE_PUBLIC="quartz-site/quartz-4/public"
MAIN_EXCLUDE_CACHE="quartz-site/quartz-4/.quartz-cache"

# ------------------------------------------------------------
# Parsing argomenti
# ------------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --preprocess)
      RUN_PREPROCESS=1
      shift
      ;;
    --build)
      RUN_BUILD=1
      shift
      ;;
    --all)
      RUN_PREPROCESS=1
      RUN_BUILD=1
      shift
      ;;
    -m|--message)
      [[ $# -lt 2 ]] && die "Manca il testo del commit dopo $1"
      PAGES_COMMIT_MESSAGE="$2"
      shift 2
      ;;
    --main-message)
      [[ $# -lt 2 ]] && die "Manca il testo del commit dopo $1"
      MAIN_COMMIT_MESSAGE="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "Opzione sconosciuta: $1"
      ;;
  esac
done

# ------------------------------------------------------------
# Controlli di base
# ------------------------------------------------------------
require_cmd git
require_cmd rsync

[[ -d "$VAULT_DIR" ]] || die "Vault non trovato: $VAULT_DIR"
[[ -d "$PAGES_DIR" ]] || die "Cartella worktree gh-pages non trovata: $PAGES_DIR"

git -C "$VAULT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1 \
  || die "Il vault non è una repository Git valida: $VAULT_DIR"

git -C "$PAGES_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1 \
  || die "La cartella gh-pages non è una worktree/repository Git valida: $PAGES_DIR"

CURRENT_VAULT_BRANCH="$(git -C "$VAULT_DIR" branch --show-current)"
[[ "$CURRENT_VAULT_BRANCH" == "main" ]] \
  || die "Il vault NON è sul branch main ma su: $CURRENT_VAULT_BRANCH"

CURRENT_PAGES_BRANCH="$(git -C "$PAGES_DIR" branch --show-current)"
[[ "$CURRENT_PAGES_BRANCH" == "gh-pages" ]] \
  || die "La worktree di pubblicazione NON è sul branch gh-pages ma su: $CURRENT_PAGES_BRANCH"

# ------------------------------------------------------------
# Step 1: preprocess opzionale
# ------------------------------------------------------------
if [[ "$RUN_PREPROCESS" -eq 1 ]]; then
  require_cmd python3
  [[ -f "$PREPROCESS_SCRIPT" ]] || die "Script Python non trovato: $PREPROCESS_SCRIPT"

  log "Eseguo preprocessing tags"
  python3 "$PREPROCESS_SCRIPT"
fi

# ------------------------------------------------------------
# Step 2: build Quartz opzionale
# ------------------------------------------------------------
if [[ "$RUN_BUILD" -eq 1 ]]; then
  [[ -f "$BUILD_SCRIPT" ]] || die "Script build Quartz non trovato: $BUILD_SCRIPT"

  log "Eseguo build Quartz"
  bash "$BUILD_SCRIPT"
fi

# ------------------------------------------------------------
# Step 3: controllo output statico
# ------------------------------------------------------------
[[ -d "$PUBLIC_DIR" ]] || die "Cartella public non trovata: $PUBLIC_DIR"
[[ -f "$PUBLIC_DIR/index.html" ]] || die "index.html non trovato in: $PUBLIC_DIR"

# ------------------------------------------------------------
# Step 4: commit e push del vault su main
# Esclude output compilati Quartz
# ------------------------------------------------------------
log "Preparo commit del vault su main (escludo public e cache Quartz)"

git -C "$VAULT_DIR" add -A .

# Se public o cache fossero finiti nello staging, li tolgo.
git -C "$VAULT_DIR" reset -q HEAD -- "$MAIN_EXCLUDE_PUBLIC" "$MAIN_EXCLUDE_CACHE" 2>/dev/null || true

if git -C "$VAULT_DIR" diff --cached --quiet; then
  log "Nessuna modifica sorgente da pushare su main"
else
  log "Committo i cambiamenti del vault su main"
  git -C "$VAULT_DIR" commit -m "$MAIN_COMMIT_MESSAGE"

  log "Push su origin/main"
  git -C "$VAULT_DIR" push origin main
fi

# ------------------------------------------------------------
# Step 5: sincronizzazione public -> gh-pages
# Preserva .git e .nojekyll
# ------------------------------------------------------------
log "Sincronizzo public verso gh-pages"
rsync -av --delete \
  --exclude='.git' \
  --exclude='.nojekyll' \
  "${PUBLIC_DIR}/" "${PAGES_DIR}/"

# Garantisce sempre la presenza di .nojekyll
touch "${PAGES_DIR}/.nojekyll"

# ------------------------------------------------------------
# Step 6: commit e push di gh-pages
# ------------------------------------------------------------
log "Aggiungo i cambiamenti in gh-pages"
git -C "$PAGES_DIR" add -A

if git -C "$PAGES_DIR" diff --cached --quiet; then
  log "Nessuna modifica da pubblicare su gh-pages. Esco."
  exit 0
fi

log "Committo i cambiamenti in gh-pages"
git -C "$PAGES_DIR" commit -m "$PAGES_COMMIT_MESSAGE"

log "Push su origin/gh-pages"
git -C "$PAGES_DIR" push origin gh-pages

log "Pubblicazione completata con successo"
