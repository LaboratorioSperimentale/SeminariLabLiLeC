---
id-asset: '06'
title: elantrascrizione
description: Seminario fake su lessico e ripetizione.
videoLink:
- https://www.youtube.com/watch?v=OHgy75FqOZk
videoThumbnail: https://www.wpbeginner.com/wp-content/uploads/2013/07/get-the-post-thumbnail-url-in-wordpress-og.png
videoLabel: Watch video
tags:
- '#ob/tre'
- '#ob/uno'
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
replicated_from: Lista-Seminari/elantrascrizione-It.md
topic_section: questo è il titolo
tag_combo:
- ob/animali
---

> Copia generata automaticamente per il topic **questo è il titolo**.
> Sorgente: `/Lista-Seminari/elantrascrizione-It.md`

%%layout: seminar
title: La Trascrizione del Parlato con ELAN
author: marcoesposito
speaker: silviaballare
video_title: La Trascrizione del Parlato con ELAN
video: "https://liveunibo-my.sharepoint.com/personal/ludovica_pannitto_unibo_it/_layouts/15/stream.aspx?id=%2Fpersonal%2Fludovica%5Fpannitto%5Funibo%5Fit%2FDocuments%2FSEMINARI%20LAB%2FVideo%2FLa%20Trascrizione%20del%20Parlato%20con%20ELAN%20%28Silvia%20Ballar%C3%A8%29%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E6de32167%2Da3c0%2D4ff0%2D9f13%2D978bc7696a4c"
length: 2h
unibo: yes
materials:
  - materials/trascrizione-parlato/ladyfrankenstein.eaf
  - materials/trascrizione-parlato/ladyfrankenstein.mp4
---

* Table of Contents
{:toc}
{:.no_toc}%%

## Obiettivo del seminario

L’obiettivo del seminario è quello di presentare anzitutto alcune nozioni di base in merito alla trascrizione e al sistema Jefferson (fornendo alcune possibili soluzioni ai problemi più comuni), per poi passare alle funzioni di base del software ELAN. In questo modo verranno forniti tutti gli strumenti per poter trascrivere un file audio in autonomia.

## La trascrizione del parlato

Per trascrizione si intende una forma di **rappresentazione del parlato in forma scritta**. Ciò può essere eseguito mediante diverse convenzioni, che vengono scelte in base agli obiettivi del ricercatore. Pertanto, prima di scegliere un tipo di convenzione piuttosto che un altro, è necessario tenere bene a mente il motivo stesso per cui stiamo trascrivendo. Vediamo quelli che sono gli obiettivi più comuni:

1. Si vuole studiare un fenomeno;
2. Si ha intenzione di documentare a livello più generale il comportamento di una comunità;
3. Si vuole avere una traccia scritta di “che cosa succede” nel mio file audio.

In base ai nostri obiettivi e a come decidiamo di usare il nostro programma, otterremo dei risultati diversi:

1. Un file annotato da consultare su ELAN;
2. Testo da consultare senza riferimento audio;
3. Trascrizione conversazionale;
4. Testo glossato.

Il nostro focus sarà principalmente riguardo la trascrizione conversazionale e il sistema Jefferson.

### Principali differenze fra scritto e parlato

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/image-1.png"
  caption="Confronto fra scritto e parlato"
%}

Naturalmente, prima di iniziare la trascrizione bisogna tenere a mente alcune differenze sostanziali fra le produzioni in forma parlata e in forma scritta. Vediamo le differenze più importanti:

* **Tempo di pianificazione**: Anzitutto, il fatto che il parlato venga organizzato in diretta fa sì che ci sia poco tempo per pianificare (ad esempio, possono esserci false partenze o progetti sintattici non portati a termine). Bisogna quindi capire come rappresentare questo tipo di caratteristiche.
* **Produzione e ricezione**: A differenza dello scritto, nel parlato la produzione e la ricezione sono contemporanee: pertanto, nel caso di compresenza di più parlanti all'interno di una registrazione, diverse produzioni in forma parlata possono sovrapporsi (e bisogna dunque trovare un modo per rappresentare anche questo tipo di situazioni).

### Problemi più comuni nella trascrizione e possibili soluzioni

Vediamo alcuni dei probemi più comuni che emergono quando ci si approccia alla trascrizione:

* **L'individuazione di unità**, ossia il corrispettivo in lingua parlata di ciò che rappresenta la frase nella lingua scritta. Discuteremo di questo punto più approfonditamente in seguito.

* **L'intonazione**: modulando l’intonazione possiamo cambiare il significato della frase stiamo pronunciando (ad esempio, da essa dipende la distinzione fra una frase interrogativa e una frase dichiarativa). Bisogna dunque capire come trasferire queste informazioni nella trascrizione. Lo stesso vale per le pause, le false partenze, le riformulazioni, i cosiddetti filler e così via: vanno rappresentati nella conversazione? Se sì, come? Possono esserci diverse soluzioni a tale problema.

La risposta alle domande che ci siamo posti dipende dal contesto, in quanto bisogna sempre adattare le proprie risposte in base alle proprie esigenze di trascrizione. In base alle intenzioni con cui sto trascrivendo posso effettivamente decidere il sistema di trascrizione più adatto. Ad ogni modo, a prescindere dall'intento, *bisogna cercare di mantenere un equilibrio fra due esigenze diverse*:

* **Fedeltà al parlato**: c'è l'esigenza di trascrivere nella maniera più fedele possibile ogni aspetto del parlato (dunque anche aspetti come pause e sovrapposizioni fra parlanti);
* **Cercabilità nel testo**: se sovraccarichiamo la trascrizione con dei simboli per indicare tutto ciò che avviene nel parlato, c'è il rischio che il testo perda parte della propria cercabilità e leggibilità.

In sostanza, la trascrizione è una pratica di **decision-making**: in base al sistema di convenzioni che si sceglie di adottare, di volta in volta il trascrittore deve cercare di agire in maniera più coerente possibile rispetto al modello scelto e in base agli obiettivi che vogliamo raggiungere.

Riassumendo, idealmente si trascrive quanto più possibile (anche le pause, i vari segnali discorsivi, le false partenze e talvolta anche i gesti del parlante): tuttavia, se per i nostri obiettivi non è necessario avere una trascrizione eccessivamente dettagliata, è meglio non sovraccaricare il testo di informazioni (in modo da non perdere la facilità con cui si può interrogare il testo).

### L’Individuazione di un’unità

Come è stato accennato precedentemente, una delle cose più complicate per quanto riguarda la trascrizione del parlato è l'individuazione dell'unità, cioè l'individuazione della frase. Ciò accade proprio perché il livello sintattico è quello che, rispetto allo scritto, presenta più differenze.

Ai fini della trascrizione non è importante dare una definizione precisa di *frase* nel parlato: la trascrizione è uno strumento che ci serve a rappresentare il parlato, ma in un certo senso è **pre-teorica**, cioè non ci serve per l'analisi. La trascrizione deve essere sempre funzionale all'analisi, che avviene in un secondo momento.
Per trascrivere, vengono spesso utilizzate come unità delle **unità di trascrizione** (che non hanno nessun tipo di rilevanza per l'analisi). L'unità di trascrizione viene individuata in base a un criterio intuitivo, cioè in base a parametri come la curva intonativa e, soprattutto, le pause.

### Il Sistema Jefferson

Il sistema di trascrizione Jefferson è sicuramente il **sistema di trascrizione più diffuso** (anche se non necessariamente il migliore). Il sistema Jefferson permette una rappresentazione piuttosto dettagliata di molti dei fenomeni che occorrono nel parlato, tra cui:

* Sovrapposizioni, pause, interruzioni;
* Allungamenti delle vocali, alterazione del volume, alterazione della velocità del parlato;
* Comportamenti non verbali (come risate o starnuti).

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/image-2.png"
  caption="Simboli più frequenti del Sistema Jefferson"
%}

Notiamo che nella lista è presente un simbolo per rappresentare una pausa breve, ma non una pausa lunga. Quest'ultima è assente nella lista poiché non viene rappresentata mediante un simbolo, ma si inseriscono direttamente due unità diverse (e quindi la pausa viene rappresentata dall'interruzione delle unità).

## Il software ELAN

**ELAN** è un **software gratuito**, la cui funzione principale è quella di permettere la **trascrizione del parlato**. Ad un livello più avanzato si può utilizzare anche per effettuare ricerche all'interno delle trascrizioni (interrogazione del corpus) e per creare annotazioni su più livelli (ad esempio, posso decidere di creare delle glosse). È uno dei software più diffusi per la trascrizione del parlato, per cui online sono reperibili molti strumenti di supporto accessibili gratuitamente (tra cui un [forum](https://archive.mpi.nl/forums/) e diversi manuali, come [questo](https://www.ling.upenn.edu/~wlabov/L560/ELAN_introduction.pdf)).


### Scaricare il programma

Il programma è scaricabile a questo [link](https://archive.mpi.nl/tla/elan/download). Quando si scarica il programma, il sito stesso mette a disposizione molto [materiale in PDF](https://archive.mpi.nl/tla/elan/documentation) che si può utilizzare per prendere confidenza con ELAN o per risolvere moltissimi dei problemi che possono emergere con col programma.

### Scaricare i materiali

In allegato è possibile trovare **un file video** che può essere utilizzato per compiere un esercizio di trascrizione e per familiarizzare con le funzioni base di ELAN. Il video in questione è un estratto di "Lady Frankenstein", un film del 1971 diretto da **Mel Welles**.

### Qualità e Formato dell'Audio

Prima di andare avanti, è utile fare una premessa: la qualità della traccia audio, assieme ad altri fattori (come il numero di persone o il luogo in cui è stata registrata l'interazione), influisce molto sulla difficoltà della trascrizione. Per intervenire sulla qualità della traccia audio (ad esempio per alzare il volume o ridurre il disturbo) si possono usare moltissimi software, come ad esempio **Audacity** (scaricabile a questo [link](https://www.audacityteam.org/download/) gratuitamente).

Un altro aspetto che ha delle conseguenze sulla facilità della trascrizione è il formato della traccia audio.

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/image-3.png"
  caption="File non compresso e file compresso"
%}

Quando si usa un formato **file non compresso**, è possibile visualizzare le onde sonore del parlato. Ciò ci aiuta molto nell’individuazione delle unità, in quanto gli spazi vuoti tra un’unità e l’altra sono resi graficamente dall’assenza di onde sonore. Invece, nel caso di un **file compresso** non abbiamo alcuna rappresentazione visiva del parlato.

### La Struttura di ELAN

La struttura di ELAN è costruita su righe diverse, che possiamo approssimare a uno spartito musicale per più strumenti: in sostanza, *su ogni riga viene riportato ciò che dice un singolo parlante*.

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/image-4.png"
  caption="Visualizzazione dei tier"
%}

Questa è la visualizzazione che appare una volta aperto ELAN. Le righe qui riportate si chiamano **tier**: su ciascun tier (in questo caso ne sono presenti tre) bisogna trascrivere ciò che dice un singolo parlante.

Vediamo un esempio:
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/esempiotier.png"
  caption="Tier di un dialogo tratto dal film"
%}

In questo caso sono presenti solo due tier. Notiamo come le parole "will" e "it" appaiano tra parentesi quadre, in quanto questo è il simbolo del sistema Jefferson col quale si indica la sovrapposizione fra parlanti.

### Aggiungere il file da trascrivere

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/7 Avviare una trascrizione nuovo.PNG"
  caption="Associazione del file audio o video"
%}

Per avviare una trascrizione, la prima cosa da fare è associare il file audio o video che dobbiamo trascrivere, seguendo il percorso *File > New > Add media file*.

In generale, per tenere in ordine i file è prassi a dare al file della trascrizione lo stesso nome del file audio o video in modo tale che rimangano sempre associati e non si non si perdano.

### Salvare un file e impostare il Backup Automatico

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/8 backup automatico.PNG"
  caption="Impostazione del backup automatico"
%}

Ancor prima di iniziare la trascrizione è utile salvare il file quando è ancora vuoto. Fatto ciò, possiamo impostare il **backup automatico** (tramite il percorso *File > Automatic Backup*): è estremamente utile, in quanto così facendo non si perde il lavoro svolto nel caso in cui il software dovesse bloccarsi. Si consiglia di impostare il backup automatico con il minutaggio più basso possibile (quindi con un minuto).

### Creazione dei Tier

A questo punto dobbiamo creare i Tier, affinché ciascuno di essi sia associato al parlante che vogliamo trascrivere. Anziché creare un tier nuovo, possiamo modificare il tier che ELAN ci dà di default. Nella parte bassa della schermata troviamo una riga rossa col nome di “***tier default***”: possiamo semplicemente rinominare quel tier col nome che vogliamo associare a un certo parlante. Per farlo, clicchiamo col tasto destro sul tier default e selezioniamo “*Change Attributes of default*”; così facendo si apre una finestra nella quale è possibile modificare, tra le altre cose, il nome del tier.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/image-10.png"
  caption="Modificare il nome del tier default"
%}

A questo punto la cosa da fare è creare i tier successivi in base al numero di parlanti presenti nel file che vogliamo trascrivere. Se non sappiamo a priori quanti parlanti ci sono nel nostro file, possiamo tranquillamente aggiungere dei tier successivamente. Per aggiungere un nuovo tier basta andare sul pulsante “***Tier***” in alto e cliccare poi su “***Add New Tier***”: si aprirà dunque una finestra analoga a quella che abbiamo già visto, nella quale sarà possibile scegliere il nome del tier.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/image-11.png"
  caption="Creare un tier nuovo"
%}

Una cosa che spesso viene fatta è scegliere un codice alfanumerico per ogni tier, mentre nello spazio “participant” scriviamo il nome vero e proprio del partecipante (nel caso in cui non volessimo poi vederlo sulla trascrizione).

### La Trascrizione e i Comandi Essenziali

A questo punto possiamo avviare la trascrizione vera e propria. Anzitutto bisogna precisare che tutti questi comandi qui riportati possono essere eseguiti anche col mouse. L’utilizzo della tastiera può risultare difficile all’inizio, in quanto bisogna memorizzare le diverse combinazioni di tasti per ogni specifico comando, ma risulta molto più vantaggiosa in seguito.
Vediamo dunque alcuni dei comandi che servono per la trascrizione (tra i materiali c’è un PDF in cui c’è la lista completa delle combinazioni di tasti):

* **CTRL + Spazio**: avvia/stoppa la traccia audio.
* **CTRL/⌘ + K**: Seleziona/deseleziona la selection mode. Per individuare la stringa di parlato che vogliamo trascrivere bisogna entrare in selection mode, che può essere attivata o disattivata anche spuntando la casella apposita. A questo punto, quando si avvia/stoppa la traccia audio, si avvia/stoppa anche la selezione.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/13 Select Mode.PNG"
  caption="Casella di Selection Mode"
%}
* **ALT + N**: A tal punto dobbiamo creare la nostra unità. Ciò significa che dobbiamo individuare quella che noi consideriamo essere un'unità di parlato che vogliamo trascrivere e selezionarla con la selection mode che abbiamo visto; dopodiché, una volta che abbiamo selezionato lo spazio che vogliamo trascrivere, dobbiamo *creare una sorta di campo di testo all'interno di quello spazio selezionato*, così che possiamo scriverci dentro quello che vogliamo. Per creare il campo di testo nello spazio selezionato, usiamo la combinazione ALT + N (oppure, una volta selezionato lo spazio, si può cliccare col tasto destro del mouse e premere su “New Annotation”). Premendo invio, l’unità trascritta si salva.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/14 selezione.PNG"
  caption="Inserire una casella di testo"
%}
* **ALT + Mouse (in orizzontale)**: Volendo possiamo anche allargare o stringere la nostra unità con la combinazione ALT + mouse, premendo il tasto sinistro di quest'ultimo e spostando il cursore in senso orizzontale.
* **CTRL/⌘ + su/giù**: Questa combinazione serve per spostarsi da un tier all’altro in verticale (ad esempio, quando vogliamo trascrivere ciò che dice un parlante diverso da quello associato al tier su cui ci troviamo).
* **ALT + Mouse (in verticale)**: Può capitare di trascrivere le parole di un parlante nel tier sbagliato. Premendo ALT e il tasto destro del mouse, possiamo spostare l’unità da un tier all'altro (dunque in verticale).
* **SHIFT + ALT + C**: Questa combinazione serve p34 cancellare una selezione, che + uno step necessario per poter cominciare una nuova selezione.
* **SHIFT + Spazio**: Questa combinazione serve nel caso in cui volessimo riascoltare la singola annotazione (ad esempio, può capitare che in un determinato punto l'audio non sia chiarissimo).

### I Problemi più comuni

* **Cambiare le combinazioni di tasti**: In alcuni casi, le combinazioni di tasti precedentemente viste possono non funzionare, in quanto non tutte le tastiere funzionano allo stesso modo. In molti casi il problema può essere risolto svolgendo semplicemente l’azione col mouse, ma volendo ELAN offre anche l’opportunità di modificare le combinazioni di tasti associate a specifici comandi. Ad esempio, supponiamo che con la combinazione ALT + N io non riesca a creare il campo di testo nell’area selezionata: eseguendo il percorso *Edit > Preferences > Edit Shortcuts*, possiamo vedere quale combinazione di tasti è associata a quella specifica funzione ed eventualmente possiamo cambiarla a nostro piacimento.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/image-16.png"
  caption="Cambiare le Shortcut della tastiera"
%}
* **Cambiare la velocità di riproduzione**: Se l’audio è troppo lento o troppo veloce, nella sezione in alto è possibile trovare il tasto “rate”, col quale si può modificare la velocità di riproduzione. In alcuni casi la visualizzazione di ELAN è piccola. Per ingrandire solo la visualizzazione si può cliccare col tasto destro del mouse, selezionare “font size” e regolare la grandezza del testo. Un'altra cosa che può aiutare nella visualizzazione è il cursore in basso a destra, grazie al quale si può modificare la visualizzazione delle unità (restringendole o allargandole). Ciò vuol dire che la durata dell’unità si mantiene sull'asse temporale, ma diventa possibile visualizzare tutte le parole che prima non si riuscivano a vedere.
* **Ingrandire la visualizzazione delle unità**: In alcuni casi la visualizzazione di ELAN è piccola. Per ingrandire solo il corpo della trascrizione si può cliccare col tasto destro del mouse, selezionare “*font size*” e regolare la grandezza del testo. Un'altra cosa che può aiutare nella visualizzazione è il cursore in basso a destra, grazie al quale si può modificare la visualizzazione delle unità (restringendole o allargandole). Ciò vuol dire che la durata dell’unità si mantiene sull'asse temporale, ma diventa possibile visualizzare tutte le parole che prima non si riuscivano a vedere. In sostanza, con queste funzioni si alterà la modalità di visualizzazione delle unità, ma non le unità stesse.
* **Cancellare l'unità creata**: Per cancellare un'unità creata bisogna selezionarla cliccandoci sopra (in tal modo, l’unità dovrebbe diventare blu), per poi cliccare su “Delete Annotation”.
* **Il programma non legge il file mp3**: Tra i problemi che possono emergere durante la trascrizione, può capitare che ELAN non legga il file mp3 o che si blocchi. Il modo migliore per risolvere questo problema è cambiare il formato dell'audio, quindi convertirlo in formato .wav (è possibile farlo con Audacity, di cui abbiamo già parlato). Ovviamente, una volta cambiato il formato dell'audio bisogna riassociare nuovamente la trascrizione alla nuova traccia, e per fare ciò bisogna seguire questa sequenza: *Edit > Linked Files*.

## Funzioni Avanzate di ELAN

### Vedere tutte le unità associate a un tier

ELAN permette di vedere assieme tutto ciò che abbiamo trascritto per quanto riguarda un unico parlante. Per fare questo, bisogna andare su “***Grid***” e selezionare un tier: si apre così una visualizzazione a griglia di tutte le unità presenti all’interno del tier scelto.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/grigliatier.png"
  caption="Visualizzazione a griglia delle unità associate a un tier"
%}

###  La strutturazione dei tier

I tier possono avere diversi tipi di struttura. La strutturazione più semplice dei tier è quella che prevede l’associazione di un unico tier ad ogni parlante. Tuttavia, è possibile anche creare un quadro molto più complesso: è infatti possibile creare una serie di **tier dipendenti** dal tier che abbiamo associato a un parlante, creando così dei “sotto-tier”. In sostanza, è possibile creare un’**architettura interna** dei tier. Vediamo alcuni casi in cui questa funzione può essere utile:

* **Comunicazione non verbale**: posso fare un tier relativo solo ai movimenti del corpo di un determinato parlante.
* **Commenti**: Questa funzione può tornare utile anche nel momento in cui decido di lasciare dei commenti, andando dunque ad inserirli proprio in un tier dipendente (usandolo come un vero e proprio block notes)
* **IPA**: se voglio trascrivere delle parti con l’alfabeto IPA, posso farlo andando ad inserirle in un apposito tier.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/tiercomplesso.png"
  caption="Esempio di tier complesso"
%}

Vediamo un esempio. Qui abbiamo un tier complesso, in quanto vediamo una serie di “sotto-tier” associati ad un unico parlante. Tali tier contengono molti tipi di informazioni: nel primo tier vi è una trascrizione ortografica; nel secondo tier abbiamo una trascrizione in IPA; nel terzo tier abbiamo una trascrizione del linguaggio non verbale.

Vediamo dunque come aggiungere dei tier dipendenti.
La prima cosa da fare è creare un tier che segue la scansione temporale a cui voglio poi associarlo. Anzitutto andiamo su ***Type > Add New Tier Type***. Nella finestra che si apre andiamo poi su ***Stereotype*** e selezioniamo ***Time subdivision***, inserendo anche il nome del tipo.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/18 tier dipendente.PNG"
  caption="Add New Tier Type"
%}

A questo punto, una volta che abbiamo creato il nuovo type possiamo creare il nuovo tier. Seguiamo dunque gli stessi passaggi di prima (Tier > Add New Tier), ma questa volta bisogna specificare a quale tier dipende il “sotto-tier” che stiamo creando. Per farlo, nella riga “***Parent Tier***” dobbiamo selezionare il tier a cui vogliamo associarlo.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/19 tier dipendente.PNG"
  caption="Add New Tier"
%}

A questo punto, ci si ritrova con tutti i tier allineati. Per avere un tipo di visualizzazione in cui si rende evidente “quale tier dipende da quale tier”, bisogna seguire il seguente percorso: **Click destro sui tier** ***> Sort Tiers > Sort by Hierarchy***.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/20 tier dipendente.PNG"
  caption="Tier ordinati per gerarchia"
%}

### Divisione per Parola

Possiamo anche decidere di creare un tier dipendente in cui le parole presenti nella trascrizione vengono suddivise. Per farlo, bisogna anzitutto creare un nuovo tipo di tier (*Type > Add New Tier Type*), ma questa volta in Stereotype bisogna selezionare ***Symbolic Subdivision***.

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/21 divisione per parola.PNG"
  caption="Add Type - Symbolic Subdivision"
%}

Prima di procedere, è necessario creare un nuovo sotto-tier dipendente dal tier di cui vogliamo la tokenizzazione. A questo punto dobbiamo andare su *Tier*, e nel menù che si apre selezioniamo ***Tokenize Tier***: nella finestra che si apre, selezioniamo il Source Tier (ossia il tier che vogliamo tokenizzare) e la destinazione (cioè in quale tier vogliamo inserire la divisione per token), e infine clicchiamo su Start.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/tokenizetier.png"
  caption="Tokenize Tier"
%}

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/tierword.png"
  caption="Tier con parole divise"
%}

La tokenizzazione, però, ha un problema: tutte le parole separate da un apostrofo (come ad esempio "it's" nella foto di sopra) vengono contate come un unico token. Per evitare questo problema ci sono due soluzioni:

* Mettiamo uno spazio dopo ogni apostrofo (in modo da separare le due parole e risolvere il problema a monte):
* Possiamo inserire lo spazio in un secondo momento: per farlo, seguiamo anzitutto il percorso *Search > Find (and replace)*. Dopodiché clicchiamo sull’icona del foglio con l’asterisco: da qui, nello spazio “that matches” cerchiamo tutti gli apostrofi e li sostituiamo con la combinazione apostrofo + spazio. A questo punto non ci resta che ri-tokenizzare il tier. Alla fine di ciò, troveremo le parole separate da un apostrofo conteggiate come due token distinti (N.B.: in alcuni casi, può capitare che la ricerca dell’apostrofo non dia risultati. Per risolvere questo problema bisogna spuntare la casella chiamata “Regular Expression”).
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/24 divisione per parola.PNG"
  caption="Sostituzione dell'apostrofo con la combinazione 'apostrofo + spazio'"
%}

### Ricerca

ELAN permette di fare ricerche molto raffinate, anche in base a quanto è strutturata la nostra annotazione. Possiamo fare una ricerca semplice per forme all’interno della trascrizione come abbiamo già descritto nel punto precedente (quindi seguendo il percorso *Search > Find (and replace)* oppure premendo CTRL/⌘+ F), ma possiamo anche fare ricerche su più file contemporaneamente (dunque usando i file delle nostre trascrizioni come se fossero un corpus).
Per fare ciò andiamo anzitutto su ***Search > Search Multiple EAF***; dopodiché bisogna definire il dominio della ricerca. Dopo aver creato un nuovo dominio di ricerca su New Domain, possiamo aggiungere una cartella / un file e diamo il nome al dominio in quesitone.

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/26 search.PNG"
  caption="Definizione del dominio"
%}

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/27 search.PNG"
  caption="Definizione del dominio"
%}

A questo punto possiamo fare la ricerca in questione: cercando una parola (nell’esempio viene cercata la parola “se”), vedremo tutte le occorrenze di quella specifica parola all’interno dei nostri file.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/28 search.PNG"
  caption="Esempio di ricerca"
%}

### Esportazione dei File

Il formato della trascrizione è il file EAF, ma si possono utilizzare diversi formati. Tra i vari formati disponibili vi è il TXT, che permette di utilizzare il file su vari programmi usati per l’analisi linguistica. Per selezionare il formato, basta andare su File > Export e selezionare il formato che ci interessa.

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/29 export.PNG"
  caption="Modalità di esportazione"
%}

{%
  include figure.html
  image="images/seminar-images/elantrascrizione/30 export.PNG"
  caption="Modalità di esportazione"
%}

Esportando il file in TXT il risultato è questo: viene rappresentato verticalmente ciò che su ELAN appare orizzontalmente.
{%
  include figure.html
  image="images/seminar-images/elantrascrizione/31 export.PNG"
  caption="Visualizzazione del file esportato in TXT"
%}
