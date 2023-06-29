#!/bin/bash

# Collect static files
python manage.py collectstatic

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# check for any new migrations, then apply them to production database
python manage.py makemigrations 
python manage.py migrate

# Start nginx and reload it to apply the new config
nginx
nginx -s reload

tail -f /var/log/nginx/access.log -f /var/log/nginx/error.log & gunicorn project.wsgi:application --bind 0.0.0.0:8000 && fg