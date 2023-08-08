dev:
	docker-compose up
{% if cookiecutter.framework == 'FastAPI' %}
SHELL := /bin/bash

# Variables definitions
# -----------------------------------------------------------------------------

# Target section and Global definitions
# -----------------------------------------------------------------------------
.PHONY: all clean test install run deploy down

all: clean test install run deploy down

test:
	poetry run pytest tests -vv --show-capture=all

install: generate_dot_env
	pip install --upgrade pip
	pip install poetry
	poetry install --with dev

run:
	uvicorn {{ cookiecutter.project_slug }}.main:app --reload

deploy: generate_dot_env
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

generate_dot_env:
	@if [[ ! -e .env ]]; then \
		cp .env.example .env; \
	fi

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build

all:

# docker
up:
	@echo "bringing up project...."
	docker compose up

down:
	@echo "bringing down project...."
	docker compose down

bash:
	@echo "connecting to container...."
	docker compose exec  cookiecutter.backend_container_name bash

# alembic
alembic-scaffold:
	@echo "scaffolding migrations folder..."
	docker compose exec  cookiecutter.backend_container_name alembic init -t async migrations

alembic-init:
	@echo "initializing first migration...."
	docker compose exec  cookiecutter.backend_container_name alembic revision --autogenerate -m "init"

alembic-make-migrations:
	@echo "creating migration file...."
	docker compose exec  cookiecutter.backend_container_name alembic revision --autogenerate -m "add year"

alembic-migrate:
	@echo "applying migration...."
	docker compose exec  cookiecutter.backend_container_name alembic upgrade head

# lint
test:
	@echo "running pytest...."
	docker compose exec  cookiecutter.backend_container_name pytest --cov-report xml --cov=src tests/

lint:
	@echo "running ruff...."
	docker compose exec  cookiecutter.backend_container_name ruff src

black:
	@echo "running black...."
	docker compose exec  cookiecutter.backend_container_name black .

mypy:
	@echo "running mypy...."
	docker compose exec  cookiecutter.backend_container_name mypy src/

# database
init-db: alembic-init alembic-migrate
	@echo "initializing database...."
	docker compose exec  cookiecutter.backend_container_name python3 src/db/init_db.py

check: BREW-exists
BREW-exists: ; @which brew > /dev/null

hooks: check
	@echo "installing pre-commit hooks...."
	pre-commit install
{% endif %}
