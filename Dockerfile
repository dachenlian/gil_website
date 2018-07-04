FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt 
WORKDIR /code/gil_website/
RUN python manage.py collectstatic
