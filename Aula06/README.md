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

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
print(produtos_entregues)

# Parei em 29:00

