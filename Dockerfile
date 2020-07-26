FROM python:3.8

COPY Pipfile.lock .
RUN pip install pipenv

ADD app app

EXPOSE 5000

CMD pipenv run python app/app.py