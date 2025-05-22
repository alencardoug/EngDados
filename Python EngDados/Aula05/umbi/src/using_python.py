# processamento_temperaturas.py

"""
Este script processa um arquivo TXT contendo medições de temperatura por estação meteorológica.
Ele realiza a análise de grandes volumes de dados e retorna, para cada estação:
- Temperatura mínima registrada
- Temperatura máxima registrada
- Temperatura média

As informações são lidas de um arquivo delimitado por ponto e vírgula (;), e o processamento
utiliza dicionários com valores padrão e contadores automáticos para eficiência.

A saída final é formatada no padrão: "EstacaoX: min/média/max".

------------------------------------------------------------
Funções disponíveis:

- processar_temperaturas(path_do_txt: str) -> dict:
    Lê o arquivo especificado, processa os dados e retorna um dicionário com os valores
    mínimos, médios e máximos por estação, formatados como strings.

Bloco principal:
    Executa o processamento completo medindo o tempo de execução e exibindo os resultados.
------------------------------------------------------------

Dependências externas:
- tqdm (instale com `poetry add tqdm` ou `pip install tqdm`)
- Instalado versão tqdm 4.67.1
"""


# ========================
# IMPORTAÇÕES DE BIBLIOTECAS
# ========================

# Importa o leitor de arquivos CSV
from csv import reader

# Importa tipos especiais de dicionários da biblioteca collections
from collections import defaultdict, Counter

# tqdm exibe uma barra de progresso durante loops demorados
from tqdm import tqdm

# Módulo para medir o tempo de execução
import time


# ========================
# CONSTANTE DE CONTROLE
# ========================

# Número total de linhas esperadas no arquivo.
# O underline (_) melhora a legibilidade, não afeta o valor.
NUMERO_DE_LINHAS = 10_000_000


# ========================
# FUNÇÃO PRINCIPAL DE PROCESSAMENTO
# ========================

def processar_temperaturas(path_do_txt):
    """
    Lê um arquivo TXT com temperaturas e calcula para cada estação:
    - temperatura mínima
    - temperatura máxima
    - temperatura média
    """

    # defaultdict com valor inicial infinito positivo para encontrar mínimos
    minimas = defaultdict(lambda: float('inf'))

    # defaultdict com valor inicial infinito negativo para encontrar máximos
    maximas = defaultdict(lambda: float('-inf'))

    # defaultdict com valor inicial 0.0 para somar temperaturas por estação
    somas = defaultdict(float)

    # Counter para contar quantas vezes cada estação aparece
    medicoes = Counter()

    # Abre o arquivo CSV em modo leitura
    with open(path_do_txt, 'r') as file:
        # Cria o leitor CSV, assumindo que os campos são separados por ponto e vírgula
        _reader = reader(file, delimiter=';')

        # Loop com barra de progresso. Ideal para arquivos grandes.
        for row in tqdm(_reader, total=NUMERO_DE_LINHAS, desc="Processando"):
            # Converte os valores da linha para tipos apropriados
            nome_da_station = str(row[0])
            temperatura = float(row[1])

            # Atualiza o contador de medições da estação
            medicoes.update([nome_da_station])

            # Atualiza o valor mínimo se a nova temperatura for menor
            minimas[nome_da_station] = min(minimas[nome_da_station], temperatura)

            # Atualiza o valor máximo se a nova temperatura for maior
            maximas[nome_da_station] = max(maximas[nome_da_station], temperatura)

            # Soma a temperatura para cálculo da média depois
            somas[nome_da_station] += temperatura

    print("Dados carregados. Calculando estatísticas...")

    # Armazena os resultados por estação: (mínima, média, máxima)
    results = {}

    for station, qtd_medicoes in medicoes.items():
        mean_temp = somas[station] / qtd_medicoes
        results[station] = (minimas[station], mean_temp, maximas[station])

    print("Estatística calculada. Ordenando...")

    # Ordena os resultados alfabeticamente pelo nome da estação
    sorted_results = dict(sorted(results.items()))

    # Formata os resultados para exibição: 00.0/00.0/00.0
    formatted_results = {
        station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}"
        for station, (min_temp, mean_temp, max_temp) in sorted_results.items()
    }

    return formatted_results


# ========================
# BLOCO PRINCIPAL
# ========================

if __name__ == "__main__":
    # Caminho para o arquivo de dados (pode ser alterado conforme necessário)
    path_do_txt = "data/measurements.txt"

    print("Iniciando o processamento do arquivo.")
    start_time = time.time()  # Marca o tempo de início

    # Executa o processamento das temperaturas
    resultados = processar_temperaturas(path_do_txt)

    end_time = time.time()  # Marca o tempo de término

    # Exibe os resultados formatados no terminal
    for station, metrics in resultados.items():
        print(station, metrics, sep=': ')

    # Informa o tempo total gasto no processamento
    print(f"\nProcessamento concluído em {end_time - start_time:.2f} segundos.")
