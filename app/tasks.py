# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月26日01:08:29

from celery_app import celery_task, celery_beat_schdule
from celery.schedules import crontab

@celery_task(name='app.task1', queue='app')
def task1(x, y):
    return x + y

celery_beat_schdule.update(
    app_task1_beat = {
        'name': 'app_task1_beat',
        'task': 'app.task1',
        'schedule': crontab(), # 1min
        'args': (5, 2),
        'options': {'queue': 'app'}
    }
)