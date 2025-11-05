# Kanban / GitHub Project Guide

Este documento descreve as configurações sugeridas para o Kanban (Projects) do GitHub antes de realizar o commit e o push do repositório.

> Observação: Este arquivo contém instruções e templates que você pode usar para criar o Project / Issues / Labels manualmente ou com GitHub CLI.

## Colunas do Kanban (Project board)

- Backlog (Ideias/Requests)
- To do (Próximas tarefas a serem feitas)
- In progress (Atualmente em desenvolvimento)
- In review (Pull Requests aguardando revisão)
- Done (Concluído)

## Labels sugeridos

- bug (red) — Problemas que quebram o comportamento
- enhancement (blue) — Melhorias/novos recursos
- docs (green) — Documentação
- test (purple) — Testes/QA
- ci (orange) — Integração contínua / workflow
- infra (gray) — Docker / infra

## Exemplo de Issues iniciais (templates)

1) Issue: "Adicionar CI básico"
   - Labels: `ci`, `enhancement`
   - Description: Criar workflow GitHub Actions que instale dependências e execute checagens básicas (import, lint, compile)

2) Issue: "Configurar Kanban / Project"
   - Labels: `infra`, `docs`
   - Description: Criar Project com colunas Backlog/To Do/In Progress/In Review/Done e adicionar issues iniciais

3) Issue: "Melhorar tratamento de erros da API"
   - Labels: `bug`, `enhancement`

## Milestones sugeridos

- v1.0.0 - Lançamento inicial
  - Issues: criar CI, documentar README, endpoints básicos, testes

## Assigness / Owners

- Author / Maintainer: adicione como `Assignee` nas issues críticas de arquitetura

## Automação com GitHub CLI (exemplo)

Se você tem `gh` (GitHub CLI) configurado, crie labels e project com comandos:

```bash
# criar label
gh label create "bug" --color FF0000 --description "Bug or breaking issue"
# criar project (classic)
gh project create "app-clima Kanban" --body "Kanban board for app-clima"
```

## Templates de Issue (colocar em `.github/ISSUE_TEMPLATE/`)

- `bug.md` — reportar erros com steps para reproduzir
- `feature.md` — descrever novo recurso com story e acceptance criteria

## GitHub Actions (recomendação)

- Um workflow `ci.yml` para:
  - Instalar Python 3.11
  - Instalar dependências
  - Rodar checks rápidos (import, compile)
  - (Opcional) Build docker image e push em tag

## Observações finais


