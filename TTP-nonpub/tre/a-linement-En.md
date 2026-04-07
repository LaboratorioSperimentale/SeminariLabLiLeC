---
id-asset: '01'
title: a-linement
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
replicated_from: Lista-Seminari/en/a-linement-En.md
topic_section: Tre
tag_combo:
- ob/tre
---

> Copia generata automaticamente per il topic **Tre**.
> Sorgente: `/Lista-Seminari/en/a-linement-En.md`

%%layout: seminar
title: "A-linement: Un tool di importazione e allineamento sottotitoli per la ricerca scietifica"
author: letiziastrocchi
speaker: Francesco Vitucci, Michele Zangheri %%


#  "A-linement": Un tool di importazione e allineamento sottotitoli per la ricerca scientifica

# Che cos'è A-linement

**A-linement** è un software per l'analisi dei sottotitoli, che nasce nel 2022 grazie al lavoro di Francesco Vitucci, professore associato in Lingua e Linguistica Giapponese presso il Dipartimento di Lingue, Letterature e Culture Moderne dell'Alma Mater Studiorum Università di Bologna, Michele Zangheri, dottore ed esperto in traduzione televisiva e con l'aiuto di Paolo Pierruccio, informatico. A-linement viene utilizzato nell'ambito della traduzione audiovisiva interlinguistica.

A-linement è un **tool** che aiuta, chi lo utilizza, nell'analisi qualitativa e poi quantitativa delle traduzioni interlinguistiche. Questo strumento nasce dalla necessità di concentrarsi su alcuni aspetti delle lingue, in particolare sulle traduzioni e sottotitolazioni interlinguistiche. A-linement si concentra anche, in modo particolare, sull'analisi comparativa della punteggiatura tra lingue diverse.

A-linement lavora per *frame*, ovvero fotogrammi all'interno dei quali vengono visualizzati le stringhe contenenti i sottotitoli. Il risultato finale sarà una tabella dove vengono comparati ed allineati i vari sottotitoli. il **tool** di A-linement può essere  utilizzato per l'analisi, sia di scene brevi tratte da film contenenti per esempio 35 battute, sia per interi film/docufilm. 

inserire foto tabella da chiedere a vitucci

Grazie a questo strumento è alla fine possibile capire come è avvenuta la sottotitolazione a livello diacronico. 

# Come utilizzare A-linement

Lo strumento di A-linement comunica con il software Excel, ovvero produce in automatico delle tabelle Excel che possono essere subito incluse nelle proprie varie ricerche linguistiche. 

immagine interfaccia vitucci

(A-linement, ancora sottoforma di link, è raggiungibile trammite il profilo Github di Paolo Pirruccio, sarà però presto disponibile in versione software accessibile anche senza connessione ad Internet.)

A-linement si presenta con una interfaccia principalmente bianca caratterizzata da diversi tasti verdi, al disotto di questi ci sono varie colonne (dieci per l'esattezza) in cui verrano poi inserite le varie traduzioni in lingue diverse.

## I *pulsanti* di A-linement e come utilizzarli

- "**Convert to table**": motore del tool, è il pulsante tramite il quale è possibile convertire i dati in tabella, tabella che verrà poi importata su Execel, e che sarà possibile utilizzarla nel medesimo istante per la propria ricerca.

*Primo Step*:
importare i dati all'interno di A-linement, questo è possibile grazie al pulsante "**Scegli il file**": selezionando il file desiderato dalla cartella di appartenenza, questo apparirà al fianco destro di tale pulsante. (Il file deve essere in formato SRTOASS.)

  Successivamente cliccando sul pulsante "**Convert subs file**" apparirà una finestra contenente il "**Conversion output**" ovvero il testo da analizzare. (Con testo si intende il dialogo di qualsiasi contenuto audiovisivo.) Tramite il pulsante "**Copy subtitles**" verrà copiato l'intero contenuto, nel caso si volesse andare a studiare solo una parte di testo, basta selezionarla e copiarla con Ctrl+C. 

*Secondo Step*: 
incollare il contenuto sulla prima colonna di A-linement con Ctrl+V. Le colonne possono essere rinominate, per esempio: Column1 in JAP CC, Column2 in ENG SUB, Column3 in ITA SUB, e così via. 

  Se si vuole già trasformare questo contenuto in tabella serve utilizzare il pulsante "**Convert to table**", ma facendo ciò il passaggio da una stringa di testo ad un'altra viene letto come un'ulteriore nuova stringa, che in tabella viene visualizzata come una stringa vuota. 

inserire immagine stringa vuota tra testo 

*Terzo Step*: per risolvere va inserito il simbolo *asterisco* (*), questo grazie al pulsante "**Replace newline**" che sostiuisce tutti gli *a capo* creati nel passaggio da una stringa ad un'altra. 

Cliccando "**Convert to table**" ora ogni stringa è al suo posto. 

Altri comandi:

- "**Reset**": come dice il nome stesso, per eliminare ogni contenuto e ricominciare da capo. 

- "**Bold text**": per evidenziare parti di testo specifiche, cliccando questo pulsante si apre una casella di testo dove va digitato il testo desiderato, il quale riappare inscritto tra <b> e </b> ... Successivamente copiare ed incollare il testo in tabella, ed una volta convertito in tabella il testo appare già in **grassetto**. 

- "**Save**": per salvare in local sul device con cui si opera. 

- "**Load**": per ricaricare l'ultima versione di testo salvata in caso di reset o cancellazione di quest'ultima. 

- "**Export json**": per creare un file di salvataggio esportabile da spostare tra device diversi o da condividere a qualcuno. Cliccando sul pulsante, viene chiesto di salvare il file con estension .json e per caricarlo sul programma cliccare "**Scegli il file**" ed in seguito "**Convert subs file**". 

Sia il comando "**Replace newline**" che "**Bold**" possono essere inseriti manualmente. 

## Come importare da A-linement ad Excel

Per importare grandi quantità di file i passaggi iniziali sono sempre li stessi: scegliere il proprio file, cliccare su "**Convert subs file**", copiare ed incollare il contenuto nella prima colonna. Questo processo va ripetuto per tutte le sottotitolazioni possedute, alla fine si avrà un vario numero di colonne nella quali sarà presente lo stesso testo ma in lingue diverse.

Importante è ricordarsi di eliminare sempre la prima stringa intitolata "**Conversion output**" che è irrilevante allo studio.

Segue il passaggio di "**Replace newline**" così da eliminare gli spazi tra le stringhe, ed infine "**Convert to table**". 

Il risultato sarà una tabella numerata di tutte le traduzioni. 

- Il passaggio successivo è copiare la tabella col pulsante "**Copy table**", aprire Excel e alla coordinata **A1** incollare la tabella. 

Un passaggio intermedio, prima di trasportare il file su Excel, può essere quello di rendere in grassetto stringhe specifiche, così da ritrovarle più facilmente per eventuali future indagini.

Il prodotto finale sarà una tabella perfettamente numerata ed allineata, al numero 1 la prima stringa di testo, al numero 2 la seconda stringa di testo, e così via dicendo. Su questo prodotto sarà poi possibile uno studio più specifico. 

immagine tabella su excel

## Cosa fare se le stringe su Excel non sono allineate 

Nel caso di eventuali stringhe (della stessa frase ma di sottotitolazioni diverse) non allineate, i passaggi sono i seguenti: 

- selezionare la stringa sbagliata e con il tasto destro selezionare "**Inserisci**" e in seguito "**Sposta celle in basso**". 

Così facendo si andrà a creare una cella vuota dove prima c'era la stringa errata. 

## Cosa sono i pop up 

I pop up sono gli approfondimenti monoculturali che si trovano solitamento in alto rispetto al sottotitolo. 

Rendendoli in "**Bold**" è possibile ritrovarli più facilemente in un eventuale studio solo sui pop up dei sottotitoli. 

## Il risultato finale

immagini tabelle da vitucci mostrate al min 43 circa

Grazie al tool di A-linement è stato possibile intercettare delle disparità nell'allinamento, come nello studio incentrato sull'analisi interpuntiva, ovvero l'uso della punteggiatura in lingue diverse. 

Con A-linment è oggi possibile uno studio più approfondito delle diverse sottotitolazioni e anche uno studio più apporofondito a livello diacronico, ovvero una comparazioni di diversi dataset. 

Questo tool è stato recentemente utilizzato per l'analisi sulla manipolazione sull'ideologia linguistica. Lo studio si incentrava sull'analisi di violetti stereotipati, violetti creati all'interno delle traduzioni audiovisive che però non rispecchiano il vero parlato e l'dentità femminile giapponese. Grazie ad A-linement è stato possibile studiare come questo veniva riproposto nel tempo facendo comparazioni dello stesso film distribuito più volte sul mercato. 


link ad A-linement https://nocoldiz.github.io/a-linement/ 

