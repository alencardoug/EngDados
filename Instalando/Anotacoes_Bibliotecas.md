Pyenv, PIP, VENV, PIPX, Poetry
---
*Como criar estrutura de projeto de forma isolada e profissional*
# Pyenv
Instalar (ver vídeo do Jornada)
- Abrir Git Bash
- pyenv --version
- ls e cd pasta/ (para navegar) 
- mkdir nomedoprojeto (para criar pasta(s) projeto(s))
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
- 
