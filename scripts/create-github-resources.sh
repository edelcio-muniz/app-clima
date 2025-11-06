#!/usr/bin/env bash
set -euo pipefail

# Script to create GitHub resources (labels, issues, project, milestone)
# Requires: gh CLI (https://cli.github.com/) authenticated (gh auth login)

REPO_OWNER_AND_NAME="$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || true)"
if [ -z "$REPO_OWNER_AND_NAME" ]; then
  echo "Error: cannot detect repo. Run this script from a git repo or provide REPO in GH CLI context."
  echo "If you're running locally, run: gh auth login && gh repo view"
  exit 1
fi

echo "Using repo: $REPO_OWNER_AND_NAME"

echo "Creating labels..."
declare -a labels=(
  "bug:FF0000:Problemas que quebram o comportamento"
  "enhancement:1E90FF:Melhorias e novos recursos"
  "docs:2ECC71:Documentação"
  "test:8E44AD:Testes e QA"
  "ci:F39C12:CI / Workflows"
  "infra:95A5A6:Infraestrutura / Docker"
)

for label in "${labels[@]}"; do
  IFS=":" read -r name color desc <<< "$label"
  echo "- Creating label: $name ($color) - $desc"
  gh label create "$name" --color "$color" --description "$desc" || echo "label $name exists"
done

echo "Creating milestone v1.0.0 (if not exists)"
gh milestone create v1.0.0 -d "Initial release milestone" || echo "milestone exists"

echo "Creating sample issues..."
gh issue create --title "Adicionar CI básico" --body "Criar workflow GitHub Actions que instale dependências e execute checagens básicas (import/compile)." --label ci,enhancement || true
gh issue create --title "Configurar Kanban / Project" --body "Criar Project com colunas Backlog/To Do/In Progress/In Review/Done e adicionar issues iniciais." --label infra,docs || true
gh issue create --title "Melhorar tratamento de erros da API" --body "Revisar e melhorar mensagens de erro, códigos HTTP e logs." --label bug,enhancement || true

echo "Creating a classic project (if supported)"
gh project create "app-clima Kanban" --body "Kanban board for app-clima" || echo "project exists or gh version does not support classic projects"

echo "Done. Review created labels/issues in GitHub UI."
