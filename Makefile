.DEFAULT_GOAL := all

.PHONY: all
all: format lint typecheck

.PHONY: format
format:
	uv run ruff format
	uv run ruff check --fix --fix-only

.PHONY: lint
lint:
	uv run ruff format --check
	uv run ruff check -e

.PHONY: typecheck
typecheck:
	uv run pyright

.PHONY: test
test:
	uv run pytest

.PHONY: uwsgi
uwsgi:
	bash scripts/build_uwsgi.sh

.PHONY: nginx
nginx:
	bash scripts/build_nginx.sh
