#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# SCRIPT: quartz-build-serve.sh
#
# SCOPO
# - Caricare l'ambiente Node corretto per Quartz
# - Verificare che Quartz sia nella cartella giusta
# - Verificare che content/ esista davvero
# - Lanciare build + preview locale di Quartz
#
# USO
# Dalla root del progetto, oppure da qualunque cartella:
#
#   bash quartz-nonpub/quartz-build-serve.sh
#
# NOTA IMPORTANTE
# Questo script NON usa Python e NON usa il venv.
# Quartz gira su Node/npm/npx.
# ============================================================


# ------------------------------------------------------------
# 1. Individuazione dei percorsi
# ------------------------------------------------------------
# SCRIPT_DIR  = cartella in cui si trova questo script
# PROJECT_ROOT = root del progetto (assunta come cartella padre di quartz-nonpub)
# QUARTZ_DIR   = cartella del progetto Quartz
# ------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
QUARTZ_DIR="$PROJECT_ROOT/quartz-site/quartz-4"

echo "==> Root progetto: $PROJECT_ROOT"
echo "==> Cartella Quartz: $QUARTZ_DIR"


# ------------------------------------------------------------
# 2. Controllo che la cartella Quartz esista
# ------------------------------------------------------------
if [[ ! -d "$QUARTZ_DIR" ]]; then
  echo "ERRORE: cartella Quartz non trovata: $QUARTZ_DIR"
  exit 1
fi


# ------------------------------------------------------------
# 3. Caricamento di nvm
# ------------------------------------------------------------
# nvm serve per selezionare la versione corretta di Node.
# Quartz richiede Node >= 22.
# ------------------------------------------------------------
export NVM_DIR="$HOME/.nvm"

if [[ -s "$NVM_DIR/nvm.sh" ]]; then
  # shellcheck disable=SC1090
  . "$NVM_DIR/nvm.sh"
else
  echo "ERRORE: nvm non trovato in $NVM_DIR"
  exit 1
fi


# ------------------------------------------------------------
# 4. Attivazione di Node 22
# ------------------------------------------------------------
# nvm use 22 seleziona Node 22 nella shell corrente.
# hash -r ripulisce eventuali percorsi in cache della shell.
# ------------------------------------------------------------
echo "==> Attivo Node 22 con nvm..."
nvm use 22 >/dev/null
hash -r


# ------------------------------------------------------------
# 5. Verifica dei binari effettivamente in uso
# ------------------------------------------------------------
# Questi controlli servono a rendere visibile l'ambiente reale.
# ------------------------------------------------------------
echo "==> Verifica ambiente Node"
echo "node: $(which node)"
echo "npm:  $(which npm)"
echo "npx:  $(which npx)"
echo "node version: $(node -v)"
echo "npm version:  $(npm -v)"


# ------------------------------------------------------------
# 6. Entrata nella cartella Quartz
# ------------------------------------------------------------
cd "$QUARTZ_DIR"

echo "==> Contenuto cartella Quartz:"
ls


# ------------------------------------------------------------
# 7. Controllo che il file package.json esista
# ------------------------------------------------------------
# Se manca, non siamo in un progetto Quartz valido.
# ------------------------------------------------------------
if [[ ! -f "package.json" ]]; then
  echo "ERRORE: package.json non trovato in $QUARTZ_DIR"
  exit 1
fi


# ------------------------------------------------------------
# 8. Controllo che content/ esista
# ------------------------------------------------------------
# Quartz legge SOLO la sua cartella content/.
# Se content manca o è vuota, builderà il vuoto.
# ------------------------------------------------------------
if [[ ! -e "content" ]]; then
  echo "ERRORE: content/ non esiste in $QUARTZ_DIR"
  exit 1
fi

echo "==> Verifica content/"
ls -l content
echo
echo "==> Contenuto di content/"
ls content


# ------------------------------------------------------------
# 9. Controllo minimo della home
# ------------------------------------------------------------
# Quartz si aspetta una home in content/index.md.
# Se manca, segnaliamo il problema ma non fermiamo per forza lo script.
# ------------------------------------------------------------
if [[ ! -f "content/index.md" ]]; then
  echo "ATTENZIONE: content/index.md non esiste."
  echo "Quartz potrebbe buildare con warning o routing incompleto."
fi


# ------------------------------------------------------------
# 10. Build del sito
# ------------------------------------------------------------
echo "==> Lancio build Quartz..."
npx quartz build


# ------------------------------------------------------------
# 11. Avvio preview locale
# ------------------------------------------------------------
# Questo avvia il server locale per vedere il sito nel browser.
# ------------------------------------------------------------
echo "==> Avvio preview locale Quartz..."
npx quartz build --serve

