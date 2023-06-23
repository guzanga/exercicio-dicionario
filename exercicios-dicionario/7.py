import random

def jogar_dado():
    return random.randint(1, 6)

jogadores = ["Jogador 1", "Jogador 2", "Jogador 3", "Jogador 4"]
resultados = {}

for jogador in jogadores:
    resultado = jogar_dado()
    resultados[jogador] = resultado

for jogador, resultado in resultados.items():
    print(f"{jogador} tirou: {resultado}")