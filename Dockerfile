FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install pipenv
WORKDIR /code/
RUN pipenv install --system
WORKDIR /code/gil_website
