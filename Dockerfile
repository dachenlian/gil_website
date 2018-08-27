FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install pipenv
WORKDIR /code/gil_website/
RUN pipenv install --system
#RUN python manage.py collectstatic
