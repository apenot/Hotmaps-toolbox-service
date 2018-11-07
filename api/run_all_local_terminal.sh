#!/usr/bin/env bash

sudo gnome-terminal -e "python producer_cm_alive.py" --title="HTAPI: producer_cm_alive"

sudo gnome-terminal -e "python run.py" --title="HTAPI: run API"

sudo gnome-terminal -e "python consumer_cm_register.py" --title="HTAPI: consumer_cm_register"

sudo gnome-terminal -e "celery -A celery_worker.celery worker --loglevel=info --concurrency=10 -n worker3@%" --title="HTAPI: celery3"

sudo gnome-terminal -e "celery -A celery_worker.celery worker --loglevel=info --concurrency=10 -n worker2@%h" --title="HTAPI: celery2"

sudo gnome-terminal -e "celery -A celery_worker.celery worker --loglevel=info --concurrency=10 -n worker1@%h" --title="HTAPI: celery1"



