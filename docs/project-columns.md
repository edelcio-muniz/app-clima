# app-clima — Project Kanban: Colunas e dados completos

Este documento contém tudo que você precisa colar no campo README do Project ou consultar enquanto cria as colunas manualmente. Para cada coluna há: propósito, quando mover cards, exemplos de cards iniciais, checklists e automações sugeridas. Inclui também exemplos de comandos `gh api` (substitua {PROJECT_ID} e {COLUMN_ID} pelos valores reais).

---

## Visão geral

Nome do Project (sugestão): app-clima Kanban

Colunas padrão e ordem recomendada:

- Backlog
- To Do
- In Progress
- In Review
- Done

---

## 1) Backlog

- Propósito:
  - Guardar ideias, requests, melhorias e bugs que ainda não foram priorizados.
  - Local para triagem regular (ex.: semanalmente) para mover itens para `To Do`.

- Quando mover para outra coluna:
  - Mover para `To Do` quando o item for priorizado e planejado para o próximo ciclo.

- Campos/convenções dos cards:
  - Título conciso (ex.: "feature: histórico de consultas por usuário").
  - Labels: `enhancement` / `bug` / `infra` / `docs` / etc.
  - Milestone opcional (ex.: `v1.0.0`).

- Exemplos de cards iniciais:
  - "Adicionar CI básico (import/compile)" — label: `ci`, milestone: `v1.0.0`.
  - "Documentar endpoints principais" — label: `docs`.

- Automations sugeridas:
  - Ao adicionar label `triage` -> mover para Backlog.

---

## 2) To Do

- Propósito:
  - Itens priorizados e prontos para iniciar (próximo ciclo).

- Quando mover para outra coluna:
  - Mover para `In Progress` assim que alguém começar a trabalhar.

- Campos/convenções dos cards:
  - Atribuir responsável (assignee) quando iniciar o trabalho.
  - Estimativa opcional no título ou nas descrições (p.ex. "(2h)").

- Exemplos de cards iniciais:
  - "Implementar endpoint /clima/{cidade} com caching" — label: `enhancement`.

- Automations sugeridas:
  - Ao adicionar label `ready` -> mover para To Do.

---

## 3) In Progress

- Propósito:
  - Tarefas ativamente sendo implementadas.

- Quando mover para outra coluna:
  - Mover para `In Review` quando abrir o Pull Request (PR) associado.

- Campos/convenções dos cards:
  - Link para branch/PR no próprio card.
  - Comentários de progresso curtos (ex.: "Implementando testes unitários").

- Checklist sugerida no card (PR / Pull request):
  - [ ] Código implementado
  - [ ] Testes básicos adicionados
  - [ ] Documentação atualizada (se aplicável)

- Automations sugeridas:
  - Ao abrir PR com label `ready-for-review` -> mover card para `In Review`.

---

## 4) In Review

- Propósito:
  - Revisão de código, validação do comportamento e aprovação de PRs.

- Quando mover para outra coluna:
  - Mover para `Done` após o merge e verificação pós-merge.
  - Se revisão falhar, mover de volta para `In Progress` com comentários.

- Checklist sugerida para revisão:
  - [ ] Código atende aos requisitos
  - [ ] Testes passaram
  - [ ] Nenhum dado sensível foi adicionado
  - [ ] Logs e mensagens de erro OK

- Automations sugeridas:
  - Ao merge do PR -> mover card para `Done` (automação possível via GitHub Projects / Actions).

---

## 5) Done

- Propósito:
  - Tarefas concluídas e validadas.

- Quando arquivar/limpar:
  - Periodicamente limpar/arquivar cards antigos (ex.: após release).

- Observações:
  - Mantenha histórico de quais PRs fecharam quais issues — use o link PR/issue no card.

---

## Exemplos de comandos `gh api` (criar colunas)

Substitua `{PROJECT_ID}` pelo ID do seu Project (no seu caso, o 7 se for o mesmo) e execute cada linha:

```bash
gh api projects/{PROJECT_ID}/columns -X POST -H "Accept: application/vnd.github.inertia-preview+json" -F name='Backlog'
gh api projects/{PROJECT_ID}/columns -X POST -H "Accept: application/vnd.github.inertia-preview+json" -F name='To Do'
gh api projects/{PROJECT_ID}/columns -X POST -H "Accept: application/vnd.github.inertia-preview+json" -F name='In Progress'
gh api projects/{PROJECT_ID}/columns -X POST -H "Accept: application/vnd.github.inertia-preview+json" -F name='In Review'
gh api projects/{PROJECT_ID}/columns -X POST -H "Accept: application/vnd.github.inertia-preview+json" -F name='Done'
```

Se preferir criar cards a partir de uma issue já existente (ex.: issue #1) — exemplo para adicionar card na coluna (substitua `{COLUMN_ID}` e `{ISSUE_NODE_ID}`):

1) Obter node_id da issue (ex.: #1):
```bash
gh api repos/edelcio-muniz/app-clima/issues/1 --jq '.node_id'
```

2) Adicionar card com referência a issue na coluna:
```bash
# supondo que ISSUE_NODE_ID seja o node_id retornado
gh api projects/columns/{COLUMN_ID}/cards -X POST -H "Accept: application/vnd.github.inertia-preview+json" -F content_id={ISSUE_NUM} -F content_type=Issue
```

Observação: a API de Projects usa `node_id`/`content_id` dependendo do endpoint; consulte a documentação se receber erro.

---

## Sugestões de automações (práticas)

- Auto-mover issues novas com label `triage` para `Backlog`.
- Quando PR é marcado `ready-for-review`, mover a card paralela para `In Review`.
- Ao fechar PR com "fixes #N" mover issue/card para `Done`.

Essas automations podem ser configuradas via GitHub Projects (UI) ou via GitHub Actions + API.

---

## Modelo curto para README do Project (texto pronto)

Board: app-clima Kanban

Propósito: Organizar o desenvolvimento do app-clima; Backlog → To Do → In Progress → In Review → Done.

Contribuição: abra issues e use labels; siga o fluxo de colunas. Consulte o README do repositório para instruções de execução e testes.

---


