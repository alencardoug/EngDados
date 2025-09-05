Boas práticas.
def nome_da_funcao
função, por boa prática, é minúsculo.

1ª letra maiúscula, somente Classes.

Para projetos, nas boas práticas, usar PEP8.
É importante configurar automação que executa rotina de fazer avaliação de código por meio de programas.
Exemplo dado de bibliotecas usadas: black, isort, flake8 com plugin do bugver.
Estas são bibliotecas para a formatação.

codigos utilizados:
ls
cd
mkdir
code .
Depois criou o repositorio, copiou todos codigos da lista de codigos para criar repositorio do github, e executou  na pasta.

Copiou/colou um codigo que precisa de verificação da formatação.

#Sequencia de execuções feitas:
pyenv local 3.11.5 #Para criar ambiente virtual.
poetry init #Para gerenciar bibliotecas
poetry use 3.11.5
poetry shell
poetry add flake8

#O flake8 verifica se as linhas estão nas regras definidas.
poetry run flake8 main.py #Para evitar que ele leia todo o venv, e foque no main.py

#Dicas serão exibidas no terminal para evidenciar o que fazer.
#Dá dicas, sem tocar no código.
#Enquanto o black, altera seu código.

poetry add black
poetry run black main.py

#E black arruma pra você.
#Pra resolver e deixar os dois com as mesa regras:
#Criar arquivo com nome .flake8
#Colar  texto

ˋˋˋbash
[flake8]
max-line-length = 89
extend-ignore = E203,E701
ˋˋˋ
#Vai ignorar estas 2 regras E203,E701.

poetry remove black #Por causa de conflito
poetry remove flake8 #Por causa de conflito
poetry add blue #Ele já vem com black e flake8
poetry run blue ,
poetry run flake8 main.py
poetry run isort main.py

#Para não criar confusão na sequencia de execução flake8, black e isort.
#Sem configurar, um altera o outro.
#Para evitar:
#Dentro do pyproject.toml, definir que quem manda é o isort, adicionar no final:
ˋˋˋbash
[tool.isort]
profile = "black"

[tool.taskipy.tasks]
format = """
isort main.py
black main.py
flake8 main,py
"""
ˋˋˋ
Este main.py está se aplicando somente ao main.py, o que é uma limitação, errado.
#Criar .gitignore com conteúdo
ˋˋˋbash
.venv
ˋˋˋ

Então, para evitar que não façam commit sem executar esta cadeia de exemplo, é necessário fazer o pré-commit, que executa uma sequencia de códigos antes do commit. Nesse caso, o pré-commit forçará a execução do black, isort e flake8.

#Instalando o pré-commit
poetry add pre-commit #Do pre-commit.com

#Este está sendo executado para formatação, mas existem centenas de pré-commit úteis, por exemplo para segurança, tamanho de arquivo.
#Acessar do www.pre-commit.com/hooks.html
#Segurança, usar github.com/PyCQA/bandit, que previne uso de bibliotecas obsoletas, por exemplo, e cyber-security.
#Outro, commitizem #Padrão do commit seguindo o padrão que vc definiu.
#Outro é bugerben
#Gestão de arquivo binario: docker.
#Usar git e docker, executa em qualquer lugar. Git guarda o código, docker guarda seus programas.
#Se tiver o frontend e um banco postgree, que vão além do python, o docker é necessário.

#Então, para padronizar, dentro do criado arquivo com nome pre-commit-config.yaml:
ˋˋˋbash
- repo: https://github.com/pre-commit/pre-commit-hooks
   rev: v4.5.0
   hooks:
     - id: trailing-whitespace
       args: [--markdown-linebreak-ext=md]
     - id: end-of-file-fixer
     - id: check-yaml
     - id: check-toml
     - id: detect-private-key
     - id: check-added-large-files
- repo: https://github.com/psf/black-pre-commit-mirror
  rev:24.1.1
    - id: black
      language_version: python3.11
- repo: https://github.com/pycqa/isort
  rev: 5.13.2
  hooks:
    - id: isort
      name: isort (python)
- repo: https://github.com/pycqa/flake8
  rev: 7.0.0
  hooks:
    - id: flake8
ˋˋˋ
#E então, executar:
poetry run pre-commit install

#Não está mostrando a pasta .git por configuração do VSCode.
#Para mostrar, entrar na config > config > Commonly used > Files:Exclude > **/.git e deletar.

#Após o pre-commit install, a pasta hooks dentro da .git foi criada.
#15 arquivos criados, que são os programas pre-commit.
#Após a instalação, precisa adicionar o pre-commit:

git add .pre-commit-config.yaml
git commit -m "pre commit adicionado"
#Pode não funcionar, então pedir pro chatgpt consertar e identação e codigos.
#Após o commit, ele executa todos os pre-commit

#Pode mostrar que o black falhou. Mas o arquivo foi alterado e consertado.
#Para enviar:

git add main.py
git commit -m "pre commit adicionado"

#Então funcionará.

#Sugerido instalar a biblioteca bandit (cybersecurity) e commitizen (padronizar commit).

#Entrar no ambiente virtual é importante para permitir executar black .
#Fora do ambiente virtual, precisa executar poetry run black .

#Vale versionar tudo. SQL, js, Dockerfile, criar pasta Create table e ter os scripts SQL salvos.

#Monorepo versus Multirepo
#Monorepo tem a vantagem de compartilhar funções, como ler_arquivo_s3(), salvar_arquivo_s3(), etc.

#Importante fazer typehint nas variaveis para facilitar a leitura, assim como isinstance para proteger o programa de quebra:

nome_aluno: str = "Luciano" #typehint

if isinstance (nome_aluno, str):
   nome_aluno_maiusculo = nome_aluno.upper()
   print(nome_aluno_maiusculo)
else:
   print("voce digitou uma classe errada, precisa ser str")

#Aula 06 finalizada.

#Aula 07 iniciada. 
#Funcoes: um dos principais benefícios é permitir a reutilização do código.
#Eficiência e produtividade para manter a entrega, mesmo com aumento de escopo.
#Função é metodologia e padrão. É também criação de KPIs.
#Exemplo: extrato do Excel, API, SQL; Transforma e Carrega em um DW, PostgreSQL, S3, Iceberg, DuckDB. Mas não interessa muito a tecnologia em si.
#No exemplo, é ter uma função modificável, de forma que alterar em uma, altere em tudo.

#Criar novo repositório.
#Estrutura da função: 

```
def nome_da_funcao():
    return funcao
```

#Funções precisam ser parametrizaveis. Que significa, em função de condições diferentes, se comporta de formas diferentes. 

#Exemplo:

```
valor_1 = 4
valor_2 = 6

valor_3 = valor_1 + valor_2
```

#Tornando isto uma função: 
```
def soma(valor_1:float, valor_2: float) -> float:
    valor_3 = valor_1 + valor_2
    return valor_3
```

#Boas práticas: 
```
def soma(valor_1_para_somar: float, valor_2_para_somar: float = 10) -> float:
    """
    Uma função simples de soma de valores do tipo float que retorna float.
    """
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma
```

#PS: A docstring (o que está entre """ """ aparece quando coloca o mouse em cima da função.

#Colocando valores padrões se parâmetro não for informado: valor_2_para_somar: float = 10. Este valor é substituído se for informado outro valor na parametrização da função.

#Sobre formas de declarar a função. É possível destas 2 formas, incluindo a vantagem: 

```
valor_1 = 4
valor_2 = 6
soma(valor_1, valor_2)
soma(valor_2_para_somar = valor_2, valor_1_para_somar = valor_1
```

#Exemplo sendo resolvido (Aula 07, 22:00)

#Arquivo csv criado: 
```
produto,price,entregue
cadeira,500,False
mesa,200,True
mouse,50,False
```

#Funcao para ler arquivo csv:
#Importante que a função with() abre e fecha o arquivo
```python
import csv

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]
    """
    Função que le um arquivo csv e retorna uma lista de dicionários 
    """
    lista = []
    with open(nome_do_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista
```

#Funcao para filtrar os produtos entregues+sequência de execução:
```
def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
   """
   Função que filtra produtos onde entrega = True
   """
   lista_com_produtos_filtrados = []
   for produto in lista:
      if produto.get("entregue") == "True":
         lista_com_produtos_filtrados.append(produto)
   return lista_com_produtos_filtrados
```

#Criar função somar_valores_dos_produtos

```
def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
   """
   Soma todos os produtos que estão na lista
   """
   valor_total = 0
   for produto in lista_com_produtos_filtrados:
      valor_total += int(produto.get("price"))
   return valor_total
```

#E então, criar um main.py para encapsular, conectar as funções. 

```
from etl import ler_csv, filtrar_produtos_nao_entregues, somar_valores_dos_produtos

path_arquivo = "vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)
print(valor_dos_produtos_entregues)
```



lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
print(produtos_entregues)

#Aula08
#Criar pasta vazia via terminal com cd ls mkdir cd clear
#Entrar no GitHub e new directory, mesmo nome da pasta. Copiar sequência de comando e jogar no terminal.
# Configurar:

pyenv local 3.11.5 #escolher versão do python
poetry init #criar o ambiente virtual
poetry shell #iniciar ambiente virtual
code . #iniciar vscode

#Criar .gitignore comendo .venv
#Sincronizar tudo com GitHub:

git add .
git commit -m "primeiro commit"
git push

#Verificar no GitHub se foi.
#Iniciando o desafio:
#A partir de uma API de vendas, criar um dashboard. Concatenar os dados recebidos via json. Carregar em csv ou parquet.
#Como serão lidos e carregados diferentes arquivos, primeiro será escolhida a ferramenta de processamento. opções citadas: pandas, polars, DuckDB, spark, dask. Foi escolhido o pandas, podendo refatorar pro DuckDB.
#Quanto a ferramenta de qualidade: Pydantic ou Pandera. Se for trabalhar com dataframe, sql: Pandera. Se linha a linha ou API, Pydantic.

#Se for usar ferramenta de processamento que contém dataframe (as 5 citadas) usar Pandera. Se não, como exemplo, usar fastapi, então usar Pydantic. Também é possível converter dataframe para estrutura de objeto.

#Definido usar Pandera, por usar o Pandas, então:
```terminal
poetry add Pandera pandas
```

#Python puro usa dicionários. Mas é uma estrutura primitiva que não funciona para BigData. Para desafios BigData, usar dataframe e ferramenta de processamento + qualidade.

#Neste treinamento, primeiro será tentado com dicionário (chave valor) e depois será resolvido via dataframe. Citado a importância de dominar funcionamento de dicionário, visto que há bancos que usam chave valor. há estruturas docker e CI tem toeml que usam chave valor. json usa chave valor. 

#Etapa primeira: criar fluxo no excalidraw.com com fluxo e sequência de resolução 

#Em seguida, criar módulos (os arquivos .py)

```
etl.py #contem a lógica, as funções
pipeline.py #vai chamar o pipeline
schema.py #validacao do dataframe
pasta dados #arquivos json
```

#Criada para data e colocados os 3 arquivos json.
#json: Java script object notation.
#É um arquivo de dicionário, chave: valor
#Dados usa dataframe, enquanto front e back usam json.
```json
[
   {
      "chave": "valor",
      "chave": número,
      "chave": "data"
   },
   {
      "chave": "valor",
      "chave": "valor",
      "chave": "valor"
   }
]
```

#Criado etl.py

#1.De o teste lógico para a função:
#Teste lógico que printa mostrando que funciona

```python
import pandas as pd
import os
import glob
#uma função de extract que le e consulta os json

pasta = 'data'
arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
df_list = [pd.read_json(arquivo) for arquivo in arquivo_json]
df_total = pd.concat(df_list, ignore_index=True)
print(df_total)
```

#2.De o teste lógico para a função local:

```python
import pandas as pd
import os
import glob
#uma função de extract que le e consulta os json

def extrair_dados(nome_pasta: str) -> pd.DataFrame:
   arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
   df_list = [pd.read_json(arquivo) for arquivo in arquivo_json]
   df_total = pd.concat(df_list, ignore_index=True)
   return df_total

if __name__ == "__main__":
   pasta = 'data'
   print(extrair_dados(nome_pasta=pasta))
#esse teste em if previne que, se esquecer de tirar esse teste, não vai quebrar o módulo.

```

#3.De o teste lógico para a função unitário:

etl.py
```python
import pandas as pd
import os
import glob
#uma função de extract que le e consulta os json

def extrair_dados(nome_pasta: str) -> pd.DataFrame:
   arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
   df_list = [pd.read_json(arquivo) for arquivo in arquivo_json]
   df_total = pd.concat(df_list, ignore_index=True)
   return df_total
```

etl_teste.py
```
if __name__ == "__main__":
   pasta = 'data'
   print(extrair_dados(nome_pasta=pasta))
#esse teste em if em arquivo separado garante o teste em módulo unitário.
#dunder names
```

#Mais uns função em etl.py

```python
#uma função que transforma: 

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
   df["Total"] = df["Quantidade"] * df["Venda"]
   return df

if __name__ == "__main__":
   pasta_argumento = 'data'
   data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
   print(calcular_kpi_de_total_de_vendas(data_frame))
```

#Para rodar o código:
```terminal
poetry run python etl.py
```

#Criando a ~função~ procedure para carregar dados:

```python
def carregar_dados(df: pd.DataFrame, format_saida: list):
   """
   parâmetro lista contendo "csv" e/ou "parquet"
   """
   for formato in format_saida:
      if formato == 'csc':
         df.to_csv("dados.csv", index=False)
      if formato == 'parquet':
         df.to_parquet("dados.parquet", index=False)

if __name__ == "__main__":
   pasta_argumento: str = 'data'
   data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
   data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
   formato_de_saida: list = ["csv", "parquet"]
   carregar_dados(data_frame_calculado, formato_de_saida)
```
#Vai dar erro pois é pandas + parquet.
#Para criar parquet com pandas:

```terminal
poetry add fastparquet
```

#Para rodar o código:
```terminal
poetry run python etl.py
```

#Como adequar para que um usuário execute via um pipeline.py
#toda a parte if __name__ até o fim será (apagada, e) migrada em 2 arquivos, etl.py e pipeline.py:

#etl.py
```python
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
   data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
   data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
   carregar_dados(data_frame_calculado, formato_de_saida)
```

#pipeline.py
```python
from etl import pipeline_calcular_kpi_de_vendas_consolidado

pasta_argumento: str = 'data'
formato_de_saida: list = ["csv"]

pipeline_calcular_kpi_de_vendas_consolidado(pasta_argumento, formato_de_saida)
```

#Necessário criar um arquivo __init__.py
#Pois (pipeline.py) requisita importação de parte (função, procedure) de outro módulo (etl.py).

#Executar:
```terminal
poetry run python pipeline.py
```

#git add
#git commit
#git push

#Finalizada aula 08 :)

#Aula 09: decoradores

#Na engenharia de dados, a eficiência, reusabilidade e confiabilidade do código são cruciais. Por isso trabalhamos com decoradores.
#Criar novo repositório.

#3 formas de testar um código:
#1. print()
#2. VS Code Debug
#3. Log via loguru 

#Para que serve o log:
#Serve para registrar todos os erros, indicados via código, da pipeline. Registra de forma automática e autônoma a hora e o erro, independente do horário ou da execução.

```terminal
poetry init
poetry shell
poetry add loguru
```

#Abaixo, onde deveria ter print para verificar os valores, tem registrador de log.

```python
from loguru import logger

logger.add("meu_app.log") # Criar o arquivo log

def somar(x, y):
   logger.info(x)
   logger.info(y)
   logger.info(f"você quer uma soma: {x + y}")
   return x + y

somar(2, 3)
somar(2, "3")
```

```terminal
poetry run python exemplo_001.py
```

#Na aula 09 do repositório, há exemplos dos loggers com {} e outros.
```python
from loguru import logger

logger.debug("um aviso para o desenvolvedor no futuro")
logger.info("informação importante no processo")
logger.warning("um aviso de que algo vai parar de funcionar no futuro")
logger.error("aconteceu uma falha")
logger.critical("aconteceu uma falha que aborta a aplicação")
logger.add("meu_log.log", level = "CRITICAL")
```

#Exemplo de uso, com log: 
```python
from loguru import logger

logger.add("meu_log.log", level="CRITICAL")
#este argumento level indica que eu só quero registrar os logs logger.critical

#A partir daqui até o fim, é ref1, referência reutilizada no código seguinte
def soma(x, y):
   try:
      soma = x + y
      logger.info(f"você digitou valores corretos, parabéns {soma}")
      return soma
   except:
      logger.critical("você tem que digitar valores corretos")

soma(2,3)
soma(2,7)
soma(2,"3")
```
#ele vai printar todos os loggers, mas só vai salvar o critical.

#no terminal:

```terminal
poetry shell
poetry run python exemplo_00.py
```

#Código de log na tela e log crítico no arquivo, com variáveis especiais.

```python
from loguru import logger
from sys import stderr

logger.add(
sink=stderr,
format="{time} <r>{level}</r> <g>{message}</g> {file},
level="INFO"
)

logger.add(
format="{time} {level} {message} {file},
level="CRITICAL"
)

#reutilizar ref1
```

#há diversas opções e vale explorar no chat GPT

# Parei em 24m aula 09
