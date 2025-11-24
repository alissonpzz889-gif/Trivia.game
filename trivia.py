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

   