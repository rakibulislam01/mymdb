#!/usr/bin/env bash
root-$1
source $root/venv/bin/activate

export TIMEOUT=100

cd $root/main/
python manage.py collectstatic