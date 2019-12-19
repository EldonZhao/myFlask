# -*- coding: utf-8 -*-
# @author: xueyong.zxy
# @date: 2019年12月19日00:46:27

from flask import Flask

app = Flask(__name__)

@app.route('/hello-world', methods=['GET'])
def hello_world():
    return 'Hello World.'

if __name__ == "__main__":
    app.run()