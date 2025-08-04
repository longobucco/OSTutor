# OSTutor: Esercizi Sistemi Operativi - Memoria Virtuale

OSTutor è una piattaforma interattiva pensata per aiutare gli studenti a comprendere e mettere in pratica i concetti fondamentali dei sistemi operativi, con particolare attenzione alla memoria virtuale, gestione della paginazione, I/O, file system e hardware di memorizzazione. Il progetto integra un tutor digitale che guida l'utente nella risoluzione degli esercizi e fornisce spiegazioni dettagliate.

## Obiettivi

- Fornire agli studenti uno strumento pratico per esercitarsi su domande d'esame e quiz riguardanti la memoria virtuale e altri aspetti dei sistemi operativi.
- Presentare spiegazioni dettagliate e risposte commentate per favorire la comprensione dei meccanismi di base come paginazione, IPT, DMA, allocazione file system, interrupt e prestazioni dei dispositivi di memorizzazione.
- Offrire una interfaccia web semplice e intuitiva per la consultazione e lo studio autonomo.
- Integrare un tutor digitale che supporta lo studente nella comprensione degli esercizi, suggerisce strategie di risoluzione e fornisce feedback immediato.

## Struttura

- Tutti gli esercizi sono visualizzati in modo interattivo tramite una pagina HTML (`exam-os.html`, `exam-os161.html`, `theory-os-internal.html`).
- Ogni esercizio include domanda, risposta sintetica e spiegazione dettagliata, con la possibilità di ricevere suggerimenti e feedback dal tutor.
- Il file `tutor.py` gestisce la logica degli esercizi, la valutazione delle risposte e l'integrazione con l'interfaccia web. Questo script permette di generare nuovi esercizi, verificare le soluzioni inserite dagli utenti e fornire spiegazioni personalizzate.
- Il progresso degli utenti può essere tracciato tramite il file `progress.json`, che memorizza lo stato degli esercizi svolti.

## Destinatari

Il progetto è pensato per studenti universitari di informatica, ingegneria informatica o chiunque voglia approfondire i concetti di base dei sistemi operativi in modo pratico e guidato. Grazie all'integrazione del tutor digitale, OSTutor è adatto sia per lo studio autonomo che per l'utilizzo in contesti didattici strutturati.
