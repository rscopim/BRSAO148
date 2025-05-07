'''
Crie um programa que armazene nomes de países e suas capitais em um dicionário. 
O usuário digita o nome do país e o programa mostra a capital correspondente.
'''
# Dicionário com países como chave e capitais como valor
paises_capitais = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Japão": "Tóquio",
    "Canadá": "Ottawa",
    "Alemanha": "Berlim",
    "Argentina": "Buenos Aires",
    "Estados Unidos": "Washington, D.C.",
    "Itália": "Roma",
    "Portugal": "Lisboa",
    "Reino Unido": "Londres"
}

# Função que solicita dados do usuário
def solicita():
    # Pede o nome do país ao usuário e remove espaços em branco extras
    pais = input("Digite o nome de um país (ou deixe vazio): ").strip()
    # Pede o nome da capital ao usuário e remove espaços em branco extras
    capital = input("Digite o nome de uma capital (ou deixe vazio): ").strip()
    # Retorna os dois valores 
    return pais, capital

# Função que procura a capital ou o país com base nos dados inseridos
def procura(pais, capital):
    if pais:
        # Se o usuário digitou o país, busca a capital no dicionário
        return paises_capitais.get(pais, "País não encontrado.")
    elif capital:
        # Se o usuário digitou a capital, faz uma busca invertida no dicionário
        for p, c in paises_capitais.items():
            if c.lower() == capital.lower():  # Ignora maiúsculas/minúsculas
                return f"A capital {capital} pertence ao país: {p}"
        return "Capital não encontrada."
    else:
        # Se nenhum valor foi informado
        return "Nenhum valor foi informado."

# Execução do programa 

# Chama a função de solicitação e armazena os dados
pais, capital = solicita()

# Chama a função de busca com os dados fornecidos e imprime o resultado
print(procura(pais,capital))