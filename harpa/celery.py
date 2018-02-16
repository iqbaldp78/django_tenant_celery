import os
from harpa.settings import TIME_ZONE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'harpa.settings')
# from celery.schedules import crontab
from django.conf import settings

from tenant_schemas_celery.app import CeleryApp

app = CeleryApp()
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    'add-every-60-seconds': {
        'task': 'fmw.concurrentManager.tasks.concurrent_schedule',
        'schedule': 60.0
    },
}

app.conf.update(
    result_backend='django-db',
    # CELERY_RESULT_DBURI = "postgresql://trees_apps:trees_apps@trees.harpa.com/harpa",
    # result_backend='db+postgresql://trees_apps:trees_apps@trees.harpa.com/harpa',
    # CELERY_RESULT_DBURI = "postgresql://trees_apps:trees_apps@trees.harpa.com/harpa",
    include=['fmw.concurrentManager.tasks',],
)

CELERY_TIMEZONE = TIME_ZONE