# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月26日01:08:29

from celery_app import celery_app, celery_beat_schedule
from celery.schedules import crontab

@celery_app.task(name='app.task1', queue='app.tasks')
def task1(x, y):
    return x + y

celery_beat_schedule.update(
    app_task1_beat = {
        'name': 'app_task1_beat',
        'task': 'app.task1',
        'schedule': crontab(), # 1min
        'args': (5, 2),
        'options': {'queue': 'app.tasks'}
    }
)