
.PHONY: help install install-dev format format-check type test build clean

help:
	@echo "Cibles disponibles :"
	@grep -E '^[a-zA-Z0-9_-]+:.*?##' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS=":.*?## "}; {printf "  [36m%-16s[0m %s\n", $$1, $$2}'

install: ## Installe les dépendances de production
	pip install -e .

install-dev: ## Installe les dépendances de développement
	pip install -e ".[dev]"

format: ## Formate le code
	black --line-length 100 src tests
	isort src tests

format-check: ## Vérifie le formatage
	black --check --line-length 100 src tests
	isort --check-only src tests

type: ## Vérifie les types
	mypy src/monPackage tests

test: ## Lance les tests
	pytest -q

build: ## Construit la distribution
	python -m build

clean: ## Nettoie les fichiers temporaires
	rm -rf .pytest_cache .mypy_cache .ruff_cache
	rm -rf dist build *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
