# base image
FROM python:3.9.6 as base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV POETRY_VIRTUALENVS_CREATE false

RUN pip install --upgrade pip

# install poetry


WORKDIR /app




# linters image
FROM base as linters

COPY ./requirements /code/requirement

RUN pip install --no-cache-dir --upgrade -r /code/requirement/linters.txt


COPY . ./

CMD ["make", "lint.local"]

# test image
FROM base as tests
ARG JUNIT_PATH=./reports/junit.xml
ARG COVERAGE_PATH=./reports/coverage.xml

RUN pip install -r requierements/test.txt

COPY . ./

CMD ["make", "test.local"]

# development image
FROM base as development

EXPOSE 8000

ENV DEBUG=1

COPY ./requirements /code/requirement

RUN pip install --no-cache-dir --upgrade -r /code/requirement/base.txt


COPY ./app /code/app


CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

