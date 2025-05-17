import random
import string

def gerar_senha(tamanho):
    """
    Gera uma senha aleatória com letras, números e caracteres especiais.
    
    Parâmetros:
    tamanho (int): Número de caracteres da senha.
    
    Retorno:
    str: Senha gerada aleatoriamente.
    """
    # Define o conjunto de caracteres que podem estar na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera uma senha escolhendo caracteres aleatórios
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

# Solicita ao usuário o tamanho da senha
tamanho = int(input("Digite o tamanho da senha desejada: "))

# Exibe a senha gerada
print(f"Sua senha gerada é: {gerar_senha(tamanho)}")