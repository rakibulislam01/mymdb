#!/usr/bin/env bash
root=$1
# shellcheck disable=SC1090
# shellcheck disable=SC2086
source ${root}/venv/bin/activate

export DJANGO_CASHE_TIMEOUT=100
export DJANGO_SETTINGS_MODULE=main.settings

export TIMEOUT=100

# shellcheck disable=SC2164
# shellcheck disable=SC2086
cd ${root}/main/
python manage.py collectstatic