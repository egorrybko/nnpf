#!/bin/sh

# python manage.py flush --no-input
#python manage.py migrate image_pnev --settings=settings
#python manage.py collectstatic --no-input --clear
python manage.py runserver 0.0.0.0:8000

exec "$@"