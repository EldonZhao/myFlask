# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月26日00:51:03

from flask import Flask

app = Flask(__name__)

@app.route('/user', method=['GET'])
def get_users(*args, **kwargs):
    return "OK"
