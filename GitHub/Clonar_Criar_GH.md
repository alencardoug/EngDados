# Clonar do GitHub e deletar arquivo no GitHub via VS Code

### Foram executados os códigos a seguir:
```bash
python --version
ssh -T git@github.com
git clone git@github.com:alencardoug/EngDados.git
cd EngDados
cd 'Python EngDados'
cd 'Aula 01'
git add Deletar
# Deletei o arquivo Deletar
git add Deletar
git status
git commit -m "Deletei o arquivo Deletar"
git push
```

Com isso, foi verificado/executado:
- Se python está instalado, e qual versão
- Se Github está conectado e authenticado via ssh
- Clonar repositório EngDados
- Navegar por pasta
- Adicionar arquivo ao git
- Deletar o arquivo via interface gráfica
- Adicionar arquivo ao git (que foi deletado)
- Verificar status, se deleção está no staged
- Comitar deleção
- Sincronizar local ao remoto via push

# Criar repositório do zero em ambos local e remoto

Abrir o bash e executar:
```bash
ls|cd|mkdir|clear
#Criar repositório no githu de preferencia com o mesmo nome
#Copiar as 7 linhas de comando para criar um novo repositório; sugerido pelo github:
echo "# aula-2_bootcamp" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:lvgalvao/aula02_bootcamp.git
git push -u origin main
```

O primeiro comando tira um print no terminal e salva no arquivo readme. 
Os outros comando, iniciam a sincronização.
