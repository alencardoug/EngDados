# GitHub CLI – Fluxo Completo de Pull Request e Merge

> **Objetivo**  
> Executar **todo** o ciclo de _feature → Pull Request → merge_ **sem sair do terminal**, usando apenas o [GitHub CLI (`gh`)](https://cli.github.com).

---

## Índice

1. [Pré-requisitos](#pré-requisitos)  
2. [Criar a branch e abrir o Pull Request](#criar-a-branch-e-abrir-o-pull-request)  
3. [Acompanhar o Pull Request](#acompanhar-o-pull-request)  
4. [Fazer o merge pelo CLI](#fazer-o-merge-pelo-cli)  
5. [Limpeza pós-merge](#limpeza-pós-merge)  
6. [Checklist rápido](#checklist-rápido)
7. [Após a requisição até o merge](#requisicao-merge)

---

### 1. Pré-requisitos

```bash
# macOS / Linux (Homebrew)
brew install gh

# Windows (winget)
winget install --id GitHub.cli

# Login (apenas na primeira vez)
gh auth login          # escolha: GitHub.com → SSH → Abrir no navegador
```

### 2. [Criar a branch e abrir o Pull Request](#criar-a-branch-e-abrir-o-pull-request)  

```bash
# 1 — criar ou mudar para a branch
git switch -c feature/login

# 2 — commits normais…
git push -u origin feature/login

# 3 — abrir o PR (modo interativo)
gh pr create

# ↳ modo “sem perguntas”
gh pr create \
  --base main \
  --head feature/login \
  --title "Tela de login" \
  --body  "Implementa OAuth2 e testes" \
  --label "frontend,backend" \
  --draft
```

- Dica: gh pr create --help exibe todas as opções (revisores, projeto, etc.).

### 3. [Acompanhar o Pull Request](#acompanhar-o-pull-request)  

```bash
# visão geral dos PRs (criados, revisados, etc.)
gh pr status

# detalhes do PR da branch atual
gh pr view            # --web abre no navegador

# resultados do CI / checks
gh pr checks
```

### 4. [Fazer o merge pelo CLI](#fazer-o-merge-pelo-cli)  

| Estratégia   | Flag principal | Descrição                                         |
|--------------|----------------|---------------------------------------------------|
| Merge normal | `--merge`      | Mantém todos os commits                           |
| Squash       | `--squash`     | Compacta tudo em um único commit                  |
| Rebase       | `--rebase`     | Reescreve commits no topo da _base_               |

```bash
# merge imediato, squash e remoção da branch
gh pr merge --squash --delete-branch

# habilitar AUTO-MERGE (entra na fila → conclui quando CI + reviews OK)
gh pr merge --auto           # herda a estratégia padrão do repositório

# merge como admin (ignora checks, requer permissão)
gh pr merge --admin --merge
```

Opções úteis:
- --delete-branch → remove a branch local e remota após o merge
- --match-head-commit <SHA> → falha se alguém fez force-push depois da revisão
- --body / --subject → edita a mensagem do commit de merge (quando existir)

### 5. [Limpeza pós-merge](#limpeza-pós-merge)  

Caso não tenha usado --delete-branch:

```bash
git switch main
git pull --ff-only
git branch -d feature/login      # remove branch local
git fetch --prune origin         # limpa referência remota obsoleta
```

6. [Checklist rápido](#checklist-rápido)

```bash
1. git switch -c minha-feature
2. <commits> → git push -u origin minha-feature
3. gh pr create
4. gh pr status / gh pr checks  (aguarde “✔”)
5. gh pr merge --squash --delete-branch
6. (Opcional) limpar branch local se não usou --delete-branch
```

Pronto! Com estes comandos você realiza todo o fluxo de Pull Request e merge diretamente no terminal.

### 7. [Após a requisição ao merge](#requisicao-merge)

Uma vez sincronizado o main, precisaremos iniciar um novo desenvolvimento. Esta sequencia permite criar branch, entrar, criar o arquivo.py, acessar, descrever com #, salvar, sincronizar ao git, sincronizar ao github, fazer pull request, mergear e uma vez finalizado o projeto, limpar os branchs tanto do remoto quanto do local.

```bash
git checkout -b ex05
touch ex05.py
code ex05.py
```

```python
# Iniciando o desenvolvimento ex05.py
```
- ctrl + s

```bash
git add ex05.py
git commit -m "criado branch ex05 e criado arquivo ex05.py"
git push -u origin ex05
gh pr create
gh pr merge --squash
```

- uma vez finalizado o desenvolvimento, substituir adicionando --delete-branch:
```bash
gh pr merge --squash --delete-branch
```