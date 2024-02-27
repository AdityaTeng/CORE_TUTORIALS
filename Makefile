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

.PHONY: update
update: install migrations migrate ;

.PHONY: run
run: install migrations migrate runserver ;