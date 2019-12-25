#! /usr/bin/env bash
celery multi stop worker -A celery_app -n app -I app.tasks -Q app -l info --pidfile='%p.pid' --logfile='%p.log'
ps aux | grep app-schedule | grep -v grep | awk '{print $2}' | xargs sudo kill -9
ps aux | grep flask | grep -v grep | awk '{print $2}' | xargs sudo kill -9