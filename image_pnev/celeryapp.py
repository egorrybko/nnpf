# image_parroter/image_parroter/celery.py

import os
import sys
from celery import Celery
from celery._state import _set_current_app
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_pnev.settings')

celery_app = Celery('image_pnev')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
_set_current_app(celery_app)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../image_pnev')))
django.setup()
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
