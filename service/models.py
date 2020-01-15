# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2020年01月08日00:34:26

from flask_sqlalchemy import SQLAlchemy

from application import db

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    pass

    def __repr__(self):
        return '<User: %s>' % self.name
