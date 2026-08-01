# 📸 "Truffa del link che fa le foto" - Educational Proof of Concept (PoC)

Questo repository contiene una **Proof of Concept (PoC) a scopo puramente educativo** per dimostrare come funziona tecnicamente la truffa diffusa sui social network (spesso camuffata da finti video di TikTok) che scatta foto di nascosto agli utenti.

Il progetto nasce per fare **Cybersecurity Awareness**, mostrando quanto sia facile per un sito web malevolo catturare un'immagine e inviarla a un bot Telegram, se l'utente concede ingenuamente i permessi alla fotocamera.

## 🧠 Come funziona la truffa (e questo codice)

L'architettura si divide in due parti:

1.  **Frontend (L'esca - HTML/JS):** 
    Una pagina web apparentemente innocua richiede i permessi per accedere alla fotocamera e al microfono. Se l'utente clicca su "Consenti", uno script in JavaScript cattura un frame del flusso video, lo converte in formato Base64 e lo invia silenziosamente al server tramite una richiesta `POST`.
2.  **Backend (L'esfiltrazione - Flask/Python):** 
    Un server Flask riceve la stringa Base64, la converte in un file immagine temporaneo (`photo.png`) e utilizza le API ufficiali di Telegram per inviarla immediatamente a una chat privata tramite un Bot. Subito dopo l'invio, il file locale viene distrutto.

## 🛡️ Come difendersi

L'obiettivo di questo codice è insegnare agli utenti a proteggersi. Ecco le regole d'oro:
*   **Mai concedere permessi a caso:** Non autorizzare l'accesso a fotocamera, microfono o posizione a siti web sconosciuti o a cui sei arrivato tramite link sospetti (es. catene di messaggi, storie Instagram ambigue).
*   **Controlla l'URL:** Se un link promette un video di TikTok ma l'indirizzo nella barra di ricerca non è `tiktok.com`, sei di fronte a un tentativo di phishing.
*   **Revoca i permessi:** Nelle impostazioni del tuo browser (Chrome, Safari, ecc.), controlla regolarmente quali siti hanno accesso alla tua fotocamera e revoca le autorizzazioni a quelli che non riconosci.

## 🛠️ Requisiti Tecnici

Per analizzare o testare in locale questo codice (nel tuo ambiente controllato):
*   Python 3.x
*   Librerie: `Flask`, `requests`
*   Un Bot Telegram valido (creato tramite BotFather) e il relativo Chat ID.

**Configurazione Sicura:** 
Assicurati di configurare il `BOT_TOKEN` e il `CHAT_ID` come variabili d'ambiente nel tuo sistema operativo o tramite un file `.env`. Non inserire mai le tue chiavi in chiaro nel codice sorgente.

## ⚠️ Disclaimer Etico e Legale

> **Questo progetto è stato creato ESCLUSIVAMENTE per scopi educativi e di ricerca sulla sicurezza informatica.**

> L'autore disapprova fermamente qualsiasi utilizzo di questo codice per scopi malevoli, come phishing, violazione della privacy, cyberstalking o qualsiasi altra attività illegale. Acquisire immagini di persone a loro insaputa o senza il loro esplicito consenso è un reato e una grave violazione della privacy (GDPR). 

> Scaricando o utilizzando questo codice, l'utente si assume la piena e totale responsabilità delle proprie azioni. L'autore non è responsabile in alcun modo per l'uso improprio di queste informazioni.
