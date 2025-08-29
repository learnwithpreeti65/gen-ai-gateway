.PHONY: help install dev test lint format clean run

help:  ## Show this help message
	@echo "Gen AI Gateway - Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install the package and dependencies
	pip install -e .

dev:  ## Install development dependencies
	pip install -e .[dev]

test:  ## Run tests
	pytest gen_ai_gateway/tests/ -v

test-coverage:  ## Run tests with coverage
	pytest gen_ai_gateway/tests/ --cov=gen_ai_gateway --cov=ppt_wrapper --cov-report=html --cov-report=term

lint:  ## Run linting checks
	flake8 gen_ai_gateway ppt_wrapper
	black --check gen_ai_gateway ppt_wrapper
	isort --check-only gen_ai_gateway ppt_wrapper

format:  ## Format code
	black gen_ai_gateway ppt_wrapper
	isort gen_ai_gateway ppt_wrapper

mypy:  ## Run type checking
	mypy gen_ai_gateway ppt_wrapper

tox:  ## Run all tests with tox
	tox

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .tox/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

run:  ## Run the development server
	python run.py

run-prod:  ## Run the production server
	uvicorn gen_ai_gateway.apps.main:app --host 0.0.0.0 --port 8000

docker-build:  ## Build Docker image
	docker build -t gen-ai-gateway .

setup-git-hooks:  ## Setup git pre-commit hooks
	pre-commit install
