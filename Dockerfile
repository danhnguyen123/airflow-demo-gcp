FROM apache/airflow:2.10.0-python3.10

USER root

# install psycopg2, git
RUN apt-get update \
    # pakage required for psycopg2
    && apt-get -y install libpq-dev gcc gosu git wget
    # && pip install psycopg2

USER airflow

# Required for airflow 
RUN pip install passlib
# Install pakage python 
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH=${PYTHONPATH}:/opt/airflow/plugins

