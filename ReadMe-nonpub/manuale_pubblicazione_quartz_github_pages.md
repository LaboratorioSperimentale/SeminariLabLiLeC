# Manualetto operativo per la pubblicazione del sito Quartz su GitHub Pages

Correzione ortografica: **indicazione**, non *inidcazione*.

## 1. Scopo

Questo manualetto descrive la procedura concreta per pubblicare il sito Quartz del progetto **SeminariLabLiLeC** usando:

- una **repo principale** con tutti i sorgenti;
- una cartella/worktree separata per il branch **`gh-pages`**;
- uno script **`.sh`** che sincronizza il sito generato e poi esegue commit e push.

Chiarisce anche il punto più delicato emerso durante il lavoro: il rapporto tra

- **hashtag usati in Obsidian**;
- **tassonomia mantenuta in `tag-index-source-nonpub.md`**;
- **pagine `Topics/...` generate da script Python**;
- **sistema automatico dei tag di Quartz (`/tags/...`)**.

L’obiettivo è avere una pipeline semplice, ripetibile, e senza conflitti tra sistemi concorrenti.

---

## 2. Architettura del progetto

### 2.1 Repo principale

Cartella locale principale di lavoro:

`SeminariLabLiLeC`

Qui stanno i sorgenti reali del progetto. In particolare:

- file markdown del vault/contenuti;
- script Python per generazione pagine, topics, intersezioni e derivati;
- script di build del sito Quartz;
- script di pubblicazione del sito statico;
- configurazione Git e Quartz;
- eventuali script di supporto e automazione.

In altre parole: **la repo principale è la sorgente di verità del progetto**.

### 2.2 Cartella del sito statico generato

Output della build Quartz:

`quartz-site/quartz-4/public/`

Questa cartella contiene il sito statico già pronto per la pubblicazione.

Non è la cartella in cui si lavora manualmente sui contenuti: è il risultato della build.

### 2.3 Cartella/worktree del branch pubblicato

Cartella locale dedicata al branch GitHub Pages:

`../SeminariLabLiLec-pages`

Questa cartella è un **worktree Git separato** collegato al branch `gh-pages`.

Serve solo a ricevere i file statici generati e a fare commit/push della versione pubblicata del sito.

Punto importante: **non è una seconda repo autonoma da gestire a mano**. È una cartella di pubblicazione.

---

## 3. Modello operativo corretto

La procedura corretta è questa:

1. si lavora nella repo principale `SeminariLabLiLeC`;
2. si aggiornano contenuti, tassonomia, script e configurazione;
3. si esegue la build del sito Quartz;
4. si sincronizza `quartz-site/quartz-4/public/` dentro `../SeminariLabLiLec-pages`;
5. si fa commit e push **nel worktree `gh-pages`**.

Questo evita di mischiare sorgenti e artefatti pubblicati nello stesso albero di lavoro.

---

## 4. Cosa c’è nella repo principale

Nella repo principale convivono tre livelli diversi, che vanno tenuti distinti mentalmente:

### 4.1 Contenuti

Sono i markdown, i metadati YAML, le pagine del vault, i seminari, le sezioni topics, ecc.

### 4.2 Logica di trasformazione

Sono gli script Python che:

- leggono i contenuti;
- interpretano i tag;
- costruiscono pagine `Topics/...`;
- costruiscono intersezioni;
- costruiscono indici;
- eventualmente generano repliche o strutture di supporto.

### 4.3 Logica di pubblicazione

Sono gli script shell che:

- prendono il risultato della build Quartz;
- lo copiano nel worktree `gh-pages`;
- preservano `.git` e `.nojekyll`;
- eseguono add/commit/push.

Se questi tre livelli vengono confusi, iniziano i problemi: pagine duplicate, routing incoerente, 404, branch sbagliati, artefatti vecchi ancora pubblicati.

---

## 5. Branch e worktree: il punto da non sbagliare

### 5.1 Repo principale

Nella repo principale lavori sul branch di sviluppo normale, per esempio `main`.

### 5.2 Worktree di pubblicazione

Nel worktree `../SeminariLabLiLec-pages` devi avere il branch `gh-pages`.

### 5.3 Conseguenza pratica

Per pubblicare **non devi cambiare branch nella repo principale**, se il worktree `gh-pages` è già configurato correttamente.

Devi invece:

- restare nella repo principale per buildare;
- sincronizzare i file generati nel worktree `gh-pages`;
- fare commit/push nel worktree.

---

## 6. Comandi Git minimi di controllo

### Vedere su quale branch sei nella cartella corrente

```bash
git branch --show-current
```

### Vedere branch corrente e tracking remoto

```bash
git branch -vv
```

### Vedere status sintetico

```bash
git status -sb
```

### Fare gli stessi controlli sul worktree `gh-pages`

```bash
git -C ../SeminariLabLiLec-pages branch --show-current
git -C ../SeminariLabLiLec-pages branch -vv
git -C ../SeminariLabLiLec-pages status -sb
```

### Cambiare branch nella cartella corrente

```bash
git switch nome-branch
```

Esempio:

```bash
git switch gh-pages
```

### Creare/agganciare un branch locale al remoto

```bash
git switch -c gh-pages --track origin/gh-pages
```

---

## 7. Setup iniziale del worktree `gh-pages`

Se il worktree di pubblicazione non esiste ancora, la procedura standard è:

```bash
git fetch origin
git worktree add -B gh-pages ../SeminariLabLiLec-pages origin/gh-pages
```

Questo crea una cartella separata collegata al branch `gh-pages`.

Poi conviene creare subito anche `.nojekyll`:

```bash
touch ../SeminariLabLiLec-pages/.nojekyll
```

---

## 8. Caso di worktree rotto o danneggiato

Il problema tipico è perdere `.git` nel worktree di pubblicazione.

### 8.1 Perché succede

Nel worktree separato, `.git` spesso **non è una cartella**, ma un **file**. Se si usa `rsync --delete` proteggendo solo `.git/` e non `.git`, si rischia di cancellarlo.

Errore tipico:

```bash
--exclude='.git/'
```

Questo protegge una cartella `.git`, ma **non protegge un file `.git`**.

### 8.2 Forma corretta di protezione

Bisogna escludere entrambe le forme:

```bash
--exclude='.git'
--exclude='.git/'
```

### 8.3 Recupero prudente del worktree rotto

Se il worktree è rotto, la forma prudente è:

```bash
mv ../SeminariLabLiLec-pages ../SeminariLabLiLec-pages.BROKEN
git worktree prune
git fetch origin
git worktree add -B gh-pages ../SeminariLabLiLec-pages origin/gh-pages
touch ../SeminariLabLiLec-pages/.nojekyll
```

Questa soluzione conserva una copia della cartella danneggiata prima di ricrearla pulita.

---

## 9. Build del sito

La build del sito va eseguita nella repo principale.

Esempio tipico:

```bash
cd quartz-site/quartz-4
npx quartz build
```

Oppure con script dedicato già presente nel progetto, se preferisci una pipeline standardizzata.

Il punto non è il nome del comando, ma il risultato: alla fine devi avere i file statici aggiornati in:

`quartz-site/quartz-4/public/`

---

## 10. Script di pubblicazione `.sh`

Lo script seguente assume che venga lanciato dalla cartella principale `SeminariLabLiLeC`.

### 10.1 Contenuto dello script

Salvare come per esempio:

`publish-gh-pages.sh`

```bash
#!/usr/bin/env bash
set -euxo pipefail

SOURCE_DIR="quartz-site/quartz-4/public/"
PAGES_DIR="../SeminariLabLiLec-pages"
COMMIT_MSG="${1:-Update site}"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "ERROR: source folder not found: $SOURCE_DIR"
  exit 1
fi

if [ ! -e "$PAGES_DIR/.git" ]; then
  echo "ERROR: $PAGES_DIR/.git not found."
  echo "In a git worktree, .git is often a FILE, not a folder."
  echo "Recreate the worktree first."
  exit 1
fi

CURRENT_BRANCH="$(git -C "$PAGES_DIR" branch --show-current)"
if [ "$CURRENT_BRANCH" != "gh-pages" ]; then
  echo "ERROR: target worktree is on branch '$CURRENT_BRANCH', not 'gh-pages'"
  exit 1
fi

echo "==> Syncing $SOURCE_DIR -> $PAGES_DIR"
rsync -av --delete \
  --exclude='.git' \
  --exclude='.git/' \
  --exclude='.nojekyll' \
  "$SOURCE_DIR" "$PAGES_DIR/"

echo "==> Recreating .nojekyll"
touch "$PAGES_DIR/.nojekyll"

echo "==> Git status"
git -C "$PAGES_DIR" status

echo "==> Adding files"
git -C "$PAGES_DIR" add -A

if git -C "$PAGES_DIR" diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

echo "==> Committing"
git -C "$PAGES_DIR" commit -m "$COMMIT_MSG"

echo "==> Pushing to gh-pages"
git -C "$PAGES_DIR" push origin gh-pages

echo "==> Publish completed."
```

### 10.2 Rendere eseguibile lo script

```bash
chmod +x publish-gh-pages.sh
```

### 10.3 Lancio standard

```bash
./publish-gh-pages.sh
```

### 10.4 Lancio con messaggio di commit personalizzato

```bash
./publish-gh-pages.sh "Update Quartz site"
```

### 10.5 Lancio tracciato

Se vuoi vedere passo per passo l’esecuzione:

```bash
bash -x ./publish-gh-pages.sh
```

Nel caso presente, lo script ha già `set -x` incorporato tramite `set -euxo pipefail`, quindi la traccia è già attiva.

---

## 11. Procedura operativa completa

Questa è la sequenza pratica consigliata.

### 11.1 Aggiornare i contenuti e gli script

Lavorare nella repo principale su markdown, YAML, script Python, configurazione Quartz, tassonomia, ecc.

### 11.2 Rigenerare i contenuti derivati

Eseguire gli script Python che producono:

- topics;
- intersezioni;
- indici;
- eventuali pagine di supporto.

### 11.3 Eseguire la build Quartz

Produrre il sito statico in `quartz-site/quartz-4/public/`.

### 11.4 Pubblicare con lo script shell

```bash
./publish-gh-pages.sh
```

### 11.5 Verificare

Controllare:

- che il push su `gh-pages` sia andato a buon fine;
- che GitHub Pages abbia aggiornato il sito;
- che i link principali non producano 404;
- che non siano riapparse pagine residue del vecchio sistema.

---

## 12. Hashtag in Obsidian e tassonomia: il punto davvero delicato

Qui sta una delle questioni architetturali più importanti.

### 12.1 Cosa vuoi ottenere

Vuoi poter usare i tag in Obsidian con la sintassi normale `#tag`, così da sfruttare:

- la navigazione di Obsidian;
- la ricerca per tag;
- il file `tag-index-source-nonpub.md` come tassonomia controllata.

Questo è sensato.

### 12.2 Il problema

Quartz ha un proprio sistema automatico di gestione dei tag. Se nel markdown pubblico restano hashtag grezzi come:

```md
#ob/animali
#ob/corpora
```

Quartz tende a considerarli tag del suo sistema e può generare o aspettarsi pagine in percorsi tipo:

`/tags/ob/animali`

Questo entra in conflitto con la tua architettura custom, che invece vuole pagine generate da script in percorsi tipo:

- `Topics/animali`
- `Topics/corpora`
- `Topics/_intersezioni/...`

### 12.3 Strategia corretta

La strategia corretta è separare i due piani:

#### Piano A — uso interno in Obsidian
Nei file del vault puoi usare gli hashtag con `#` se ti servono davvero come tag Obsidian.

#### Piano B — pubblicazione sul sito
Nelle pagine pubbliche che devono navigare verso i topics non conviene affidarsi agli hashtag grezzi.

Serve invece che i collegamenti siano **espliciti nel markdown generato**, per esempio:

```md
[[Topics/animali|animali]]
```

oppure, se vuoi mostrare anche il prefisso simbolico:

```md
[[Topics/animali|#ob/animali]]
```

In questo modo il link è sotto il tuo controllo, non sotto quello del sistema automatico dei tag Quartz.

### 12.4 Conclusione operativa sulla tassonomia

`tag-index-source-nonpub.md` può continuare a svolgere la funzione di:

- archivio tassonomico;
- fonte per lo script Python;
- riferimento concettuale per Obsidian.

Ma la navigazione pubblica del sito deve essere costruita **via pagine markdown generate da script con link espliciti**, non lasciata al comportamento automatico di Quartz sui tag.

---

## 13. Errore già emerso: pagina concorrente del vecchio sistema

È emerso un conflitto concreto con un file pubblico vecchio:

`content/tag-index.md`

Quella pagina generava link verso il sistema automatico Quartz dei tag, non verso il sistema `Topics/...` prodotto dallo script.

Questo ha creato una situazione ambigua:

- una parte del sito usava il sistema custom;
- un’altra parte puntava ancora a `/tags/...`.

Risultato: pagine concorrenti, incoerenza architetturale, possibili 404.

### Regola pratica

Se la navigazione pubblica deve usare il sistema custom generato da script, allora:

- le vecchie pagine del sistema `tag-index` vanno rimosse o assorbite;
- i link pubblici devono puntare a `Topics/...`;
- gli hashtag grezzi non devono guidare la navigazione pubblica.

---

## 14. Convenzione consigliata per i tag

Per evitare caos, conviene distinguere tre rappresentazioni dello stesso concetto:

### 14.1 Forma tassonomica canonica
Esempio:

`ob/animali`

Questa è utile come identificatore pulito lato script.

### 14.2 Forma Obsidian interna
Esempio:

`#ob/animali`

Questa è utile come tag vero nel vault Obsidian.

### 14.3 Forma di navigazione pubblica
Esempio:

`[[Topics/animali|#ob/animali]]`

oppure

`[[Topics/animali|animali]]`

Questa è la forma giusta per il sito statico, perché controlla esplicitamente la destinazione.

---

## 15. Regole pratiche per non rompere il sistema

### Non fare

- non affidarti al sistema automatico `/tags/...` di Quartz se hai scelto il sistema custom `Topics/...`;
- non lasciare pagine vecchie concorrenti pubblicate;
- non usare `rsync --delete` senza proteggere sia `.git` sia `.git/`;
- non fare commit di pubblicazione dalla repo principale sul branch sbagliato;
- non considerare `public/` come sorgente da modificare a mano.

### Fare

- usa gli script Python per generare le pagine derivate;
- usa Quartz per buildare il sito statico;
- usa il worktree `gh-pages` solo come destinazione di pubblicazione;
- usa link espliciti nei markdown pubblici verso `Topics/...`;
- usa la tassonomia in `tag-index-source-nonpub.md` come base controllata.

---

## 16. Checklist sintetica di pubblicazione

### Prima della build

- contenuti aggiornati;
- tassonomia aggiornata;
- script Python aggiornati;
- nessuna pagina concorrente del vecchio sistema ancora pubblicata.

### Dopo la build

- `quartz-site/quartz-4/public/` esiste;
- il worktree `../SeminariLabLiLec-pages` esiste e ha `.git`;
- il worktree è sul branch `gh-pages`.

### Pubblicazione

```bash
./publish-gh-pages.sh
```

### Verifica finale

- push eseguito;
- sito online aggiornato;
- link principali funzionanti;
- niente 404 sui topics;
- niente ritorno accidentale a `/tags/...`.

---

## 17. Formula architetturale finale

La formula corretta del progetto è questa:

- **Obsidian** serve a scrivere, organizzare e taggare i contenuti;
- **`tag-index-source-nonpub.md`** serve come tassonomia controllata;
- **gli script Python** trasformano la tassonomia e i contenuti in pagine markdown coerenti;
- **Quartz** builda il sito statico;
- **lo script `.sh`** pubblica il contenuto statico sul branch `gh-pages`.

Quando questi livelli sono distinti, il sistema è leggibile e robusto.

Quando si sovrappongono, iniziano i problemi invisibili: branch sbagliati, routing sbagliato, pagine duplicate, tag automatici che interferiscono, e cancellazioni indesiderate nel worktree.

---

## 18. Nota finale

Il punto strategico non è “pubblicare un sito”. Quello è banale.

Il punto strategico è **mantenere separati**:

- sorgenti;
- tassonomia;
- pagine generate;
- build statica;
- worktree di pubblicazione.

Se questa disciplina viene rispettata, la pipeline resta comprensibile anche mesi dopo. Se invece questi livelli si mescolano, ogni modifica futura costerà più del dovuto.

