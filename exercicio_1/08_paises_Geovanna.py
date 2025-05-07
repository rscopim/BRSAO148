# Dicionário com países e suas capitais
paises_capitais = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "França": "Paris",
    "Estados Unidos": "Washington, D.C.",
    "Japão": "Tóquio",
    "Alemanha": "Berlim",
    "Itália": "Roma",
    "Canadá": "Ottawa",
    "Reino Unido": "Londres",
    "México": "Cidade do México"
}

# Solicita o nome do país ao usuário
pais = input("Digite o nome de um país: ")

# Verifica se o país está no dicionário e exibe a capital
if pais in paises_capitais:
    print(f"A capital de {pais} é {paises_capitais[pais]}.")
else:
    print("Desculpe, não encontrei a capital desse país.")