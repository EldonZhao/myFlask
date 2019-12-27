# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月26日01:00:16

from celery import Celery

class CeleryApp(Celery):
    def __init__(self, name):
        super(CeleryApp, self).__init__(name)
        self.config_from_object('celery_app.celery_config')


celery_app = CeleryApp('my-flask-celery')
celery_task = celery_app.task
celery_beat_schedule = celery_app.conf.beat_schedule


__all__ = ['CeleryApp', 'celery_app', 'celery_task', 'celery_beat_schedule']