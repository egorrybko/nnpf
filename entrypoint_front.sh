#!/bin/sh

# python manage.py flush --no-input
#python manage.py migrate image_pnev --settings=settings
#python manage.py collectstatic --no-input --clear
gunicorn image_pnev.wsgi:application --bind 0.0.0.0:8000
#python manage.py runserver 0.0.0.0:8000

exec "$@"