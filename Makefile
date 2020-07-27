SHELL = /usr/bin/env bash

test:
	docker-compose run --rm web_app python -m unittest discover -v

start-server:
	docker-compose up web_app

down:
	docker-compose down

build:
	docker-compose build

start-local:
	$(MAKE) install-dev
	pipenv run uvicorn app.main:app --reload

parse:
	$(MAKE) install-dev
	pipenv run mypy app || true
	pipenv run pylint app || true

install-dev:
	pipenv install --dev