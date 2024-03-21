# Syntax
# target : prereqs
# 		recipe

.PHONY: install
install:
	poetry install

.PHONY: superuser
superuser:
	poetry run python -m core.manage createsuperuser

.PHONY: migrations
migrations:
	poetry run python -m core.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: runserver
runserver:
	poetry run python -m core.manage runserver

.PHONY: run
run: install migrations migrate runserver

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: update
update: install migrations migrate install-pre-commit lint;
