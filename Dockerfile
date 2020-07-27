FROM python:3.8

RUN pip install pipenv
COPY Pipfile.lock /tmp
COPY Pipfile /tmp
RUN cd /tmp && pipenv install --system --deploy

ADD app app
ADD tests tests

EXPOSE 5000

CMD hypercorn app.main:app
