import random
import re

html_path = "theory-os-internal.html"

with open(html_path, encoding="utf-8") as f:
    html = f.read()

pattern = re.compile(
    r'<div class="card">\s*<div class="question">(.*?)</div>\s*<div class="answer">(.*?)</div>',
    re.DOTALL
)

cards = [(q.strip(), a.strip()) for q, a in pattern.findall(html) if q.strip()]

# 10 domande casuali
quiz = random.sample(cards, 10)

score = 0
for i, (question, answer) in enumerate(quiz, 1):
    print(f"\nDomanda {i}: {question}")
    input("Premi invio per vedere la risposta...")
    print(f"Risposta: {answer if answer else '[Nessuna risposta nel file]'}")
    print("-" * 40)

print("Quiz completato!")