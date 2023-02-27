from celery import Celery
celery_app = Celery(__name__ + '_app', broker='redis://rds1:6379/0', backend='redis://rds1:6379/0')


@celery_app.task(name='task_sum')
def task_sum(**kwargs):
    param1= kwargs.get('param1')
    param2 = kwargs.get('param2')
    return float(param1) + float(param2)
