# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月19日01:00:51

from __future__ import absolute_import, unicode_literals

from celery import Celery
import sys

class CeleryApp(object):
    def __init__(self, app):
        self._celery_app = Celery(app, broker='', backend='', include=[])
        sefl._celery_app.update(result_expires=3600)

    def celery_app(self):
        return self._celery_app


if __name__ == '__main__':
    if 2 > sys.argv:
        raise Exception('参数个数不正确')
    
    app = sys.argv[-1]
    sys.argv.pop(-1)
    CeleryApp(app).celery_app().start()
