import requests
import os
import json
from bs4 import BeautifulSoup
import re


def ask_ai(prompt, context=""):
    try:
        res = requests.post("http://localhost:11434/api/generate", json={
            "model": MODEL,
            "prompt": context + "\n\n" + prompt,
            "stream": False
        })
        return res.json().get("response", "")
    except Exception:
        return ""


def carica_progressi():
    if os.path.exists("progress.json"):
        with open("progress.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"domande_fatte": []}


def salva_progressi(progressi):
    with open("progress.json", "w", encoding="utf-8") as f:
        json.dump(progressi, f, indent=2, ensure_ascii=False)


def domanda_gia_fatta(domanda, domande_fatte):
    return any(d["domanda"] == domanda for d in domande_fatte)


def fai_quiz(contexto, progressi):
    prompt = "Genera una singola domanda d'esame nuova e utile, diversa da queste:\n\n"
    gia_fatte = [d["domanda"] for d in progressi["domande_fatte"]]
    if gia_fatte:
        prompt += "\n".join(f"- {d}" for d in gia_fatte[-10:])
    prompt += "\n\nSolo una domanda, chiara e completa."
    domanda = ask_ai(prompt, contexto).strip()
    if not domanda:
        print("Errore: impossibile generare una domanda. Riprova più tardi.")
        return
    print("\nDomanda:", domanda)
    while True:
        valutazione = input(
            "Hai risposto correttamente? (corretto / sbagliato / da_rivedere): ").strip().lower()
        if valutazione in ["corretto", "sbagliato", "da_rivedere"]:
            break
        print("Valore non valido. Inserisci: corretto / sbagliato / da_rivedere.")
    progressi["domande_fatte"].append({
        "domanda": domanda,
        "valutazione": valutazione
    })
    salva_progressi(progressi)


def estrai_flashcard(path):
    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    cards = []
    for card in soup.find_all("div", class_="card"):
        q = card.find("div", class_="question")
        a = card.find("div", class_="answer")
        if q and a:
            cards.append((q.text.strip(), a.text.strip()))
    return cards


def estrai_esercizi(path):
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    # Cerca array esercizi in JS
    match = re.search(r"const esercizi = \[(.*?)\];", html, re.DOTALL)
    esercizi = []
    if match:
        items = re.findall(r"{(.*?)}", match.group(1), re.DOTALL)
        for item in items:
            domanda = re.search(r'domanda:\s*"(.*?)"', item, re.DOTALL)
            risposta = re.search(r'risposta:\s*"(.*?)"', item, re.DOTALL)
            spiegazione = re.search(r'spiegazione:\s*"(.*?)"', item, re.DOTALL)
            if domanda and risposta and spiegazione:
                esercizi.append({
                    "domanda": domanda.group(1).replace("\n", " ").strip(),
                    "risposta": risposta.group(1).replace("\n", " ").strip(),
                    "spiegazione": spiegazione.group(1).replace("\n", " ").strip()
                })
    return esercizi


def scegli_flashcard(flashcards):
    import random
    return random.choice(flashcards)


def scegli_esercizio(esercizi):
    import random
    return random.choice(esercizi)


MODEL = "mistral"


def mostra_spiegazione(esercizi, domanda, flashcards=None):
    # Cerca tra esercizi
    for ex in esercizi:
        if domanda.lower() in ex["domanda"].lower():
            return ex["spiegazione"]
    # Cerca tra flashcard
    if flashcards:
        for q, a in flashcards:
            if domanda.lower() in q.lower():
                return a
    # Se non trovata, genera spiegazione con AI
    return genera_spiegazione_ai(domanda)


def genera_spiegazione_ai(domanda):
    prompt = f"Spiega in modo chiaro e sintetico: {domanda}"
    try:
        res = requests.post("http://localhost:11434/api/generate", json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        })
        return res.json().get("response", "Spiegazione non disponibile.")
    except Exception:
        return "Spiegazione non disponibile."


if __name__ == "__main__":
    flashcards = estrai_flashcard("theory-os-internal.html")
    esercizi_os = estrai_esercizi("exam-os.html")
    esercizi_os161 = estrai_esercizi("exam-os161.html")
    progressi = carica_progressi()
    print("OSTutor avviato. Comandi: 'flashcard', 'esercizio', 'spiega', 'fine'")
    while True:
        cmd = input("\n🧑‍🎓 Tu: ").strip().lower()
        if cmd in ["fine", "exit", "esci"]:
            print("Salvataggio progressi...")
            salva_progressi(progressi)
            break
        elif cmd == "flashcard":
            domanda, risposta = scegli_flashcard(flashcards)
            print(f"\n🃏 Flashcard:\nDomanda: {domanda}")
            input("Premi invio per vedere la risposta...")
            print(f"Risposta: {risposta}")
        elif cmd == "esercizio":
            gruppo = input("Scegli gruppo: 'os' o 'os161': ").strip().lower()
            if gruppo == "os":
                esercizio = scegli_esercizio(esercizi_os)
            else:
                esercizio = scegli_esercizio(esercizi_os161)
            print(f"\n📝 Esercizio:\nDomanda: {esercizio['domanda']}")
            input("Premi invio per vedere la risposta...")
            print(f"Risposta: {esercizio['risposta']}")
            print(f"Spiegazione: {esercizio['spiegazione']}")
        elif cmd == "spiega":
            domanda = input(
                "Scrivi la domanda/esercizio da spiegare: ").strip()
            gruppo = input("Scegli gruppo: 'os', 'os161': ").strip().lower()
            if gruppo == "os":
                spiegazione = mostra_spiegazione(
                    esercizi_os, domanda, flashcards)
            else:
                spiegazione = mostra_spiegazione(
                    esercizi_os161, domanda, flashcards)
            print(f"Spiegazione: {spiegazione}")
            # Salva la domanda spiegata
            valutazione = input(
                "Valuta la tua comprensione (corretto / sbagliato / da_rivedere): ").strip().lower()
            progressi["domande_fatte"].append({
                "domanda": domanda,
                "valutazione": valutazione
            })
            salva_progressi(progressi)
        # elif cmd == "quiz":
        #     contexto = "[TEORIA]\n" + "\n".join(q for q, _ in flashcards) + "\n[ESERCIZI]\n" + "\n".join(
        #         ex["domanda"] for ex in esercizi_os + esercizi_os161)
        #     fai_quiz(contexto, progressi)
        elif cmd == "riprendi":
            print("Domande già fatte:")
            for d in progressi["domande_fatte"]:
                print(f"- {d['domanda']} [{d['valutazione']}]")
        else:
            print(
                "Comando non riconosciuto. Usa 'flashcard', 'esercizio', 'spiega', 'riprendi', 'fine'.")
