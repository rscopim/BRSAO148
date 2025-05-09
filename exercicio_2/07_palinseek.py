palavra = input("Insira uma palavra ou uma frase: ")

# Remove espaços, hífens, vírgulas e acentos (simplificado)
palavra_formatada = palavra.replace(" ", "").replace("-", "").replace(",", "").replace("é", "e").lower()

palavra_invertida = palavra_formatada[::-1]

if palavra_formatada == palavra_invertida:
    print(f"A palavra/frase '{palavra}' é um palíndromo.")
else:
    print(f"A palavra/frase '{palavra}' não é um palíndromo.")