#! /usr/bin/env bash
celery multi start worker -A celery_app -n app -I app.tasks -Q app -l info --pidfile='%p.pid' --logfile='%p.log'
celery beat -A celery_app --pidfile='app@beat.pid' -s app-schedule -l info > app@nbeat.log 2>&1 &
python3 flask.py &