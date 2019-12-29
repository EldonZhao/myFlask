# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月26日00:51:03

from flask import Flask
import json

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def get_users(*args, **kwargs):
    return json.dumps([{'name': 'eldon', 'gendor': 'male'}])

@app.route('/user/<name>', methods=['GET'])
def get_user_by_name(name):
    return {'name': name, 'gendor': 'male'}
