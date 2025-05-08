def eh_bissexto(ano):
    """Verifica se um ano é bissexto conforme as regras do calendário Gregoriano.    
    Args:
        ano (int): O ano a ser verificado        
    Returns:
        bool: True se o ano for bissexto, False caso contrário
    """
    return (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)
def main():
    """Função principal que executa o programa de verificação de ano bissexto."""
    try:
        # Entrada de dados
        ano = int(input("Digite um ano: "))        
        # Processamento
        bissexto = eh_bissexto(ano)        
        # Saída de resultados
        if bissexto:
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")            
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")
if __name__ == "__main__":
    main()