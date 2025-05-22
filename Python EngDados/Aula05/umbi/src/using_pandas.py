"""
Este script em Python processa grandes arquivos de dados (como .csv ou .txt com bilhões de linhas),
de forma eficiente usando:

- **Pandas** para manipulação de dados tabulares
- **Multiprocessing** para paralelizar o processamento de cada pedaço (chunk) de dados
- **tqdm** para exibir uma barra de progresso durante a leitura do arquivo

Funções:
- `process_chunk(chunk)`: Agrega dados por estação (mínimo, máximo e média da medida)
- `create_df_with_pandas(filename, total_linhas, chunksize)`: Lê o arquivo em pedaços e processa paralelamente

Resumo:
# Por que esse script é adequado para arquivos maiores que a memória RAM?
- Leitura em pedaços (chunksize): O pd.read_csv(..., chunksize=...) permite carregar só um trecho do arquivo por vez, evitando carregar tudo na memória.
- Processamento paralelo: Usa todos os núcleos da CPU para processar os pedaços simultaneamente.
- Concatenação final eficiente: Ao invés de acumular todas as linhas, ele faz agregações intermediárias e só junta os resultados resumidos.

Execução via terminal:
- Executado `python src/using_pandas.py`
- Falhou por faltar pandas. Executado `poetry add pandas`. Instalado pandas 2.2.3
- Funcionou.

"""

import pandas as pd  # Biblioteca para manipulação de dados tabulares
from multiprocessing import Pool, cpu_count  # Para paralelizar o processamento com todos os núcleos da CPU
from tqdm import tqdm  # Exibe barra de progresso durante o loop

# Define quantos núcleos usar com base na capacidade do computador
CONCURRENCY = cpu_count()

# Total estimado de linhas do arquivo
total_linhas = 1_000_000_000

# Define o tamanho de cada pedaço (chunk) lido do arquivo (100 milhões de linhas por vez)
chunksize = 100_000_000

# Caminho do arquivo a ser processado
filename = "data/measurements.txt"

def process_chunk(chunk):
    """
    Processa um pedaço (chunk) de dados.
    Agrupa por 'station' e calcula o mínimo, máximo e média da coluna 'measure'.
    """
    aggregated = chunk.groupby('station')['measure'].agg(['min', 'max', 'mean']).reset_index()
    return aggregated

def create_df_with_pandas(filename, total_linhas, chunksize=chunksize):
    """
    Lê o arquivo em pedaços e processa cada pedaço em paralelo usando multiprocessing.
    Junta os resultados finais agregando por estação.
    """
    # Calcula o número total de chunks necessários
    total_chunks = total_linhas // chunksize + (1 if total_linhas % chunksize else 0)
    results = []

    # Lê o arquivo em pedaços com Pandas
    with pd.read_csv(filename, sep=';', header=None, names=['station', 'measure'], chunksize=chunksize) as reader:
        # Cria um pool de processos paralelos
        with Pool(CONCURRENCY) as pool:
            for chunk in tqdm(reader, total=total_chunks, desc="Processando"):
                # Envia cada pedaço para ser processado de forma assíncrona
                result = pool.apply_async(process_chunk, (chunk,))
                results.append(result)

            # Aguarda os resultados finais de todos os chunks
            results = [result.get() for result in results]

    # Junta todos os DataFrames intermediários em um só
    final_df = pd.concat(results, ignore_index=True)

    # Agrega novamente por estação (caso haja dados de mesma estação em diferentes chunks)
    final_aggregated_df = final_df.groupby('station').agg({
        'min': 'min',
        'max': 'max',
        'mean': 'mean'
    }).reset_index().sort_values('station')

    return final_aggregated_df

if __name__ == "__main__":
    import time  # Usado para medir o tempo de execução

    print("Iniciando o processamento do arquivo.")
    start_time = time.time()

    # Chama a função principal para criar o DataFrame processado
    df = create_df_with_pandas(filename, total_linhas, chunksize)

    # Calcula quanto tempo levou
    took = time.time() - start_time

    # Exibe os primeiros resultados
    print(df.head())
    print(f"Processing took: {took:.2f} sec")
