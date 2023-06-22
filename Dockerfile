FROM python:3-alpine3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app/

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
