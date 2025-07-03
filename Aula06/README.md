Boas práticas.
def funcao
função, por boa prática, é minúsculo.

1ª letra maiúscula, somente Classes.

Para projetos, nas boas práticas, usar PEP8.
Rotina de fazer avaliação de código por meio de programas.
Exemplo dado de bibliotecas usadas: black, isort, flake8 com plugin do bugver.
Estas são bibliotecas de formatação.

codigos utilizados:
ls
cd
mkdir
code .
Depois criou o repositorio, copiou codigo a lista de codigos para criar repositorio do github, e executou  na pasta.

Copiou/colou um codigo a verificar a formatação.

#Sequencia de execuções feitas:
pyenv local 3.11.5 #Para criar ambiente virtual.
poetry init #Para gerenciar bibliotecas
poetry use 3.11.5
poetry shell
poetry add flake8

#O flake8 verifica se as linhas estão nas regras definidas.
poetry run flake8 main.py #Para evitar que ele leia todo o venv, e foque no main.py

#Dicas serão dadas para o que fazer.
#Dá dicas, sem tocar no código.
#Enquanto o black, altera seu código.

poetry add black
poetry run black main.py

#E ele arruma pra você.
#Pra resolver e deixar os dois com as mesa regras:
#Criar arquivo com nome .flake8
#Colar  texto

ˋˋˋbash
[flake8]
max-line-length = 89
extend-ignore = E203,E701 #Vai ignorar estas 2 regras.
ˋˋˋ

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
Este main.py está se aplicando somente ao main.py, o que é bem ruim.
#Criar .gitignore com conteúdo
ˋˋˋbash
.venv
ˋˋˋ

Então, para evitar que não façam commit sem executar esta cadeia de exemplo, é necessário fazer o pré-commit, que executa uma sequencia de códigos antes do commit. Nesse caso, o pré-commit forçará a execução do black, isort e flake8.

#Instalando o pré-commit
poetry add pre-commit #Do pre-commit.com

#Este está sendo executado para formatação, mas existem centenass de pré-commit úteis, por exemplo para segurança, tamanho de arquivo.
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

#Parei a aula 06 em 29:30
