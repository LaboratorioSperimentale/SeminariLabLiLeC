---
id-asset: '11'
title: tigr
description: Seminario fake su lessico e ripetizione.
videoLink:
- https://www.youtube.com/watch?v=OHgy75FqOZk
videoThumbnail: https://www.wpbeginner.com/wp-content/uploads/2013/07/get-the-post-thumbnail-url-in-wordpress-og.png
videoLabel: Watch video
tags:
- tre
- uno
- '#ob/animali'
layout:
- seminar
- altro
seminar-date: 21.06.2024
seminar-title: '...'
seminar-description: '...'
seminar-author-codekey:
- codauthor1
- codauthor2
seminar-author-affiliation: '...'
seminar-author-affiliation-unibo:
- 'no'
- 'yes'
seminar-video-title: '...'
seminar-video-link: video-link
seminar-video-thumbnail-link: video-link
seminar-video-length: 2h
tutorial-agent-type:
- human
- machine
tutorial-extended-title: '...'
tutorial-short-title: catma
tutorial-author-codkey: codkey
tutorial-video-agent-type:
- human
- machine
tutorial-video-extended-title: '...'
tutorial-video-short-title: '...'
tutorial-video-author-codkey: codkey
translation:
- language
- link
status:
- draft
- finished
resources:
- type: video
  title: Interview video
  url: https://example.com/video
  thumbnail: /img/thumb1.jpg
- type: pdf
  title: Slides
  url: /docs/slides.pdf
- type: image
  title: Poster
  url: /img/poster.jpg
replicated_from: Lista-Seminari/tigr - It.md
topic_section: questo è il titolo+tre
tag_combo:
- ob/animali
- tre
---

> Copia generata automaticamente per il topic **questo è il titolo+tre**.
> Sorgente: `/Lista-Seminari/tigr - It.md`

%%layout: seminar
title: "Il corpus TIGR: un corpus video per lo studio dell'italiano parlato"
seminar_title: "The TIGR corpus: collection, transcription, processing and management of videorecorded data for the study of Italian talk-in-interaction"
date: "06.11.2024"
author: silviamantovani
speaker: johannamiecznikowski, elenabattaglia
video_title: "Universal Dependencies come Standard per Corpora di L2"
video: "https://liveunibo-my.sharepoint.com/personal/ludovica_pannitto_unibo_it/_layouts/15/stream.aspx?id=%2Fpersonal%2Fludovica%5Fpannitto%5Funibo%5Fit%2FDocuments%2FSEMINARI%20LAB%2FVideo%2FThe%20TIGR%20corpus%20%2D%20collection%2C%20transcription%2C%20processing%20and%20management%20of%20videorecorded%20data%20for%20the%20study%20of%20Italian%20talk%20in%20interaction%20%281%29%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ea314ab83%2D2921%2D41f1%2D8bcd%2Dc0355dbc2760"
materials:
  - materials/tigr/slides.pdf
length: 2h
unibo: yes
---

* Table of Contents
{:toc}
{:.no_toc}%%

## Introduzione al corpus TIGR

Il corpus d'italiano parlato TIGR è stato raccolto negli anni 2021 e 2022  nei cantoni svizzeri Ticino e Grigioni (da qui il nome) e nasce all'interno di un progetto di ricerca condotto dall'Università della Svizzera Italiana (USI), **InfinIta - La categorizzazione delle fonti di informazione nell'interazione faccia a faccia. Una indagine basata sul corpus di italiano parlato TIGR** (per l'abstract e le pubblicazioni scientifiche: <https://data.snf.ch/grants/grant/192771>). Il progetto è stato finanziato dalla Swiss National Science Foundation (SNSF) e terminerà il 31 agosto 2025.

"l TIGR documenta interazioni faccia a faccia in situazioni non sperimentali di vario genere: conversazioni a tavola, preparazione di cibo, lezioni e incontri di tutoring, interviste, per 23,5 ore in totale. Queste interazioni sono documentate attraverso non solo registrazioni audio, trascrizioni e dati sociolinguistici, ma anche **registrazioni video**" ([link](https://sharetigr.usi.ch/it/st/corpus))

Per condividere il corpus con la comunità scientifica secondo i principi FAIR è nato [**ShareTIGR**](https://sharetigr.usi.ch/it/st/corpus), un progetto specificamente dedicato agli _open research data_ (ORD). In ShareTIGR, verranno elaborati ulteriormente i dati, eliminando certe informazioni personali, preparando file audio-video maneggevoli, convertendo e formattando le trascrizioni, redigendo descrizioni a vari livelli e preparando metadati leggibili dai motori di ricerca. Infine, tutti i file verranno depositati su [SWISSUbase](https://www.swissubase.ch/en/), un repositorio scientifico svizzero per le scienze sociali e la linguistica. Gli utenti interessati potranno così scaricare i documenti e usarli ai fini delle proprie ricerche, dopo essersi registrati e aver firmato un accordo che precisa le modalità e gli scopi del riuso.
Dopo il deposito su repositorio, un ulteriore scenario di condivisione sarà quello di inserire i documenti su una piattaforma che permetta la loro consultazione e analisi online.

In parallelo al lavoro sui dati, l'esperienza di raccolta del corpus la è stata condivisa tramite il [blog](https://sharetigr.usi.ch/it/notizie-eventi/blog), a più voci e in due lingue (italiano e inglese).

Per le pubblicazioni basate sui dati del TIGR si veda:
[Pubblicazioni e presentazioni nelle quali sono stati usati i dati TIGR](https://sharetigr.usi.ch/it/st/publications)

## Il progetto InfinIta: perché è stato creato il corpus TIGR?

### Le domande di ricerca

Il corpus TIGR è nato per cercare di rispondere a tre domande che riguardano la categorizzazione delle fonti di informazione nell'italiano parlato:

1. A livello semiotico, attraverso quali risorse (indicatori e costruzioni di evidenzialità, strategie discorsive, strategie multimodali, implicature) viene comunicata la fonte dell'informazione?

2. A livello semantico, quali distinzioni relative alla fonte dell'informazione diventano rilevanti? Categorizzazioni specifiche, ad esempio: 'Il presidente non è in forma. _Lo ha detto il suo portavoce durante la conferenza stampa di ieri_' / '_È evidente dal modo in cui si è comportato durante il dibattito televisivo di ieri_' rispetto a categorizzazioni generiche, ad esempio: '_Ho sentito dire che_/ _A quanto pare_ il presidente non è in forma'

3. A livello pragmatico, come la categorizzazione delle fonti di informazione contribuisce al posizionamento epistemico?

### Perché un  _corpus video_ dell'italiano parlato?

Sono diversi i motivi che hanno spinto alla creazione di un corpus video:

1. Il video consente lo studio dell'uso integrato di mezzi verbali, mezzi multimodali e risorse situazionali (oggetti a disposizione in una situazione che diventano funzionali alla comunicazione). Nello specifico, la disponibilità di dati videoregistrati permette di:

   * Individuare le **fonti in situ**, cioè le fonti delle informazioni aquisite durante l'interazione in corso grazie alla percezione diretta e alle inferenze basate su indizi percettivi: _'Hanno suonato alla porta, sarà il postino'_, _'Questo ragno si muove... sarà ancora vivo'_ sono esempi costruiti ad hoc sull'evidenzialità basati su indizi percettivi. Spesso nella letteratura sull'evidenzialità gli esempi sono costruiti a tavolino. Quando però abbiamo dei dati video a disposizione possiamo capire **in modo empirico** quali stimoli eventualmente presenti nella situazione diventano funzionali all'espressione della fonte.
   * Identificare il ruolo della direzione dello sguardo e di certi gesti nel posizionamento epistemico.
   * Comprendere la costruzione del riferimento deittico. Ad esempio, _qui_, _qua_, etc., interpretabili meglio quando sono presenti delle immagini a cui poter fare riferimento.

2. La presenza di un riferimento video consente una prospettiva più ricca e dinamica su come la grammatica funzioni e si sviluppi nel contesto di interazioni reali e multi-modali. Infatti, la grammatica (come la sintassi o i segnali discorsivi) da un lato è uno strumento che organizza l'interazione, ma dall'altro può essere influenzata o "emergere" dalle strutture sequenziali delle interazioni, cioè da come si sviluppano e si susseguono gli scambi comunicativi nel tempo. Dato che le interazioni non sono mediate solo dalle parole, ma anche dai gesti, i movimenti o le espressioni facciali, _i video permettono di osservare come si sviluppano le interazioni nel loro contesto sequenziale completo_. Inoltre, consentono di analizzare la **multi-attività**, cioè situazioni in cui il discorso si intreccia con altre attività parallele (ad esempio, una persona che parla mentre cucina o che gesticola durante la conversazione).

3. La variazione diafasica viene meglio studiata grazie al video. È infatti possibile studiare quelle interazioni che generalmente non vengono prese in considerazione se si dispone solamente dell'audio in quanto con la sola documentazione audio si perdono troppe informazioni. Un esempio potrebbe essere l'analisi dell'interazione durante una lezione di guida, inutile se l'interazione è documentata solo tramite registrazione audio.

### Composizione del corpus

Per conoscere la struttura del TIGR nel contesto del progetto InfinIta e lo statuto del corpus tra i vari corpora linguistici esistenti, si rimanda all'articolo:

{%
  include citation.html
  lookup="Composizione del TIGR"
%}

{% include pdf_card.html
    title="Design iniziale del corpus TIGR (2020)"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="12"
    thumb_url="images/seminar-images/tigr/thumbs/slide12.png"
%}

Secondo il disegno iniziale, l'idea era di includere diversi tipi di interazione: intervista, conversazione a tavola, preparazione di un pasto, lavori di gruppo e lezioni; per un totale di 28 ore e 39 eventi.

Ci sono poi stati dei riadattamenti del design del corpus a causa dell'avvento della Pandemia di COVID-19. Per saperne di più sulle problematiche nella raccolta dei dati legate alla Pandemia, si rimanda al seguente articolo:

{%
  include citation.html
  lookup="Raccogliere dati linguistici ai tempi del COVID-19"
%}

Alla fine del processo sono state ottenute 23h 30' di videoregistrazione, per un totale di 23 eventi e 115 parlanti.

{% include pdf_card.html
    title="La versione finale del corpus TIGR"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="14"
    thumb_url="images/seminar-images/tigr/thumbs/slide14.png"
%}

Per quanto riguarda i contesti didattici, sono state registrate lezioni di tre tipi:

* sessioni di tutoring in architettura
* lezioni di teatro, di musica e di restauro
* lezioni di glottodidattica e di cultura generale nella scuola superiore in cui gli studenti si cimentavano in lavori di gruppo e presentazioni.

COLLEGAMENTO IPERTESTUALE AGLI ESEMPI

Ai parametri del design iniziale sono stati aggiunti l'**istituzionalità** e il **ruolo dei partecipanti**. Esistono tipi di interazione istituzionali, come l'intervista o una lezione, e tipi di interazione non istituzionali, come la preparazione di un pasto o la conversazione a tavola. Il parametro dell'istituzionalità influisce sul ruolo dei partecipanti, che può essere simmetrico, asimmetrico o variabile. Prendendo in considerazione quest'ultimo parametro, è possibile studiare la dimensione epistemica in relazione al ruolo dei partecipanti, e quindi capire, ad esempio, se un rapporto di asimmetria gerarchica determina anche un'asimmetria epistemica.
Il movimento dei partecipanti e la manipolazione degli oggetti hanno a che fare con la multi-attività, la quale ha un effetto sull'organizzazione sequenziale del discorso.

## Parlanti del TIGR

### Reclutamento dei parlanti

Il contatto e il reclutamento dei partecipanti sono descritti in dettaglio nel seguente articolo[^1]:

{%
  include citation.html
  lookup="Il lavoro sul campo: ricerca e contatto dei partecipanti"
%}

[^1]: Nel testo dell'articolo è presente anche il link al questionario che è stato sottoposto ai parlanti.

Il requisito fondamentale che i parlanti dovevano possedere per essere scelti come partecipanti era di essere **italofoni**. Non era necessario che la lingua italiana fosse la lingua madre (L1).

Per un approfondimento sul questionario che i parlanti hanno dovuto compilare:

{%
  include citation.html
  lookup="Digitisation of the TIGR participant questionnaires"
%}

#### Dichiarazioni di consenso informato: esigenze della ricerca, esigenze legali e questioni etiche

Per redigere la dichiarazione di consenso informato è stato utilizzato un modello interno all'USI e sono stati consultati la Commissione etica e il Servizio legale dell'università.
Inoltre, si è fatto riferimento a normative, come la Legge federale sulla protezione dei dati, e linee guida, come quelle indicate da FORS.
Per una riflessione approfondita sulle tematiche legali, si rimanda all'articolo:

{%
  include citation.html
  lookup="Social interaction is among people. Legal, technical, and ethical explorations about personal information and its removal in talk-in-interaction as data"
%}

Prevedere fin dall'inizio la pubblicazione dei dati (video) richiede una riflessione su due tematiche principali:

1. Come gestire la deidentificazione dei parlanti?
2. Come descrivere in modo informativo ma non limitante il futuro riuso dei dati?

Qui di seguito, la struttura del documento di dichiarazione di consenso informato che è stato fatto firmare ai partecipanti.

##### Parte A. Documento informativo

1. Introduzione
2. Descrizione del progetto di ricerca per un pubblico non specialista
3. Descrizione dell'evento e modalità di video-registrazione
4. Confidenzialità e protezione dei dati
5. Conservazione e utilizzo dei dati
6. Diritti dei partecipanti allo studio
7. Contatti

##### Parte B. Consenso informato

Ogni partecipante registrata/o ha espresso il proprio consenso all'uso dei dati dopo essere messa/o a conoscenza degli scopi dell'indagine e delle modalità di diffusione dei dati. In caso il parlante avesse deciso di non essere riconoscibile, le opzioni di deidentificazione tra cui poteva scegliere erano due:

* **default**: pseudonimi nella trascrizione, silenzi nella traccia audio, misure di deidentificazione nei metadati
* **misure supplementari**: alterazione della voce nella traccia audio (6 richieste), applicazione di filtri nella traccia video (15 richieste)

Per saperne di più a proposito della stesura del documento di dichiarazione di consenso informato da parte del team di InfinIta, si legga l'articolo:

{%
  include citation.html
  lookup="Dichiarazioni di consenso informato"
%}

#### Misure di deidentificazione dei dati

Per quanto riguarda le misure di deidentificazione dei partecipanti, sono stati adottati diversi provvedimenti:

* Ad ogni partecipante è stato attrbuito un codice informatore nel formato inf-N.
* L'età è stata ridotta a un intervallo.
* Per quanto riguarda le informazioni sul luogo di provenienza, è stato inserito lo Stato (ad esempio, Svizzera) e il cantone (o la regione nel caso dell'Italia).
* il luogo di registrazione viene descritto solamente dal Cantone e dalle dimensioni del centro abitato (> o <10,000 abitanti).

Inoltre, come è riportato sul sito del corpus alla voce "Deidentificazione":

>in vista della loro condivisione sul repositorio, i documenti video saranno deidentificati in Adobe Premiere tramite l'applicazione di effetti video (p.es. Gaussian blur, Find edges) secondo i desideri espressi dai parlanti nelle loro dichiarazioni di consenso. Nelle tracce audio, si altereranno alcune voci secondo i desideri espressi nelle dichiarazioni di consenso e si sostituirà con rumore certi nomi e indicazioni temporali, nello specifico una serie di nomi di persone, istituzioni e luoghi nonché certe date che potrebbero facilitare l'identificazione delle e dei partecipanti. Questi interventi sono stati preparati in ELAN[^2] tramite l'annotazione dei passi problematici come _name_ in un'apposita traccia. Si userà uno script per leggere i tempi iniziali e finali dei segmenti annotati e istruire il programma Praat a elaborare l'insieme delle tracce audio negli intervalli in questione, cancellando il suono originale e inserendo frammenti di rumore. Nelle trascrizioni, l'informazione personale è stata sostituita da pseudonimi. I nomi dei partecipanti sono stati sostituiti da pseudonimi di simile lunghezza. Al posto di altre informazioni personali sono state inserite le diciture _personname_ / _institutionname_ / _placename_ / _datename_ accompagnate da indici, così da permettere riferimenti multipli alla stessa entità all'interno di una trascrizione.

[^2]: Per approfondire l'utilizzo di ELAN, si veda [qui](/seminari/elantrascrizione.html)

Di seguito sono riportati alcuni esempi:

{% include pdf_card.html
    title="Misure di de-identificazione"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="53"
    thumb_url="images/seminar-images/tigr/thumbs/slide53.png"
%}

{% include pdf_card.html
    title="Misure di de-identificazione"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="54"
    thumb_url="images/seminar-images/tigr/thumbs/slide54.png"
%}

{% include pdf_card.html
    title="Misure di de-identificazione"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="55"
    thumb_url="images/seminar-images/tigr/thumbs/slide55.png"
%}

### Dati sociolinguistici ricavati

Di seguito si riportano alcuni grafici sui principali dati sociolinguistici che riguardano il campione di parlanti considerato.

#### Genere e età

Come si può vedere dal grafico a sinistra,  il corpus è abbastanza bilanciato con una presenza femminile (53%) di poco superiore a quella maschile (47%). Nel grafico a destra vengono mostrate le fascie d'età, con una sovrarappresentazione della fascia degli studenti universitari (20-29).

{% include pdf_card.html
    title="Dati sociolinguistici: genere e età"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="31"
    thumb_url="images/seminar-images/tigr/thumbs/slide31.png"
%}

#### Origine dei parlanti

Qui vengono mostrati i dati specifici sulle regioni italiane e sui cantoni svizzeri in cui i parlanti hanno frequentato la scuola elementare. Nonostante un certo bias geografico per quanto riguarda l'Italia, con Lombardia e Piemonte in testa, diverse regioni sono rappresentate, sia del centro sia del sud.
In merito alla Svizzera, la maggior parte dei parlanti ha frequentato la scuola elementare nei cantoni Ticino e Grigioni.

{% include pdf_card.html
    title="Dati sociolinguistici: origine dei parlanti"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="32"
    thumb_url="images/seminar-images/tigr/thumbs/slide32.png"
%}

{% include pdf_card.html
    title="Dati sociolinguistici: origine dei parlanti"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="33"
    thumb_url="images/seminar-images/tigr/thumbs/slide33.png"
%}

#### Luogo di lavoro o studio in Svizzera

La maggior parte dei parlanti svolge la sua attività principale (studio o lavoro) in Ticino (64%). Al secondo posto troviamo i Grigioni (34%).

{% include pdf_card.html
    title="Dati sociolinguistici: luogo di lavoro o studio"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="34"
    thumb_url="images/seminar-images/tigr/thumbs/slide34.png"
%}

#### Repertorio linguistico

La maggior parte dei parlanti ha dichiarato di essere plurilingue (due, tre o addirittura più di quattro lingue nel proprio repertorio). La lista delle lingue conosciute dai partecipanti sono riportate nel grafico di destra.

{% include pdf_card.html
    title="Repertorio linguistico dei partecipanti"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="35"
    thumb_url="images/seminar-images/tigr/thumbs/slide35.png"
%}

#### Istruzione e professione

Il livello di istruzione principale è la scuola secondaria di secondo grado. Trattandosi per la maggio parte di studenti universitari, era l'ultimo grado di istruzione completato.

{% include pdf_card.html
    title="Livello di istruzione"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="36"
    thumb_url="images/seminar-images/tigr/thumbs/slide36.png"
%}

## Luoghi dove sono stati registrati gli eventi del TIGR

Come è stato detto, la registrazione delle interazioni è avvenuta nei cantoni Ticino e Grigioni. Le località all'interno dei due cantoni sono determinate in modo opportunistico in base alla disponibilità dei parlanti. In una seconda fase della raccolta, la presa di contatto ad hoc con le istituzioni scolastiche ha permesso di ampliare la copertura geografica del corpus.

In Ticino sono stati registrati 9 eventi in 7 piccoli centri e altri 9 eventi in 2 grandi centri, per un totale di 18 eventi in 9 località.
Nei Grigioni sono stati registrati 4 eventi in 1 piccolo centro e altri 4 eventi in 1 grande centro, per un totale di 5 eventi in 2 località.

Si precisa che il corpus non è disegnato per documentare la variazione diatopica dell'italiano parlato in Svizzera.

## Impostazione tecnica delle registrazioni, post-produzione e trascrizione

### Strumentazione utilizzata e post-produzione

La prassi era quella di andare sul luogo della registrazione, installare i dispositivi e lasciare che i parlanti interagissero da soli. Solamente nelle interazioni didattiche e nelle interviste erano presenti anche i ricercatori.
Una volta conclusesi le interazioni, i ricercatori venivano contattati dai partecipanti tramite Whatsapp.

In particolare, come viene illustrato sul sito dell'USI alla voce "Registrazioni audio e video":

>per ogni evento del TIGR sono state fatte due riprese video da angolazioni differenti, usando delle telecamere Sony HXR-NX80//C. Le tracce audio sono da due a sei, secondo il numero di partecipanti all'evento. Sono state registrate con da due a quattro registratori tascabili Tentacle Track E muniti di microfono da bavero e con un microfono esterno Sony EGM-VG1 montato su una delle telecamere. Nel caso specifico dell'interazione in classe, l'équipe ha aggiunto un ulteriore microfono, del tipo Neumann TLM 127 ni-K, collocato in posizione centrale e collegato con l'altra telecamera.
>I vari dispositivi sono stati sincronizzati prima dell'inizio della registrazione per ottenere una corrispondenza più precisa possibile tra immagine e suono. A questo fine sono stati impiegati generatori di timecode della marca Tentacle. Tali generatori sono parte integrante degli audioregistratori Tentacle Track E, che registrano direttamente un timecode numerico. Con le telecamere sono invece stati usati i dispositivi esterni Tentacle Sync, collegati tramite le connessioni per microfoni delle telecamere. Essi generano del timecode acustico che durante le riprese viene registrato nel corrispondente canale audio. Una componente cruciale del sistema Tentacle è un'applicazione mobile che comunica con tutti i dispositivi tramite bluetooth e permette di sincronizzarli da remoto nonché di avviare e interrompere le registrazioni.
>Dopo le riprese, i file video sono stati elaborati dal programma Tentacle Timecode Tool per Windows. Il programma legge il segnale acustico che codifica il timecode, lo converte in informazione numerica e infine lo cancella, mantenendo solo il timecode numerico. In un'ulteriore fase di post-produzione, tutti i file video e audio sono sono stati importati in un progetto Adobe Premiere, dove sono stati allineati sulla base del timecode numerico e sono stati tagliati per ottenere tracce di uguale durata.
>Le impostazioni tecniche di ogni evento e altri aspetti inerenti alla collezione dei dati sono stati descritti in una scheda, talvolta corredata da fotografie. La scheda registra la data e il luogo dell'evento, elenca i dispositivi usati e i codici identificatori anonimi dei partecipanti, riporta eventuali desideri di deidentificazione e contiene appunti su altri aspetti della situazione che l'équipe sul campo giudicava potenzialmente rilevanti per l'interpretazione dei dati. Una funzione importante della scheda è di associare i codici identificatori dei parlanti a una descrizione del loro aspetto e ai nomi dei microfoni da bavero. Essa contiene, infine, appunti su eventuali problemi tecnici riscontrati durante l'elaborazione dei file tramite TTT e in Adobe Premiere.

### La trascrizione

Per la trascrizione è stato utilizzato il software ELAN, v. 6.7.
È stato inoltre adottato il sistema GAT2 (Gesprächsanalytische Transkriptionssystem):

* funzionale a una trascrizione tramite software e machine-readable
* integrato in editor digitali (per esempio EXMARaLDA)
* dotato di tre livelli di granularità: minimal script, basic script e fine script (quello più dettagliato e usato per il corpus TIGR)

Alla guida interna sono stati aggiunti:

* una lista di lemmi per uniformare la grafia delle interiezioni
* la trascrizione del raddoppiamento fonosintattico (ex., _va bbene_, _e nniente_ )
* l'uso del simbolo ~ per le interruzioni udibili di una parola (in particolare, glottal stop), per esempio in esitazioni o ripartenze

Di seguito sono riportate alcune delle convenzioni GAT2 utilizzate nella trascrizione delle registrazioni

{% include pdf_card.html
    title="Convenzioni GAT2"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="49"
    thumb_url="images/seminar-images/tigr/thumbs/slide49.png"
%}

{% include pdf_card.html
    title="Convenzioni GAT2"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="50"
    thumb_url="images/seminar-images/tigr/thumbs/slide50.png"
%}

Da notare l'annotazione del comportamento non verbale (guarda nell'immagine sopra in "Laughter and crying") che funziona con la logica del tag.

Inoltre, sono state adottate convenzioni di trascrizione multimodale di Modada per il tier "ambient noises", come nel seguente esempio:

{% include pdf_card.html
    title="Ambient Noises"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="52"
    thumb_url="images/seminar-images/tigr/thumbs/slide52.png"
%}

#### La segmentazione in Elan

La segmentazione non rappresenta necessariamente un'unità significativa sul piano linguistico.
La segmentazione è stata pensata per essere funzionale ad una trascrizione accurata, come nel caso di sovrapposizioni multiple.
COLLEGAMENTO IPERTESTUALE 1:00:04 a 1:02:14
Il problema di come trascrivere le sovrapposizioni si pone in particolare nel caso degli schismi. Non si tratta solamente di conversazioni parallele, ma a volte c'è anche uno spostamento associato. Facciamo l'esempio delle conversazioni a tavola: quando due persone si alzano e vanno in cucina e altre due rimangono a tavola si hanno due conversazioni parallele. La stessa cosa accade durante le lezioni di restauro quando due gruppi lavorano in due parti diverse della chiesa.

COLLEGAMENTO IPERTESTUALE 1:02:14 a 1:04:03

#### La derivazione di trascrizioni in formato testo in stile "dialogo teatrale"

Come esportare la trascrizione da ELAN e creare un formato leggibile?
Come abbiamo visto, la prima trascrizione avviene su ELAN. Da questa trascrizione possono derivate altri due tipi di trascrizione:

1. una trascrizione in stile "dialogo teatrale" e formato `txt`;
2. una trascrizione in versione tokenizzata, di cui si parlerà nel paragrafo successivo.

  {% include pdf_card.html
    title="Trascrizione in stile 'dialogo teatrale'"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="59"
    thumb_url="images/seminar-images/tigr/thumbs/slide59.png"
  %}

Il primo tipo di trascrizione offre un'approssimazione grafica dell'organizzazione della conversazione in turni e una buona base per un'analisi sequenziale.
Inoltre, costituisce un input per l'annotazione delle fonti di informazione all'interno del progetto InfinIta, eseguita nel programma [INCEpTION](https://inception-project.github.io/).
 Infine, il formato `txt` è semplice e interoperabile.

Come fare per passare da una trascrizione ELAN a una trascrizione di questo tipo?
Si può esportare da ELAN la trascrizione in formato testo "tradizionale", con o senza timecode e con la formattazione automatica dei turni.
Però sono stati riscontrati alcuni problemi, tra cui: se si intende esportare la trascrizione con il timecode, il file risulta illeggibile e la messa in sequenza automatica dei turni non è sempre intuitiva.
La soluzione è stata quella di condurre una **procedura semi-automatica (script Python)**: la trascrizione veniva esportata da ELAN come trascrizione in formato "tradizionale" e con l'allineamento verticale delle parentesi quadre. Attraverso degli script sono stati eliminati i timecode tranne quelli che segnano i tempi iniziali dei segmenti (creati su ELAN), che compaiono all'incirca ogni 10 secondi. Sono, poi, state collocate delle ancore "((TC))" nel testo, come si vede in questo esempio

  {% include pdf_card.html
    title="Ancore"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="61"
    thumb_url="images/seminar-images/tigr/thumbs/slide61.png"
  %}

Sono stati eliminati i nomi di parlanti superflui e sono stati concatenati i segmenti e si è formattato manualmente le trascrizioni quando presentavano sovrapposizioni di più di due parlanti

#### Verso una versione tokenizzata delle trascrizioni

I due tipi di trascrizione, quella originale in ELAN e quella in stile "dialogo teatrale" in formato `txt`, non sono tokenizzate.

Cos'è la tokenizzazione? È la divisione di un testo in "token", cioè unità linguisticamente pertinenti di varia complessità. È indispensabile per l'inserimento in un database e ai fini della ricerca lessicometrica, morfo-sintattica, fonologica, ecc. Fornisce, infine, gli input per le procedure di annotazione automatica (per esempio, l'annotazione delle parti del discorso e la lemmatizzazione)

Per questa procedura di tokenizzazione delle trascrizioni si sta collaborando con l'azienda [_Linguisticbits_](https://linguisticbits.de/) del Dr. Thomas Schmidt.
La procedura comprende i seguenti step, elencati in ordine di precedenza:

1. Ricongiungimento dei frammenti di parola creati ai confini dei segmenti in ELAN, che avverrà in maniera in parte automatica, grazie all'uso di un lessico estratto da ItTenTen, e in parte manuale
2. Concatenazione dei segmenti ELAN in "contributi" (si tratta di un'approssimazione dell'unità "turno")
3. Divisione automatica dei contributi in parole
4. Conversione in un documento XML conforme all'[ISO/TC 37/SC 4, 2016](https://standards.clarin.eu/sis/views/view-format.xq?id=fTEISpoken)[^3]. A proposito degli standard ISO per la trascrizione della lingua parlata si cita l'articolo _The TEI-based ISO Standard ‘Transcription of spoken language’ as an Exchange Format within CLARIN and beyond_:
  {%
    include citation.html
    lookup="The TEI-based ISO Standard ‘Transcription of spoken language’ as an Exchange Format within CLARIN and beyond"
  %}

[^3]: standard ISO per la trascrizione della lingua parlata

Per saperne di più sul processo di trascrizione si rimanda ai seguenti articoli presenti nel blog:

{%
  include citation.html
  lookup="Morfologia delle trascrizioni, parte I: leggibili in che modo?"
%}

{%
  include citation.html
  lookup="Morfologia delle trascrizioni, parte II: codificare il tempo"
%}

{%
  include citation.html
  lookup="Morfologia delle trascrizioni, parte III: il primo script"
%}

{%
  include citation.html
  lookup="Morfologia delle trascrizioni, parte IV: allineamento temporale e segmentazione"
%}

{%
  include citation.html
  lookup="Morfologia delle trascrizioni, parte V: gestire le sovrapposizioni"
%}

{%
  include citation.html
  lookup="Morfologia delle trascrizioni, parte VI: uso di script in fase di impaginazione e di revisione"
%}

## Condivisione dei dati

La condivisione e il riuso dei dati è un ciclo: dei ricercatori producono dati per altri ricercatori che li riusano.
I due momenti di condivisione e riuso sono rappresentati graficamente nelle immagini qui sotto:

  {% include pdf_card.html
    title="Condivisione dei dati"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="65"
    thumb_url="images/seminar-images/tigr/thumbs/slide65.png"
  %}

  {% include pdf_card.html
    title="Riuso dei dati"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="66"
    thumb_url="images/seminar-images/tigr/thumbs/slide66.png"
  %}

Dal punto di vista tecnico le infrastrutture digitali (sono quelle che si vedono nel mezzo) sono cruciali in questo processo.
Nella condivisione e nel riuso dei dati sono contemplati tre mezzi:

1. repositorio
2. piattaforma per la consultazione online
3. l'invio dei dati a qualcuno tramite e-mail,

Un quarto mezzo potrebbe essere rappresentato dalle "data sessions", ovvero incontri faccia a faccia dove si lavora sui dati.

L'invio di dati tramite e-mail non assicura che i dati siano reperibili e accessibili a chi non li conosca già. Quindi si considera questa modalità non aderente ai principi FAIR, come invece sono le prime due, cioè il repositorio e la piattaforma digitale. Infatti, il catalogo e la regolazione degli accessi assicurano la reperibilità e l'accesso ai dati.

### Il repositorio

Nel caso del corpus TIGR verrà usato il **repositorio LaRS**, la sezione linguistica del repositorio [SWISSUbase](https://www.swissubase.ch/en/). Un articolo di approfondimento in inglese per chi fosse interessato:

{%
  include citation.html
  lookup="Exploring LaRS @ SWISSUbase"
%}

Il repositorio LaRS è organizzato secondo tre livelli gerarchici:

1. Studi
2. Dataset (entità scaricabile)
3. Documenti

Ad ogni livello ci sono dei metadati, alcuni obbligatori e altri facoltativi, che l'utente del repositorio deve inserire.

  {% include pdf_card.html
    title="LaRS"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="69"
    thumb_url="images/seminar-images/tigr/thumbs/slide69.png"
  %}

Nell'immagine sopra i dataset che verrano caricati.
Ci sarà un dataset generale di documentazione che contiene la documentazione del corpus intero (documentazione metodologica, consensi informati, ecc.).
Ci saranno poi i dataset dei singoli eventi. Di ogni evento ci sarà una versione leggera e una versione completa (che contiene le singole tracce audio). All'interno di ciascun dataset saranno raccolti dati video, dati audio, le trascrizioni e file di metadati.
L'ultimo dataset sarà un dataset di sole trascrizioni, pensando a coloro che hanno la necessità di fare ricerca sulle trascrizioni e non hanno bisogno di visionare o di ascoltare i file multimediali.

Il repositorio assegna un DOI a ciascun dataset.
Il dataset è l'unità scaricabile.

Per conoscere in dettaglio la costruzione dei vari dataset su LaRS, si legga:

{%
  include citation.html
  lookup="Grouping the TIGR data for reuse"
%}

#### Metadati

Il repositorio mette a disposizione dei campi predefiniti, alcuni obbligatori alcuni facoltativi. Si è pensato di aggiungere anche delle tabelle (in formato CSV) con i metadati per ogni singolo evento.

  {% include pdf_card.html
    title="Documenti con Metadati"
    authors="Johanna Miecznikowski, Elena Battaglia"
    date="06/11/2024"
    pdf_url="/materials/tigr/slides.pdf"
    page="70"
    thumb_url="images/seminar-images/tigr/thumbs/slide70.png"
  %}

Come si vede nell'immagine per ogni singolo evento il cuore è la tabella più centrale con le caratteristiche di base dell'evento (come il numero di partecipanti, il genere di interazione, e così via). La tabella centrale rinvia poi a una serie di altre tabelle. A sinistra si vedono due tabelle con i parlanti e i luoghi del TIGR. I parlanti del TIGR sono collegati al singolo evento tramite l'elenco dei partecipanti all'evento.
L'evento è poi associabile all'elenco dei file video, all'elenco dei file audio e all'elenco delle trascrizioni.

### Verso la messa a disposizione in una piattaforma digitale per la consultazione online

Ovviamente il repositorio è uno scenario di riuso che suppone il download dei dati sul proprio computer. Questo ha i suoi vantaggi, come la grande libertà di quello che si può fare con questi dati, e i suoi svantaggi, come quello di doversi dotare sul proprio computer degli strumenti necessari per leggere i dati scaricati.
La piattaforma online, al contrario, è percepita da molti come più comoda perché non richiede il download di alcun strumento di lettura dei dati.

Nel contesto del [progetto FAIR-FI-LD](https://www.liri.uzh.ch/en/projects/FAIR-FI-LD.html) condotto dall'Università di Zurigo a cui partecipa tra gli altri anche l'USI (in particolare l'Istituto di Studi Italiani, o ISI), si vuole depositare il TIGR nel [LiRI Corpus Platform (o LCP)](https://www.liri.uzh.ch/en/services/LiRI-Corpus-Platform-LCP.html). Questa piattaforma online è stata creata dal LiRI (Linguistic Research Infrastructure), un dipartimento dell'Università di Zurigo. Per saperne di più sul LiRI e di che cosa si occupa, qui è riportata la home page del sito: <https://www.liri.uzh.ch/en.html>.
Grazie alla collaborazione con _Linguisticbits_, di cui si è parlato sopra, si sta cercando di definire una procedura di upload in LCP di trascrizioni XML tokenizzate.
