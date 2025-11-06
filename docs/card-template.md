<!--
  Template de card para o Kanban do projeto app-clima.
  Copie o bloco correspondente (Feature / Bug / Chore) e cole como corpo do card
  no Project ou como body de uma Issue. Está em pt-BR e pronto para editar.
-->

# Template de Card — Kanban (app-clima)

Use estes modelos conforme o tipo do trabalho. Mantenha os títulos curtos e padronizados:
- Feature: feature: <curta-descricao>
- Bug: bug: <curta-descricao>
- Chore/Tarefa: chore: <curta-descricao>

---

## Modelo - Feature

Título (exemplo): feature: adicionar cache para /clima/{cidade}

Descrição (cole e edite):

```
Resumo
Um parágrafo curto explicando a feature e o benefício (ex.: melhorar latência e reduzir chamadas à API externa).

Contexto
Breve contexto técnico ou de produto: endpoints afetados, dependências (OpenWeather), DB (MySQL), etc.

Critérios de aceitação
- [ ] Requisições para a mesma cidade em 10 minutos retornam do cache
- [ ] Testes de integração cobrem cenário de cache hit/miss
- [ ] Documentação/README atualizada com a configuração da variável de ambiente

Tarefas (checklist)
- [ ] Implementar cache em memória/Redis
- [ ] Atualizar endpoint /clima/{cidade}
- [ ] Adicionar testes
- [ ] Validar performance

Labels sugeridas: enhancement, infra, test
Milestone: v1.0.0 (opcional)
Assignee: @nome-do-responsavel (defina quando atribuir)
```

---

## Modelo - Bug

Título (exemplo): bug: erro 500 ao consultar cidade vazia

Descrição (cole e edite):

```
Resumo
Descreva em uma frase o que está acontecendo e qual o impacto para o usuário.

Passos para reproduzir
1. Chamar GET /clima/ com cidade vazia
2. Observar o erro 500 e stack trace X

Comportamento esperado
Retornar 400 com mensagem clara sobre parâmetro inválido.

Logs / Evidências
Cole trechos de logs, timestamps e payloads relevantes. (Não inclua secrets)

Critérios de aceitação
- [ ] Endpoint valida entrada e retorna 400 para cidade vazia
- [ ] Testes unitários cobrem validação

Labels sugeridas: bug
Milestone: (opcional)
Assignee: @nome-do-responsavel
```

---

## Modelo - Chore / Tarefa

Título (exemplo): chore: adicionar linting ruff e pre-commit

Descrição (cole e edite):

```
Resumo
Tarefa de infraestrutura/qualidade de código: configurar lint e hooks locais.

Passos
- Adicionar ruff ao requirements-dev
- Configurar .ruff.toml
- Incluir pre-commit com hooks básicos (ruff, isort)

Critérios de aceitação
- [ ] ruff detecta erros básicos no CI
- [ ] pre-commit instalado nos devs (documentar no README)

Labels sugeridas: ci, infra
Assignee: @nome-do-responsavel
```

---

## Sugestões de uso rápido

- Ao criar card no Project: cole o bloco inteiro acima no campo de descrição para manter padrão.
- Prefira adicionar labels e milestone já na criação para facilitar filtro e automações.
- Use o título padronizado para buscar e agrupar tipo de trabalho.

---

Se quiser, eu também crio versões em formato YAML/JSON (para automação) ou um CSV com os cards iniciais listados em `docs/project-cards.md` para importação via script. Deseja que eu gere algum desses formatos agora? 
