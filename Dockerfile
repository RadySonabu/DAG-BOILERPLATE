FROM python:3.7

ENV PYHTONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r app/requirements.txt