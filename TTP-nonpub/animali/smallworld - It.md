---
id-asset: '10'
title: smallworld
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
replicated_from: Lista-Seminari/smallworld - It.md
topic_section: questo è il titolo
tag_combo:
- ob/animali
---

> Copia generata automaticamente per il topic **questo è il titolo**.
> Sorgente: `/Lista-Seminari/smallworld - It.md`

%%layout: seminar
title: "Small World of Words: mappare le Reti Semantiche attraverso le associazioni libere di parole"
author: samuelecirrito
speaker: Maria Montefinese
%%

## Il progetto

Il progetto **Small World of Words** nasce nel 2005 grazie al lavoro di Simon De Deyne con un'idea sviluppata a partire da un paio di articoli pubblicati nel 1996 e nel [2004](http://web.mit.edu/cocosci/archive/Papers/03nSteyvers.pdf) da M. Steyvers e J. B. Tenenbaum sui **network small-world**. Su questa base teorica, De Deyne concentra, quindi, i suoi sforzi sulla costruzione di una rete di associazioni verbali in olandese. La costruzione di questo database inizia nel 2006 e si conclude nel 2013.
Successivamente, Marc Brysbaert incoraggia De Deyne a replicare il progetto in inglese. In questo modo nasce il secondo grande data-set.

Nel corso degli anni sono state raccolte associazioni per 19 lingue. La collaborazione per la costruzione di un data-set in italiano inizia nel 2016. Esiste anche delle pagine sui social, [instagram](https://www.instagram.com/associaparole/), [twitter](https://x.com/associaparole) e [facebook](https://www.facebook.com/StudioAssociazioneDiParole), per la promozione della creazione di questo data-set.

I dati del progetto possono essere consultati su questa [pagina](https://smallworldofwords.org/it/project/explore). È possibile selezionare la lingua e cercare una parola. Verrano mostrate le associazioni a quella parola come parola cue (ovvero saranno mostrate le parole fornite come risposta), e le parole cue che hanno elicitato tale risposta. Su questa [pagina](https://smallworldofwords.org/it/project/visualize) è, invece, possibile visualizzare le associazioni, attraverso tre diverse modalità di visualizzazione.

I dati del progetto saranno resi disponibili su OSF e GitHub non appena verrà raggiunto il traguardo dei 5000 stimoli, soglia minima per ottenere associazioni affidabili e signiticative.

## Lo studio delle associazioni verbali

La maggior parte dei lavori sulle associazioni verbali risale agli anni '60. Soprattutto in Russia esiste una solida tradizione di studio delle associazioni verbali integrata nella **teoria della visione linguistica del mondo**,secondo cui le associazioni semantiche riflettono e modellano il modo in cui percepiamo e interpretiamo il mondo attraverso il linguaggio.

Oggi gli studi sulle associazioni verbali stanno vivendo una rinascita. Le associazioni rappresentano, infatti, un modo semplice ed efficiente per **esplorare i contenuti della mente** senza che questi vengano espressi attraverso strutture linguistiche complesse e discorsive. Inoltre, un altro motivo di interesse delle associazioni verbali è dato dalla loro capacità di descrivere l'esperienza dei parlanti sia come creatori che come destinatari di testi; riflettono, dunque, la struttura della comunicazione umana razionale e **rappresentano l'intera esperienza verbale e non-verbale** accumulata dai parlanti nativi.

## Analisi delle associazioni verbali

Le associazioni verbali, sono, quindi, connessioni tra parole che il nostro cervello stabilisce sulla base dell'**esperienza**, del **contesto** e del **significato** delle parole.

Da una prospettiva di rete, le associazioni, e dunque le relazioni tra le parole di un insieme, possono essere analizzate su diversi livelli:

1. **livello locale**: su questo livello l'analisi si concentra sui **singoli nodi**, e si esaminano, quindi, connessioni individuali tra parole; l'analisi a questo livello permette di comprendere **associazioni immediate e dirette**;
2. **livello intermedio**: su questo livello l'analisi si concentra sui **cluster di nodi** e permette di reperire informazioni su regioni coerenti all'interno della rete (i cluster), che possono rappresentare **categorie semantiche**;
3. **livello globale**: su questo livello l'analisi si concentra sull'**intera rete** e permette di reperire informazioni sulla resilienza ed efficacia della rete (ad esempio, quanto velocemente si può diffondere un'informazione); l'analisi su questo livello permette, inoltre, di confrontare **diversi tipi di architetture informative** (tra lingue diverse, discipline diverse, persone con età diversa).

## Raccolta e pulizia dei dati

Per contribuire alla ricerca, si può accedere a questa **[pagina](https://smallworldofwords.org/en/project/home)** e selezionare la propria lingua madre. Il compito consiste nell'associare le prime tre parole che vengono in mente in risposta a 18 parole cue.

Poiché le associazioni variano molto da persona a persona (dipendono, infatti, dall'esperienza individuale del parlante), affinché i dati vengano considerati affidabili, sono stati raccolti almeno 60 partecipanti per ciascuna parola stimolo.

Le parole stimolo sono state selezionate attraverso un metodo di **campionamento a valanga**, che ha permesso di includere parole con diversa frequenza d'uso. Inoltre, anche le parole associate, quindi date come risposta a questi stimoli, sono state aggiunte gradualmente come stimoli. L'obiettivo del progetto è ottenere associazioni per un totale di 5000 parole cue.

Per quanto riguarda la pulizia dei dati raccolti, innanzitutto vengono rimossi tutti i segni di interpunzione; il testo viene poi normalizzato, ovvero si correggono errori di ortografia e si rimuovo le maiuscole.

Per la selezione dei partecipanti sono applicati alcuni criteri. In particolare, verranno esclusi quei partecipanti che:

* Inseriscono frequentemente risposte formate da più parole;
* Hanno un'alta percentuale di risposte ripetute;
* Hanno un'alta percentuale di risposte non date;
* Hanno un'alta percentuale di risposte con parole in lingue diverse dall'italiano;
* Hanno meno di 18 anni.

I dati vengono, infine, bilanciati selezionando 60 risposte per ogni stimolo. Inoltre, viene data attenzione a bilanciare la rappresentanza di genere.

## Calcolo delle misure di associazione

La forza di associazione è una misura asimettrica, ovvero, l'associazione tra due parole non è reciproca. Per esempio, la probabilità di associare *luce* a *accecante* è maggiore rispetto alla probabilità di associare *accecante* a *luce* (dunque, considerando p(risposta|stimolo|, p(luce|accecante|)>>p(accecante|luce)). Inoltre, questa misure non è applicabile alla maggior parte delle coppie, infatti, la maggior parte delle parole presenti nel database non viene fornita come risposta alla maggior parte dei cue.

Si possono anche calcolare misure di somiglianza semantica utilizzando diverse metrice a livello locale (di cluster) o globale (di rete).

## Ricerche e risultati

I risultati ottenuti dalle norme di associazione sono già stati utilizzati in letteratura per spiegare le prestazioni del partecipante in vari compiti comportamentali.

![plain image](/images/seminar-images/swow/swow1.png)
_Dal grafico si osserva che le misure di somiglianza derivate dalle norme di associazione per il rioplatense (in azzurro) presentano una correlazione più forte con i giudizi di somiglianza tra concetti rispetto ad altre misure ottenute da corpora._

In particolare, le norme di associazione si sono rivelate un indicatore più preciso rispetto ad altre fonti di dati, ad esempio i corpora, per misurare le somiglianze semantiche tra concetti. Le norme, inoltre, predicono con maggiore precisione i giudizi di somiglianza, nonché il comportamento dei partecipanti in compiti di relazione tra concetti.

![plain image](/images/seminar-images/swow/swow2.png)
_I risultati derivano dalle norme di associazione per il cinese mandarino._

Aspetto da notare è la differenza nelle prestazioni tra concetti concreti e astratti. Sembra, infatti, che l'associazione predica meglio la relazione tra concetti concreti. Osservando l'ultimo grafico, si può anche aggiungere che l'analisi delle risposte multiple (considerare, quindi, non solo R1, ma anche R2 ed R3) fornisce una visione più completa delle connessioni semantiche tra concetti.

Le associazioni semantiche svolgono, inoltre, un ruolo fondamentale nel riconoscimento delle parole.
![plain image](/images/seminar-images/swow/swow3.png)

### Studio delle differenze culturali e linguistiche

Un altro importante utilizzo delle norme di associazione è lo studio delle differenze culturali e linguistiche, attraverso confronti diretti tra risposte fornite da parlanti lingue diverse a partire dagli stessi stimoli. Queste analisi permettono di osservare similirità tra lingue e specificità culturali. Cultura e lingua, infatti, influenzano il nostro modo di associare i concetti.

![plain image](/images/seminar-images/swow/swow4.png)
_Dall'immagine notiamo come, a seconda della lingua, cambiano le parole più frequentemente associate al concetto **Italia**. Più è grande una parola, più volte questa sarà stata associata._
