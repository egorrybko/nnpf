python manage.py runserver
celery -A image_pnev worker --loglevel=info --pool=solo