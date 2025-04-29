# Estrutura sequencial
'''nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Cidade onde mora: ")
print("Olá", nome)
print("Você tem", idade, "anos")
print("E mora em", cidade)

#Estrutura de repetição
for i in range(5):
    print("Contar", i)

contar = 0
while contar < 5:
    print("Executar", contar)
    contar += 1'''

'''idade = int(input('Qual a sua idade? '))
if idade >= 18:
    print("Maior de idade")
elif idade <= 18:
    print("Menor de idade")
else:
    print("Idade inválida")'''

def busca (Lista, nome_procurado):
    for i in range(len(Lista)):
        if Lista[i] == nome_procurado:
            return i + 1
    return -1 

nomes = ['Geovanna', 'Ingryd', 'Alberto', 'Iolanda', 'Maria', 'Jackson', 'Evelyn', 'Janaina']
nome_procurado = input('Qual nome você quer procurar? ')
posicao = busca(nomes, nome_procurado)
if posicao != -1:
    print('O nome está na posição', posicao)
else:
    print('O nome não está na lista')