# Comandos usados no projeto "app-clima"

Este arquivo lista, na ordem de criação/execução/testes, todos os comandos usados no projeto, com breve explicação, quando usar e link para a documentação oficial.

---

## 1) Preparação do ambiente (criação do projeto)

- Criar virtualenv (opcional localmente)
  - Comando:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
  - Para que serve: Isolar dependências Python localmente.
  - Quando usar: Desenvolvimento local, para evitar poluir o sistema.
  - Docs: https://docs.python.org/3/library/venv.html

---

## 2) Dependências

- Instalar dependências (local)
  - Comando:
    ```bash
    python -m pip install -r requirements.txt
    ```
  - Para que serve: Instala Flask, PyMySQL, cryptography, etc.
  - Quando usar: Antes de executar a aplicação localmente sem Docker.
  - Docs: https://pip.pypa.io/

---

## 3) Docker / Docker Compose (criar e executar containers)

- Subir containers (recomendado: usar `docker compose` moderno)
  - Comando:
    ```bash
    # build + start em background
    docker compose up -d --build
    # (alternativa legada)
    docker-compose up -d --build
    ```
  - Para que serve: Constrói imagens e sobe os serviços `web` (Flask) e `db` (MySQL).
  - Quando usar: Deploy local com containers, desenvolvimento com dependências idênticas ao servidor.
  - Docs: https://docs.docker.com/compose/

- Parar e remover containers/ network
  - Comando:
    ```bash
    docker compose down
    # remover volumes (apagar banco):
    docker compose down -v
    ```
  - Para que serve: Limpando o ambiente de containers.
  - Quando usar: Parar o ambiente de dev ou limpar dados do DB.
  - Docs: https://docs.docker.com/compose/reference/down/

- Ver containers ativos
  - Comando:
    ```bash
    docker compose ps
    ```
  - Para que serve: Conferir status dos serviços.
  - Docs: https://docs.docker.com/engine/reference/commandline/ps/

- Visualizar logs
  - Comando:
    ```bash
    docker compose logs -f web
    docker compose logs -f db
    ```
  - Para que serve: Debug e acompanhamento em tempo real.
  - Docs: https://docs.docker.com/compose/reference/logs/

- Entrar no container (debug)
  - Comando:
    ```bash
    docker exec -it api_clima bash
    docker exec -it mysql_clima bash
    ```
  - Para que serve: Inspecionar filesystem, executar comandos, checar connectivity.
  - Quando usar: Troubleshooting avançado.
  - Docs: https://docs.docker.com/engine/reference/commandline/exec/

---

## 4) Comandos da aplicação (diretamente no host)

- Rodar a aplicação sem Docker (apenas para desenvolvimento local)
  - Comando:
    ```bash
    python app.py
    ```
  - Para que serve: Iniciar servidor Flask (modo dev, debug=True).
  - Observação: O server roda com debug e não é indicado para produção.

- Testar endpoints com curl
  - Comandos principais:
    ```bash
    curl http://localhost:5000/
    curl http://localhost:5000/health
    curl "http://localhost:5000/clima/London"
    curl "http://localhost:5000/historico?limit=5"
    ```
  - Para que serve: Requisições simples para validar endpoints.

---

## 5) Scripts do projeto (incluídos no repositório)

- `./demo.sh` - Demonstração rápida dos endpoints
  - Para que serve: Coletar respostas de `/`, `/health` e `/historico`.
  - Uso: `./demo.sh`

- `./test-basic.sh` - Testes básicos (sem necessidade de API key)
  - Para que serve: Testar endpoints básicos e checar retorno quando API Key não está ativa.
  - Uso: `./test-basic.sh`

- `./monitor-api-key.sh` - Monitor que checa ativação da API Key
  - Para que serve: Verifica a cada 30s se a chave do OpenWeather foi ativada.
  - Uso: `./monitor-api-key.sh`

- `python test-api.py` - Suite de testes que realiza várias consultas (precisa da API Key ativa para clima)
  - Para que serve: Testes automatizados de integração via HTTP.
  - Uso: `python test-api.py`

---

## 6) Git / GitHub (comandos úteis antes do push)

- Inicializar repositório e commit inicial
  - Comandos:
    ```bash
    git init
    git add .
    git commit -m "Initial commit: app-clima"
    git remote add origin git@github.com:USERNAME/REPO.git
    git push -u origin main
    ```
  - Para que serve: Versionamento e envio ao GitHub.
  - Docs: https://git-scm.com/docs/git

- Criar branch, abrir PR e trabalhar com GitHub Projects
  - Comandos básicos:
    ```bash
    git checkout -b feat/add-monitor
    git add . && git commit -m "Add monitor script"
    git push origin feat/add-monitor
    ```
  - Para que serve: Fluxo de desenvolvimento com branches.

---

## 7) Operações de manutenção (opcionais)

- Limpar imagens e volumes Docker localmente
  - Comandos:
    ```bash
    docker image prune -af
    docker volume prune -f
    ```
  - Para que serve: Recuperar espaço em disco.
  - Docs: https://docs.docker.com/engine/reference/commandline/image_prune/

---

## 8) Links úteis de documentação

- Docker Compose: https://docs.docker.com/compose/
- Docker CLI: https://docs.docker.com/engine/reference/commandline/
- Flask: https://flask.palletsprojects.com/
- PyMySQL: https://pymysql.readthedocs.io/
- OpenWeatherMap API: https://openweathermap.org/api
- Git: https://git-scm.com/doc

---

