---
"main-wrapper": "main-wrapper"
---
Vai ai contenuti principali [Guida per l'accessibilità](https://support.google.com/websearch/answer/181196?hl=it)

Feedback accessibilità

## Risultati di ricerca

su un sito github è possibile mettere un contatore?

Sì, è assolutamente possibile inserire un contatore di visite su un sito ospitato tramite

**GitHub Pages** o direttamente nel **README** del tuo profilo o di una repository.

Poiché GitHub Pages supporta solo siti statici (non puoi usare database o linguaggi lato server come PHP direttamente sul loro server), devi affidarti a servizi esterni o strumenti pronti all'uso.

Come aggiungere un contatore

Ecco le soluzioni più comuni:

- **Badge dinamici (per README o siti semplici):**  
	Puoi usare servizi gratuiti come HITS o Mojo-Counter. Generano un piccolo badge in formato SVG che si aggiorna ogni volta che la pagina viene caricata.
	- *Esempio di inserimento in Markdown:*  
		`![Visite](https://hits.seeyoufarm.com)`
- **GitHub Profile Views Counter:**  
	Se vuoi monitorare le visualizzazioni del tuo profilo o di una specifica repository, esistono progetti open-source dedicati che forniscono un'immagine dinamica da incollare nel file `README.md`.
- **Servizi di Analisi (per siti web completi):**  
	Per statistiche più dettagliate (provenienza, tempo di permanenza), puoi integrare Google Analytics o alternative più leggere come **Umami** o **Plausible**. Basta inserire lo script fornito dal servizio nell' `<head>` del tuo file HTML.

Perché non puoi farlo "da solo" su GitHub?

GitHub Pages non ha un **backend** accessibile. Se scrivessi un contatore in JavaScript puro, il numero tornerebbe a zero (o non verrebbe salvato) ad ogni refresh perché non avresti un database dove memorizzare il conteggio. L'uso di un'API esterna risolve questo problema salvando il dato sui loro server.

Vuoi monitorare le visite di un **sito web** specifico o del tuo **profilo GitHub** personale?

- Chat IRC e contatore di visite per Pagine GitHub. - Reddit
	11 mar 2025 — Le pagine GitHub forniscono un sito statico. Non c'è un backend. Non puoi realmente memorizzare le visite o ospitare il tuo server...
	Reddit
- contatore di visualizzazioni del profilo GitHub open-source
	10 mar 2026 — Le porte 80 e 443 sono esposte direttamente alla rete, il che è un trade-off consapevole per mantenere il deployment il più minima...
	Reddit

Mostra tutto

quindi? qual'è la scelta migliore?

**Ricerca in corso…**

La scelta migliore dipende esclusivamente dal tuo obiettivo e da quanto "controllo" vuoi sui dati. Ecco un confronto rapido per aiutarti a decidere:

1\. La scelta più semplice: **Badge Dinamici**

Ideale se vuoi solo mostrare un numero pubblico (nel `README` o nel sito) senza configurazioni complesse.

- **Strumento consigliato:**Visitor Badge o hits.donaldzou.dev (un'ottima alternativa nata dopo la chiusura di servizi storici).
- **Pro:** Si inserisce con una sola riga di codice Markdown o HTML; è gratis.
- **Contro:** Offre solo il numero totale di visite, nessuna statistica su provenienza o dispositivi.

2\. La scelta per il tuo Profilo: **GitHub Profile Views Counter**

Se il tuo obiettivo è monitorare quante persone guardano il tuo profilo GitHub personale.

- **Strumento consigliato:**[antonkomarev/github-profile-views-counter](https://github.com/antonkomarev/github-profile-views-counter).
- **Pro:** Grafica pulita, si integra perfettamente con l'estetica di GitHub.
- **Contro:** Funziona bene solo all'interno dell'ecosistema GitHub.

Se hai un sito vero e proprio su GitHub Pages e vuoi capire da dove arrivano i visitatori senza usare il pesante Google Analytics.

- **Strumento consigliato:****Umami** o **GoatCounter**.
- **Pro:** Rispettano la privacy (niente cookie invasivi), sono leggeri e offrono dashboard bellissime.
- **Contro:** Richiedono la creazione di un account sul loro servizio e l'inserimento di uno script `<script>` nel codice del sito.

4\. La scelta "Power User": **GitHub Actions Counter**

Per chi vuole il controllo totale senza dipendere da servizi esterni che potrebbero chiudere.

- **Strumento consigliato:**[gayanvoice/my-profile-views-counter](https://github.com/gayanvoice/my-profile-views-counter).
- **Come funziona:** Usa le **GitHub Actions** per recuperare i dati dalle API di GitHub e salvarli automaticamente in una repository separata ogni poche ore.
- **Pro:** I dati sono tuoi al 100% e non li perderai mai.

**In sintesi:**

- Vuoi solo un numerino? Usa un **Badge**.
- Vuoi dati seri per un sito web? Usa **Umami**.
- Vuoi monitorare il tuo curriculum/profilo? Usa il **Profile Counter** di Komarev.

Quale di questi scenari si avvicina di più a quello che vuoi fare? Ti serve aiuto con il **codice da copiare**?

Ignora

Altri input

Microfono

Interrompi

Invia

App Google

Account Google

Car Car

gaetk3.org@gmail.com