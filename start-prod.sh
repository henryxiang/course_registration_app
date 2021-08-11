#!/usr/bin/env bash

PROJECT_DIR=$(cd $(dirname $0); pwd)

cd $PROJECT_DIR
echo "PROJECT_DIR=$(pwd)"

source init.sh
gunicorn --chdir=app --workers=4 main:app
