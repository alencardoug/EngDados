Pyenv, PIP, VENV, PIPX, Poetry
---
*Como criar estrutura de projeto de forma isolada e profissional*
# Pyenv
Instalar (ver vídeo do Jornada)
- Abrir Git Bash
- pyenv --version
- ls e cd pasta/ (para navegar) 
- mkdir nomedoprojeto (para criar pasta(s) projeto(s))
- rmdir nomedoprojeto/ (para remover pasta vazia se precisar)
- rm -r nomedoprojeto/ (para remover pasta se precisar)
- pyenv versions (talvez mostre nada, precisa instalar as versões do pyenv)
- pyenv install 3.12.1
- pyenv install 3.11.5
- pyenv version (vai mostrar todas versões instaladas)
- clear

**Configurando**
- pyenv global 3.12.1 (sempre que criar um projeto, vai ser com esta versão mais recente, mas precisa configurar )
- cd projeto/
- pyenv local 3.12.1 (configurado localmente, cria um arquivo .python-version na pasta do projeto)

# PIP
Faz a gestão de dependencias: baixando do pypi.org
- pip list
- pip uninstall pandas (biblioteca por biblioteca)

**Desinstalando várias bibliotecas (executar nesta ordem)**
- pip freeze
- pip freeze | grep -v "^-e" | xargs pip uninstall -y
- pip list

**Instalando bibliotecas distintas em cada projeto (venv)**
- cd pasta/ (para navegar)
- python -m venv .venv (usando python e o módulo do python venv, com nome .venv, e cria o ambiente virtual)
- ls -al (mostra a pasta e arquivo criado)
- source .venv/Scripts/activate (entrar no ambiente virtual)
- clear (e vai ver que está no ambiente virtual, mostrado pelo .venv)
- pip install pandas (instalar cada biblioteca necessária)
- deactivate (sair do venv)
- cd .. (sair da projeto)

# Pipx
- pip com mais atualizações, novidades, bibliotecas novas.
- Consegue criar ambiente virtuais por usuário.
- Única biblioteca a ser instalada globalmente, além do pip.
- *Gabarito*: argcomplete, click, colorama, packaging, pip, pipx, platformdirs, setuptools, userpath

**Executar:**
- pipx install poetry (criar globalmente, na máquina, pra este usuário)
- pipx install ipython
- python -i (abre o python para ser executado, mas interface uniforme)
- print('hello world!')
- exit()
- ipython -i (abre o ipython para ser executado, interface mais intuitiva)
- print('hello world')
- exit()

# Poetry
*tem por objetivo tornar mais fácil a gestão de dependencias e pacotes* - python-poetry.org

**Executando**
- poetry config virtualenvs.in-project true (iniciar poetry, habilitando que controle o projeto)
- poetry new nomedoprojeto (e cria a pasta do projeto, com readme, pasta de teste, pasta principal, e versões pyproject)
- cd pasta/
- pyenv local 3.12.1 (para instalar bibliotecas localmente)
- poetry env use 3.12.1 (criou a pasta do venv, e entra no venv)
- poetry add django (adicionar a biblioteca django)
- code . (entra no código, abre o vscode)
- (no vscode, terminal) poetry shell
- (no vscode, terminal) pip freeze
- (no vscode, terminal) poetry remove django (e remove junto as dependencias da biblioteca django)
