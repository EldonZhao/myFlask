# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2020年01月08日00:27:46
import os

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(os.getcwd(), 'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
