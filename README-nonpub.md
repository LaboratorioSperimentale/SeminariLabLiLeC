# Seminari site — bootstrap

# PIPELINE DEL SISTEMA

## **note Obsidian → script Python → content/ + TTP-nonpub/ → Quartz → sito statico locale**


## Passi minimi

1. Replicare il vault originale e aprirlo come vault obsidian
2. Verificare che i core plugin che servono siano attivi.
3. Se vuoi generare le pagine statiche dei tag, esegui (serve pyyaml):

```bash
python3 scripts/generate_tag_sections.py
```

## Plugin Obsidian consigliati

### Core plugin

- Templates
- Search
- Outline
- Backlinks
- Properties view
- Tags view
- Graph view
- File explorer

### Community plugin

Nessuno obbligatorio per il prototipo.

## Dipendenza Python

Serve `PyYAML`:

```bash
python3 -m pip install pyyaml
```

## Nota importante

Puoi aprire il vault in Obsidian anche senza installare nulla prima.
I plugin servono per comodità editoriale, non per far funzionare la struttura dei file.



# GUIDA-TUTORIAL SINTETICA: DA VAULT OBSIDIAN A SITO STATICO LOCALE CON QUARTZ

**OK. QUINDI, RIFAMMI UN MANUALE CHE INCLUDA CON CHIAREZZA LA CREAZIONE DELLA PREPARAZIONE (STEP) DEL REPOSITORY (AGGIUNGI QUI PAGES) POI IL RESTO RELATIVAMENTE AL DEPLOYEMENT... METTI ANCHE UN PO' DI SPIEGAZIONE PER IMPARARE.**

# Manuale sintetico: da vault Obsidian a deploy su GitHub Pages con Quartz

## 1. Architettura del sistema

Il tuo setup ha quattro livelli distinti:

* **Obsidian**: scrittura e organizzazione delle note
* **Python + venv**: generazione automatica di `index.md`, `tag-index.md`, `Topics/`, `TTP-nonpub/`
* **Quartz**: trasformazione di `content/` in sito statico HTML/CSS/JS
* **GitHub Pages**: pubblicazione web del sito già buildato da Quartz ([quartz.jzhao.xyz][1])

Formula mentale corretta:

**note Obsidian → script Python → `content/` → Quartz → `public/` → GitHub Pages**

---

## 2. Struttura del vault

Struttura di riferimento:

```text
vault/
├── content/
│   ├── index.md
│   ├── tag-index.md
│   ├── Lista-Seminari/
│   └── Topics/
├── TTP-nonpub/
├── scripts-nonpub/
│   └── generate_tag_sections.py
├── templates-nonpub/
│   └── T-Seminario.md
├── tag-definitions-nonpub.yml
├── README-nonpub.md
├── quartz-site/
│   └── quartz-4/
└── .venv/   # oppure scripts-nonpub/.venv se preferisci lì
```

### Ruolo delle cartelle

`content/` contiene ciò che Quartz deve pubblicare. `content/index.md` è la home del sito. Quartz si aspetta esplicitamente la home in `content/index.md` e builda il sito a partire da `content/`. ([quartz.jzhao.xyz][1])

`TTP-nonpub/` contiene repliche statiche per combinazione di tag, ma non è parte del sito pubblico se Quartz legge solo `content/`.

`quartz-site/quartz-4/` contiene il progetto Quartz: file di configurazione, dipendenze Node, output `public/`. Quartz genera un bundle statico di HTML, JS e CSS. ([quartz.jzhao.xyz][1])

---

## 3. Preparazione del contenuto

I seminari sorgente stanno in:

```text
content/Lista-Seminari/
```

Ogni nota deve avere frontmatter YAML coerente, per esempio:

```yaml
---
title: "UD per Corpora L2"
description: "Seminario sui corpora per la didattica L2."
tags:
  - uno
  - due
status: "draft"
---
```

I tag sono definiti in:

```text
tag-definitions-nonpub.yml
```

con struttura tipo:

```yaml
tags:
  uno:
    title: "uno"
    description: "Materiali introduttivi del primo asse tematico."
  due:
    title: "due"
    description: "Materiali del secondo asse tematico."
  tre:
    title: "tre"
    description: "Materiali del terzo asse tematico."
```

---

## 4. Ambiente Python: cosa serve davvero

Lo script:

```text
scripts-nonpub/generate_tag_sections.py
```

usa `PyYAML`, quindi ha bisogno di un ambiente Python coerente.

### Creazione del venv

```bash
python3 -m venv scripts-nonpub/.venv
source scripts-nonpub/.venv/bin/activate
python -m pip install pyyaml
```

### Controlli minimi

```bash
which python
python -m pip -V
python -c "import sys; print(sys.executable)"
python -m pip show pyyaml
```

### Cosa significa

`which python` ti dice quale binario risolve la shell.
`python -m pip -V` ti dice dove installerai i pacchetti per quel Python.
`sys.executable` ti dice quale interprete sta davvero eseguendo il codice.

Questa è la triade minima per non perdere il controllo.

---

## 5. Generazione del contenuto con Python

Dopo aver attivato il venv:

```bash
source scripts-nonpub/.venv/bin/activate
python scripts-nonpub/generate_tag_sections.py
```

Lo script genera:

* `content/index.md`
* `content/tag-index.md`
* `content/Topics/`
* `TTP-nonpub/`

`Topics/` contiene una sola pagina per combinazione.
`tag-index.md` contiene i gruppi topic per tag, con eventuali ripetizioni logiche dei link tra gruppi.

---

## 6. Quartz: ruolo e dipendenze

Quartz non usa Python. Usa **Node + npm + npx**. La documentazione Quartz 4 richiede **Node >= 22** e **npm >= 10.9.2**. ([quartz.jzhao.xyz][1])

### Cartella Quartz

```text
quartz-site/quartz-4/
```

### Cosa contiene

* `package.json`
* `quartz.config.ts`
* `node_modules/` dopo `npm install`
* `public/` dopo la build

### Cosa produce

Quartz builda il sito statico in `public/`. ([quartz.jzhao.xyz][1])

---

## 7. Preparazione di Quartz in locale

Dentro `quartz-site/quartz-4/`:

```bash
npm install
```

Se vuoi controllare l’ambiente Node:

```bash
which node
which npm
which npx
node -v
npm -v
```

Se usi `nvm`, devi essere certo di aver selezionato Node 22 nella shell in cui lavori.

---

## 8. Collegare il contenuto reale a Quartz

Quartz legge solo il suo `content/` locale. Quindi dentro `quartz-site/quartz-4/` devi collegare o copiare il `content/` reale del vault. ([quartz.jzhao.xyz][1])

### Soluzione con symlink

```bash
cd quartz-site/quartz-4
rm -rf content
ln -s ../../content content
```

### Soluzione con copia

```bash
cd quartz-site/quartz-4
rm -rf content
cp -r ../../content content
```

---

## 9. Build e preview locale

### Build

```bash
cd quartz-site/quartz-4
npx quartz build
```

### Preview locale

```bash
npx quartz build --serve
```

Quartz genera il sito in `public/` e avvia un server locale per la preview. La guida ufficiale Quartz usa `npx quartz build` come build command e `public` come output directory. ([quartz.jzhao.xyz][1])

### Cosa controllare

* `index.md` come home
* `tag-index.md`
* link a `Topics/`
* pagine seminario
* link con `+` nei nomi, se li hai mantenuti

---

# Parte 2: Preparazione della repository GitHub

## 10. Creazione della repository

Dal web GitHub:

* `+` → `New repository`
* scegli owner
* dai un nome alla repo
* scegli visibilità
* crea la repo

GitHub documenta questo flusso standard di creazione repository. ([GitHub Docs][2])

### Consiglio pratico

Se stai caricando un progetto già esistente, è meglio **non** inizializzare la repo con README, `.gitignore` o licenza, per evitare conflitti inutili. Questa è una pratica consigliata anche nella documentazione GitHub sui file in repository. ([GitHub Docs][2])

---

## 11. Preparazione immediata di GitHub Pages

Dopo la creazione della repo, puoi già fare questo:

* vai in `Settings`
* vai in `Pages`
* sotto `Build and deployment`
* scegli `Source = GitHub Actions`

Questo si può fare anche prima di caricare tutto il resto. Da solo non pubblica ancora nulla, ma prepara correttamente la repo al deploy via workflow. GitHub lo documenta esplicitamente. ([GitHub Docs][3])

### Cosa significa

GitHub Pages non prenderà contenuti da un branch statico.
Aspetterà una **workflow GitHub Actions** che builda e pubblica il sito.

---

## 12. Cosa caricare nella repo

Hai due possibilità.

### Opzione A: repo pulita di publishing

Carichi solo ciò che serve alla pubblicazione:

* `content/`
* `quartz-site/quartz-4/`
* eventuali file minimi di supporto

### Opzione B: repo più ampia

Carichi anche il resto del vault.

Se la repo è pubblica, la prima è molto più disciplinata: meno rischio di esporre contenuti `-nonpub`. Quartz stesso avverte che escludere file dal sito non significa automaticamente escluderli dal repository pubblico. ([quartz.jzhao.xyz][1])

---

# Parte 3: Preparazione al deploy

## 13. Configurare `baseUrl` in Quartz

In `quartz.config.ts`, devi impostare correttamente `baseUrl`. Quartz avverte che questa configurazione è necessaria, soprattutto per RSS e sitemap, ma in generale è importante per il deploy corretto. ([quartz.jzhao.xyz][1])

### Esempio

Se la tua repo è:

```text
https://github.com/tuo-utente/seminari-site
```

e pubblichi su GitHub Pages come project site, il `baseUrl` tipico sarà qualcosa come:

```ts
baseUrl: "tuo-utente.github.io/seminari-site"
```

Se invece usi un user site cambia.

### Punto da capire

`baseUrl` non è un path locale.
È l’URL pubblico finale con cui il sito verrà servito.

---

## 14. Aggiungere la workflow di deploy

Dentro la repo crea:

```text
.github/workflows/deploy.yml
```

Quartz documenta esplicitamente la strada GitHub Pages via GitHub Actions con una workflow che:

* fa checkout
* imposta Node 22
* esegue `npm ci`
* builda con `npx quartz build`
* carica `public`
* deploya su Pages. ([quartz.jzhao.xyz][1])

### Schema logico della workflow

1. checkout del repository
2. setup di Node 22
3. installazione dipendenze Quartz
4. preparazione del `content/`
5. build
6. upload artifact
7. deploy su GitHub Pages

Questa è la pipeline corretta.

---

## 15. Attivare davvero il deploy

Una volta che:

* hai caricato i file del progetto nella repo
* hai aggiunto `deploy.yml`
* hai già impostato `Pages → Source = GitHub Actions`

ti basta fare push sul branch scelto dalla workflow, di solito `main`.

GitHub Actions partirà automaticamente e GitHub Pages pubblicherà l’output del sito. GitHub Pages con `Source = GitHub Actions` funziona proprio così. ([GitHub Docs][3])

---

# Parte 4: Procedura operativa completa

## 16. Sequenza completa da ricordare

### A. Aggiorna il contenuto

```bash
source scripts-nonpub/.venv/bin/activate
python scripts-nonpub/generate_tag_sections.py
```

### B. Verifica localmente Quartz

```bash
cd quartz-site/quartz-4
npx quartz build
npx quartz build --serve
```

### C. Prepara il repository GitHub

* crea la repo
* `Settings → Pages → Source = GitHub Actions`

### D. Carica il progetto nella repo

* via browser oppure via Git locale
* assicurati che `content/` e Quartz siano coerenti

### E. Configura `baseUrl`

* modifica `quartz.config.ts`

### F. Aggiungi `deploy.yml`

* in `.github/workflows/`

### G. Fai push

* la workflow partirà
* GitHub Pages pubblicherà il sito

---

# Parte 5: Cosa stai imparando davvero

## 17. La lezione architetturale corretta

In questo progetto non hai “un solo ambiente”.

Hai almeno:

* **ambiente Python** per generare i contenuti
* **ambiente Node** per buildare con Quartz
* **repository GitHub** per ospitare codice e workflow
* **GitHub Pages** come destinazione del sito

Il deploy non è “caricare una cartella sul web”.
È una catena:

**contenuto → build → artifact → pubblicazione**

## 18. Formula finale

**Obsidian scrive.
Python struttura.
Quartz builda.
GitHub Actions automatizza.
GitHub Pages pubblica.**

Questa è la forma corretta di pensare l’intero processo.

[1]: https://quartz.jzhao.xyz/hosting "Hosting"
[2]: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository "Adding a file to a repository - GitHub Docs"
[3]: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site "Configuring a publishing source for your GitHub Pages site - GitHub Docs"
