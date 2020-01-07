# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月19日00:46:27

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('myFlask.config')
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run()
