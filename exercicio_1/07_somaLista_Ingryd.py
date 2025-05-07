'''
Crie um programa que contenha uma 
lista com números e calcule a soma total desses números usando um laço for.
'''
# função solicita valores
def solicitar_itens():
    #armazena os valores
    num = []
    # para cada numero na range 5 ele solicita o valor e armazena na lista
    for i in range(5):
        valor = int(input(f"Coloque o número ({i + 1}): "))
        num.append(valor)
    return num

# ele pega o valor lista e para cada elemento dele ele soma com o valor anterior
def somar(lista):
    total = 0
    for x in lista:
        total += x
    return total
# declara o valor lista que recebe a função de solicitar valores
lista = solicitar_itens()
# printa os valores
print(f"A soma total dos números é: {somar(lista)}")