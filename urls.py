# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月26日00:51:03

import json

from service.urls import *
from wsgi import app


@app.errorhandler(404)
def get_not_found():
    return 'NOT FOUND', 404
