# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月26日00:51:03

import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from service.models import *

app = Flask(__name__)
app.config.from_object('myFlask.config')
db = SQLAlchemy(app)

# @app.errorhandler(404)
# def get_not_found():
#     return 'NOT FOUND', 404

@app.route('/user', methods=['GET'])
def get_users():
    filter_params = {}
    name = request.args.get('name')
    if name:
        filter_params['name'] = name
    users = User.query.filter_by(**filter_params)
    
    return [row2dict(user) for user in users]

@app.route('/user/<int:id>', methods=['GET'])
def get_user_by_name(id):
    user = User.query.get(id)
    if user:
        return jsonify(user)
    abort('Not Found')

@app.route('/user', methods=['POST'])
def create_user(body):
    post_body = {}
    name = request.json.get('name')
    if not name:
        abort('Name can not be none')
    post_body['name'] = name
    user = User(**post_body)
    db.session.add(user)
    db.commit()
    return jsonify({'code': 200, 'message': 'OK', 'data': user})

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
    db.session.commit()
    return jsonify({'code': 200, 'message': 'OK'})

@app.route('/user/<id>', methods=['PUT'])
def update_user(id, body):
    user = User.query.get(id)
    if not user:
        abort('Not Found')

    name = request.json.get('name')
    if name:
        user.name = name
    db.session.commit()
    return jsonify({'code': 200, 'message': 'OK', 'data': user})


if __name__ == "__main__":
    app.run()
