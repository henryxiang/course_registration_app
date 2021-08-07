#!/usr/bin/env bash

BASE=$(dirname $(realpath $0))

cd $BASE

source init.sh
python app/main.py
