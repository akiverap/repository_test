SHELL := /bin/bash

# --- init project ---

.PHONY: requirements
requirements: pyproject.toml
	uv sync --group test

# --- run ---

.PHONY: run
run: requirements
	uv run uvicorn src.main:app --reload

# --- QA ---

.PHONY: ruff
ruff: requirements
	uv run ruff check . $(ARGS)

.PHONY: mypy
mypy: requirements
	uv run mypy src tests $(ARGS)

.PHONY: pytest
pytest: requirements
	uv run pytest -v $(ARGS)

.PHONY: quality_assurance
quality_assurance: ruff mypy pytest
