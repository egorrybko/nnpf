#!/bin/sh

# python manage.py flush --no-input
#python manage.py migrate image_pnev --settings=settings
#python manage.py collectstatic --no-input --clear
celery -A image_pnev worker -l DEBUG

exec "$@"