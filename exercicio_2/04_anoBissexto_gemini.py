# Solicita que o usuário digite um ano e converte a entrada para um número inteiro.
ano = int(input("Digite um ano: "))

# Verifica se o ano é um valor positivo.
if ano <= 0:
    # Se o ano não for positivo, exibe uma mensagem de erro.
    print("Por favor, digite um ano positivo.")
else:
    # Se o ano for positivo, prossegue com a verificação de ano bissexto.
    # Um ano é bissexto se for divisível por 4...
    if (ano % 4 == 0) and (
        # ...e não for divisível por 100...
        (ano % 100 != 0) or
        # ...a menos que também seja divisível por 400.
        (ano % 400 == 0)
    ):
        # Se a condição de ano bissexto for verdadeira, exibe a mensagem correspondente.
        print(f"O ano {ano} é bissexto.")
    else:
        # Se a condição de ano bissexto for falsa, exibe a mensagem correspondente.
        print(f"O ano {ano} não é bissexto.")