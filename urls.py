# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月26日00:51:03

from flask import Flask
import json

app = Flask(__name__)

from service.urls import *

@app.errorhandler(404)
def get_not_found():
    return 'NOT FOUND', 404
