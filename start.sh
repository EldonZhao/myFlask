#! /usr/bin/env bash
celery multi start worker -A app.tasks -n app -I app.tasks -Q app -l info --pidfile='%p.pid' --logfile='%p.log'
celery beat -A app.tasks --pidfile='beat@app.pid' -s app-schedule -l info > beat@app.log 2>&1 &
python3 wsgi.py &