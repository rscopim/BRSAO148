import os
import random
import time
import shutil

# Caracteres usados na "chuva"
caracteres = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&@"

# Obtém o tamanho da tela
largura, altura = shutil.get_terminal_size()

# Lista para armazenar a posição Y de cada coluna
posicoes = [0] * largura

try:
    while True:
        # Para cada coluna
        for i in range(largura):
            # Escolhe um caractere aleatório
            char = random.choice(caracteres)
            
            # Move o cursor para a posição e imprime o caractere
            print(f"\033[1;32m\033[{posicoes[i]};{i}H{char}\033[0m", end='')

            # Atualiza a posição Y da coluna, com chance de resetar
            if random.random() > 0.98:
                posicoes[i] = 0
            else:
                posicoes[i] = posicoes[i] + 1 if posicoes[i] < altura else 0

        time.sleep(0.02)

except KeyboardInterrupt:
    # Quando Ctrl+C for pressionado, limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Finalizado pelo usuário.")