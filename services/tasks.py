from celery import Celery
celery_app = Celery(__name__ + '_app', broker='redis://192.168.18.206:14000/0', backend='redis://192.168.18.206:14000/0')


# python3 -m celery -A tasks worker --loglevel=INFO
@celery_app.task(name='task_sum')
def sum(**kwargs):
    param1= kwargs.get('param1')
    param2 = kwargs.get('param2')
    return float(param1) + float(param2)