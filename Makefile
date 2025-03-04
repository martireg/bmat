SHELL = /usr/bin/env bash

test:
	docker-compose run --rm web_app python -m unittest discover -v

test-local:
	pipenv run python -m unittest discover -v

start-server:
	docker-compose up web_app

down:
	docker-compose down

build:
	docker-compose build

start-local:
	$(MAKE) install-dev
	docker-compose up -d db
	pipenv run uvicorn app.main:app --reload

lint:
	$(MAKE) install-dev
	pipenv run mypy app || true
	pipenv run pylint app || true

install-dev:
	touch .env
	pipenv install --dev

init:
	touch .env
	docker volume create --name=mongodb_data
	docker-compose build

remove-volumes:
	docker volume rm mongodb_data

mongo:
	docker-compose exec db mongo

start-as-deamon:
	docker-compose up -d web_app
