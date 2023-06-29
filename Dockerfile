FROM python:3-alpine3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev bash nginx

RUN mkdir -p /app/

WORKDIR /app

COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /run/nginx

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

RUN chmod u+x ./start.sh

ENTRYPOINT ["./start.sh"]