# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2020年01月01日21:12:10

import time

from celery.signals import *
import statsd

task_time = {}

statsd_conn = statsd.StatsClient(
    host='127.0.0.1',
    port=8125,
)

@task_prerun.connect
def task_prerun_handler(task_id, task, *args, **kwargs):
    task_time[task_id] = time.time()
    statsd_conn.incr('{}.prerun'.format(task.name))

@task_postrun.connect
def task_postrun_handler(task_id, task, *args, **kwargs):
    statsd_conn.incr('{}.postrun'.format(task.name))
    delta_seconds = time.time() - task_time[task_id]
    # 任务执行时间
    statsd_conn.timing('{}.runtime'.format(task.name), int(1000 * delta_seconds))


@task_success.connect
def task_success_handler(sender, result, **kwargs):
    # 成功任务数
    statsd_conn.incr('{}.success'.format(sender.name))


@task_failure.connect
def task_failure_handler(sender, result, **kwargs):
    # 失败任务数
    statsd_conn.incr('{}.failure'.format(sender.name))
