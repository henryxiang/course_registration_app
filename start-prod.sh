#!/usr/bin/env bash

BASE=$(dirname $(realpath $0))

cd $BASE

source init.sh
gunicorn --chdir=app --workers=4 main:app
