FROM python:3.8

RUN pip install pipenv
COPY Pipfile.lock /tmp
COPY Pipfile /tmp
RUN cd /tmp && pipenv install --system --deploy

ADD app /opt/app
ADD tests /opt/tests

WORKDIR /opt

EXPOSE 80

CMD uvicorn app.main:app --host 0.0.0.0 --port 80
