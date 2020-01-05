# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月19日01:08:59

import json
from wsgi import app

@app.route('/user', methods=['GET'])
def get_users(*args, **kwargs):
    return json.dumps([{'name': 'eldon', 'gendor': 'male'}])

@app.route('/user/<string:name>', methods=['GET'])
def get_user_by_name(name):
    return {'name': name, 'gendor': 'male'}

@app.route('/user', methods=['POST'])
def create_user(body):
    pass

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    pass

@app.route('/user/<id>', methods=['PUT'])
def update_user(id, body):
    pass