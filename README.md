# OSTutor: Studio interattivo di Sistemi Operativi & OS161

OSTutor è una piattaforma interattiva per studiare e approfondire i concetti di sistemi operativi e OS161. Permette di esercitarsi su quiz, domande d'esame e teoria, con spiegazioni dettagliate e un tutor digitale che guida lo studente passo passo.

## Funzionalità principali

- Quiz interattivi e domande d'esame su memoria virtuale, paginazione, IPT, DMA, file system, interrupt, dispositivi di memorizzazione e OS161.
- Spiegazioni dettagliate e risposte commentate per ogni esercizio.
- Tutor digitale che suggerisce strategie di risoluzione, fornisce feedback immediato e aiuta nella comprensione degli argomenti.
- Tracciamento del progresso utente e salvataggio degli esercizi svolti.
- Generazione automatica di nuovi esercizi e verifica delle risposte inserite.
- Interfaccia web semplice e intuitiva per consultare teoria, quiz e flashcards.
- Materiali di supporto e PDF di approfondimento integrati.

## Struttura

- Esercizi e quiz disponibili tramite pagine HTML (`exam-os.html`, `exam-os161.html`, `theory-os-internal.html`).
- Ogni esercizio include domanda, risposta sintetica, spiegazione e suggerimenti.
- `tutor.py` gestisce la logica degli esercizi, la valutazione e l'integrazione con l'interfaccia web.
- Il file `progress.json` salva lo stato degli esercizi svolti.

## Destinatari

OSTutor è pensato per studenti universitari di informatica, ingegneria informatica e chiunque voglia approfondire i sistemi operativi e OS161 in modo pratico e guidato, sia per studio autonomo che in contesti didattici.

## Prerequisiti

- Python 3.x installato
- Browser web

## Materiali di supporto

La cartella `flashcards/` contiene domande e risposte rapide (`OS_flashcards.pdf`). Nella cartella `src/OSTutor/` sono disponibili PDF di approfondimento (es. `OS-Internals.pdf`).

## Contribuire

Contributi, suggerimenti e nuove proposte di esercizi sono benvenuti! Forka il repository, crea una branch e invia una pull request, oppure segnala errori tramite la sezione Issues.

## Licenza

Questo progetto è rilasciato sotto la licenza MIT. Consulta il file `LICENSE` per maggiori dettagli.
