# myFlask

## 启动Flask

`python3 flask_app.py or falsk run`

## 启动Celery

* 非后台启动：
`celery worker -A celery_app -l=info -I app.tasks -Q app`

* 后台启动：
`celery multi start w1 -A celery_app -l info -I app.tasks -Q app`

## 启动Flower

`celery flower -A celery_app`
