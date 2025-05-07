'''
Crie um programa 
que receba um número do usuário e diga se ele é positivo, negativo ou igual a zero.
'''
# solicita ao usuario o valor em  numeros positivos e negativos
def solicitacao():
    return float(input('Coloque um número, positivo ou negativo: '))

# ira ser a segunda parte que depois que o primeiro for armazenado em uma variavel essa função vai receber o valor
def diga_oque_eh(numero):
    if numero > 0:
        return "Seu valor é positivo"
    elif numero == 0:
        return "Seu valor é igual a zero"
    else:
        return "Seu valor é negativo"

# a variavel recebe a solicitação do usuario
numero = solicitacao()
#printa o resultado
print(diga_oque_eh(numero))