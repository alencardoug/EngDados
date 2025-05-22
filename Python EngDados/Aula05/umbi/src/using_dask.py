"""
Este script utiliza a biblioteca Dask para processar grandes volumes de dados em arquivos CSV ou TXT.
Dask permite o processamento de datasets que não cabem na memória RAM, executando operações de forma paralela
e "preguiçosa" (lazy), ou seja, o cálculo só ocorre quando necessário (com .compute()).

Objetivo: 
- Ler um arquivo com dados de medidas por estação
- Agrupar os dados por estação
- Calcular estatísticas como mínimo, máximo e média
- Exibir os dados ordenados por estação

Funções agregadas que podem ser utilizadas com Dask além de min e max:
- mean: média
- sum: soma
- count: contagem
- std: desvio padrão
- var: variância
- first / last: primeiro ou último valor
- nunique: número de valores únicos

Execução via terminal:
- Executado `python src/using_dask.py`
- Falhou por faltar dask. Executado `poetry add dask`. Instalado dask 2025.5.1
- Falhou por faltar pyarrow. Executado `poetry add pyarrow`. Instalado pyarrow 20.0.0
- Funcionou.
"""

import dask
import dask.dataframe as dd

def create_dask_df():
    # Ativa o modo de planejamento de consultas, útil para otimizações internas
    dask.config.set({'dataframe.query-planning': True})
    
    # Lê o arquivo CSV com separador ';', sem cabeçalho
    # Define manualmente os nomes das colunas
    df = dd.read_csv("data/measurements.txt", sep=";", header=None, names=["station", "measure"])
    
    # Agrupa por 'station' e define operações agregadas sobre a coluna 'measure'
    # Dask apenas define o grafo de tarefas aqui (não executa nada ainda)
    grouped_df = df.groupby("station")['measure'].agg(['max', 'min', 'mean']).reset_index()

    return grouped_df

if __name__ == "__main__":
    import time

    # Marca o início do tempo de execução
    start_time = time.time()

    # Cria o Dask DataFrame com as operações planejadas
    df = create_dask_df()
    
    # Executa o grafo de tarefas (leitura, agregação e ordenação)
    result_df = df.compute().sort_values("station")

    # Marca o fim do tempo de execução
    took = time.time() - start_time

    # Exibe os dados processados e o tempo que levou
    print(result_df)
    print(f"Dask Took: {took:.2f} sec")
