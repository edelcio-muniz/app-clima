SHELL := /bin/bash

.PHONY: up down build restart logs demo test monitor db-shell app-shell clean lint

up: ## Build and start containers (docker compose)
	@echo "[make] docker compose up -d --build"
	@docker compose up -d --build

down: ## Stop and remove containers
	@echo "[make] docker compose down"
	@docker compose down

build: ## Build images only
	@echo "[make] docker compose build"
	@docker compose build

restart: down up ## Restart the stack

logs: ## Tail logs for web service
	@docker compose logs -f web

demo: ## Run demo script
	@bash scripts/demo.sh

test: ## Run full test suite (python)
	@python tests/test_api.py

	@bash scripts/monitor-api-key.sh

db-shell: ## Open mysql shell inside db container
	@docker exec -it mysql_clima mysql -u $(DB_USER) -p$(DB_PASSWORD) $(DB_NAME)

app-shell: ## Enter web container shell
	@docker exec -it api_clima bash

clean: ## Prune docker images and volumes (use with caution)
	@echo "This will prune images and volumes. Press ENTER to continue or Ctrl+C to cancel."
	@read
	@docker image prune -af
	@docker volume prune -f

lint: ## Placeholder for linting
	@echo "Install flake8 and run: flake8 ."
