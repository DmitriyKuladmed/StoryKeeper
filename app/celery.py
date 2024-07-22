from celery import Celery

celery = Celery(
    'app',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
    include=['app.tasks']
)

celery.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    celery.start()
