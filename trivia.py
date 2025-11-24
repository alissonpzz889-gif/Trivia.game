import html
import requests
import random

def intro():
    print("\n========================================")
    print("🎮 BEM-VINDO AO TRIVIA! 🎉")
    print("========================================")
    print("Você responderá 7 perguntas aleatórias.")
    print("Escolha a dificuldade e tente fazer o máximo de pontos!")
    print("Boa sorte, jogador! 🚀")
    print("========================================\n")

def translate(text):
    text = html.unescape(text)
    url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=pt-BR&q=" + text

    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()[0][0]  # texto traduzido
    except:
        pass

    return text
def fetch_questions(amount=7, difficulty="easy"):
    url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=multiple"
    res = requests.get(url)

    if res.status_code == 200:
        return res.json()["results"]
    return []

def choose_difficulty():
    print("\n=== ESCOLHA A DIFICULDADE ===")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")

while True:
        op = input("Escolha (1/2/3): ")

        if op == "1":
            return "easy"
        if op == "2":
            return "medium"
        if op == "3":
            return "hard"

        print("Opção inválida, tente novamente.")

def run_quiz():
    intro()
    difficulty = choose_difficulty()
    print("\nBuscando questões...\n")

    questions = fetch_questions(amount=7, difficulty=difficulty)

    if not questions:
        print("Erro ao buscar perguntas.")
        return

    score = 0

    for i, q in enumerate(questions, start=1):

        pergunta = translate(q["question"])
        correta = translate(q["correct_answer"])
        alternativas = [translate(a) for a in q["incorrect_answers"]]
        alternativas.append(correta)
        random.shuffle(alternativas)

        print(f"\nPergunta {i}: {pergunta}")

        for idx, alt in enumerate(alternativas, start=1):
            print(f"{idx}) {alt}")
        while True:
            try:
                user_ans = int(input("Resposta (1-4): "))
                if 1 <= user_ans <= len(alternativas):
                    break
            except:
                pass
            print("Opção inválida, tente novamente.")
        if alternativas[user_ans - 1] == correta:
            print("✔ CORRETA!")
            score += 1
        else:
            print(f"✘ ERRADA — Resposta certa: {correta}")

    print("\n===== FIM DO JOGO =====")
    print(f"Você acertou {score} de {len(questions)} perguntas.\n")

if __name__ == "__main__":
    run_quiz()


   