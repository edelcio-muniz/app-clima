<!--
  Arquivo gerado automaticamente com base no histórico do projeto 'app-clima'.
  Contém os cards recomendados / criados desde o início da sessão: título, descrição,
  labels, milestone, status e links para issues/PRs quando aplicável.
-->

# app-clima — Cards iniciais do Project Kanban

Este arquivo lista os cards que representam o trabalho já realizado e o trabalho recomendado/pendente, organizado em seções por status (Done, In Progress, To Do / Backlog). Use-o como referência ao preencher o seu Kanban.

> Observações:
- Issues criadas automaticamente no GitHub: #1, #2, #3 (links fornecidos abaixo).
- Milestone: `v1.0.0` criada.

---

## Done

1. Título: Scaffold inicial do projeto (arquivos base)
   - Descrição: Criação de estrutura básica, `README.md`, `Dockerfile`, `docker-compose.yml`, `requirements.txt`, e scripts de demonstração/teste.
   - Labels: docs, infra
   - Milestone: v1.0.0
   - Status: Done
   - Links: repositório principal (branch `main`)

2. Título: Implementar API Flask básica
   - Descrição: Endpoint `/clima/<cidade>`, `/historico`, `/health` e persistência em MySQL (tabela `consultas_clima`).
   - Labels: enhancement, infra
   - Milestone: v1.0.0
   - Status: Done

3. Título: Docker + Docker Compose (web + MySQL)
   - Descrição: Dockerfile atualizado, configuração de `docker-compose.yml` para orquestrar web e db; make targets para `up`, `down`, `build`.
   - Labels: infra
   - Status: Done

4. Título: Testes de integração básicos
   - Descrição: `tests/test_api.py` com 7 testes de endpoints; execução via `make test` e scripts de demonstração (`scripts/demo.sh`).
   - Labels: test
   - Status: Done (7/7 testes passaram)

5. Título: Ajuste de dependências — `cryptography`
   - Descrição: Adição de `cryptography` ao `requirements.txt` para compatibilidade com MySQL 8 (caching_sha2_password).
   - Labels: infra
   - Status: Done

6. Título: Scripts auxiliares e automações iniciais
   - Descrição: `scripts/create-github-resources.sh`, `scripts/monitor-api-key.sh`, `scripts/test-basic.sh` e `Makefile` com alvos comuns.
   - Labels: infra, ci
   - Status: Done

---

## In Progress

1. Título: Criar Project / Kanban (configurado manualmente pelo usuário)
   - Descrição: Project criado pelo usuário; aguardando criação automática de colunas e movimentação de issues. Project URL: https://github.com/users/edelcio-muniz/projects/7
   - Labels: infra, docs
   - Status: In Progress (colunas criadas manualmente pelo usuário)

2. Título: Criar automações do Project
   - Descrição: Automations sugeridas (mover issues novas para Backlog, mover PRs com merge para Done, etc.).
   - Labels: infra
   - Status: In Progress / Pending (aguardando autorização para configurar via API)

---

## To Do / Backlog

1. Título: Adicionar CI básico (issues #1)
   - Descrição: Criar workflow GitHub Actions que instale dependências e execute checagens básicas (import/compile), além de rodar testes rápidos.
   - Labels: ci, enhancement
   - Issue: https://github.com/edelcio-muniz/app-clima/issues/1
   - Milestone: v1.0.0
   - Status: Backlog / To Do

2. Título: Configurar Kanban / Project (issues #2)
   - Descrição: Criar Project com colunas Backlog/To Do/In Progress/In Review/Done e adicionar issues iniciais.
   - Labels: infra, docs
   - Issue: https://github.com/edelcio-muniz/app-clima/issues/2
   - Status: Backlog (project criado manualmente; preencher com cards)

3. Título: Melhorar tratamento de erros da API (issues #3)
   - Descrição: Revisar e melhorar mensagens de erro, códigos HTTP e logs. Cobrir casos de validação e falhas de terceiros (OpenWeather / MySQL).
   - Labels: bug, enhancement
   - Issue: https://github.com/edelcio-muniz/app-clima/issues/3
   - Status: Backlog

4. Título: Migrar app-clima para minikube / Kubernetes (futuro)
   - Descrição: Gerar manifests k8s (Deployment, Service, ConfigMap/Secret para API key), preparar `k8s/` e `Makefile` targets para `minikube` — planejar como etapa posterior.
   - Labels: infra
   - Status: Backlog (Future)

5. Título: Melhorar cobertura de testes e lint
   - Descrição: Adicionar pytest, testes unitários, linting (flake8/ruff), e integrar ao CI.
   - Labels: test, ci
   - Status: Backlog

6. Título: Documentação de uso e deploy
   - Descrição: Completar `USAGE.md`, `COMMANDS.md` e adicionar exemplos de deploy para produção/local com variáveis de ambiente e secrets.
   - Labels: docs
   - Status: Backlog

---

## Como usar este arquivo

- Ao criar os cards no Project, copie o título e a descrição conforme acima e cole no novo card.
- Use as labels já criadas no repositório (`bug`, `enhancement`, `docs`, `ci`, `infra`, `test`).
- Se quiser que eu crie automaticamente os cards/associações (via API), gere um classic PAT com scopes `repo` e `project` e me passe confirmação — eu criarei cards para as issues listadas e para os itens do backlog.

---

## Exportar para CSV/JSON

Se preferir, posso exportar estes cards para `docs/project-cards.csv` ou `docs/project-cards.json` para facilitar importação/automação — quer que eu gere agora?

---

## ADICIONAIS (inserir novos cards manualmente abaixo)

Se você tem novos itens para adicionar ao Kanban, copie o template abaixo e preencha os campos; depois cole como novo card no Project ou adicione como nova issue e associe ao Project.

Template de card (preencha e cole no Kanban):

```
Título: <Título curto e padronizado, ex.: feature: adicionar X>
Descrição: <Descrição completa do que precisa ser feito>
Labels: <comma-separated, ex.: enhancement,infra>
Milestone: <opcional, ex.: v1.0.0>
Issue: <opcional, link para a issue relacionada>
Status: <Backlog | To Do | In Progress | In Review | Done>
```

Exemplo (cole abaixo do último item):

Título: feature: implementação do endpoint /clima/batch
Descrição: Criar endpoint que recebe lista de cidades e retorna resumo com caching e paralelismo controlado.
Labels: enhancement, infra
Milestone: v1.0.0
Issue: <coloque link se já criou a issue>
Status: Backlog

