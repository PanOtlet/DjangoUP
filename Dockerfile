FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install pipenv
RUN pipenv lock
RUN pipenv sync
ADD . /code/
