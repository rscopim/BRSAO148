import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados

# Nome do arquivo de log a ser analisado
arquivo = "logs_treinamento.csv"

try:
    # Tenta ler o arquivo CSV e armazená-lo em um DataFrame
    df = pd.read_csv(arquivo)

    # Verifica se a coluna 'tempo_execucao' está presente no arquivo
    if 'tempo_execucao' not in df.columns:
        raise ValueError("A coluna 'tempo_execucao' não foi encontrada no arquivo.")

    # Calcula a média do tempo de execução
    media = df['tempo_execucao'].mean()

    # Calcula o desvio padrão do tempo de execução
    desvio_padrao = df['tempo_execucao'].std()

    # Exibe os resultados formatados para duas casas decimais
    print(f"Média do tempo de execução: {media:.2f}")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")

# Captura erro caso o arquivo não seja encontrado
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")

# Captura erro caso a coluna esperada não esteja presente
except ValueError as e:
    print(f"Erro: {e}")

# Captura qualquer outro erro inesperado
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
