SHELL = /usr/bin/env bash

test:
	docker-compose run --rm web_app python -m unittest discover -v

start-server:
	docker-compose up web_app

down:
	docker-compose down

build:
	docker-compose build

local:
	pipenv run python3 app/main.py

