# myFlask

## 启动Flask

`python3 flask_app.py`

## 启动Celery

* 非后台启动：
`celery -A celery_app worker -l=info`

* 后台启动：
`celery multi start w1 -A celery_app -l info`

* python启动：
`python celery_app.py worker -l info`

## 启动Flower

`python celery_app.py flower -l info`
