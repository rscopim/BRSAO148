# Solicita ao usuário que digite um ano e converte a entrada para inteiro
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto de acordo com as regras:
# 1. O ano deve ser divisível por 4
# 2. E não pode ser divisível por 100, a menos que também seja divisível por 400
if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
    # Se a condição for verdadeira, imprime que o ano é bissexto
    print(f"O ano {ano} é bissexto.")
else:
    # Se a condição for falsa, imprime que o ano não é bissexto
    print(f"O ano {ano} não é bissexto.")