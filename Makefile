.PHONY: help install start run run-api test lint format type-check clean docs release security

help:
	@echo "Available targets:"
	@echo "  install      - Install dependencies using uv"
	@echo "  start        - Run the CLI application (alias for run)"
	@echo "  run          - Run the CLI application"
	@echo "  run-api      - Run the FastAPI app"
	@echo "  test         - Run tests with coverage"
	@echo "  lint         - Run ruff checks"
	@echo "  format       - Run ruff format"
	@echo "  type-check   - Run mypy type checks"
	@echo "  security     - Run bandit security checks"
	@echo "  release      - Bump version and generate changelog locally"
	@echo "  clean        - Remove caches and build artifacts"

install:
	uv sync

start: run

run:
	uv run defaultpython

run-api:
	uv run uvicorn defaultpython.api:app --reload

test:
	uv run python -m pytest --cov --cov-report=term-missing

lint:
	uv run ruff check src tests

format:
	uv run ruff format src tests

type-check:
	uv run python -m mypy src tests

clean:
	rm -rf .venv .pytest_cache .ruff_cache .coverage site

release:
	uv run cz bump --changelog

security:
	uv run bandit -r src
