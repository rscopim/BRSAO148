senha_correta = "segredo"
tentativas = 0  # Contador de tentativas

while True:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Senha correta! Acesso concedido.")
        break
    elif tentativas == 3:
        print("Número máximo de tentativas atingido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")