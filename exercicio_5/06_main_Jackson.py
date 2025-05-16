def idade_valida(idade):
    """
    Função que verifica se a idade é válida.
    Retorna True se idade for entre 0 e 120 (inclusive), caso contrário False.
    """
    return 0 <= idade <= 120

def main():
    nome = input("Digite seu nome: ").strip()

    try:
        idade = int(input("Digite sua idade: "))

        if not idade_valida(idade):
            print("⚠ Idade inválida. Por favor, insira uma idade entre 0 e 120 anos.")
            return

        print(f"Olá, {nome}! Você tem {idade} anos.")
        print("🎉 Parabéns por estar utilizando o Python, na aula do professor Ricardo da Escola da Nuvem!")

    except ValueError:
        print("⚠ Entrada inválida. A idade deve ser um número inteiro.")

if __name__ == "__main__":
    main()