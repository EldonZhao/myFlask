# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2020年01月08日01:12:45

import click

from wsgi import app, db

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def init_db(drop):
    '''Initialize the database.'''
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息
