#!/usr/bin/env bash

PROJECT_DIR=$(cd $(dirname $0); pwd)

cd $PROJECT_DIR
echo "PROJECT_DIR=$(pwd)"

if [ ! -e 'venv' ]; then
    echo "creating virtual env";
    python3 -m venv venv;
    source venv/bin/activate;
    pip install -r requirements.txt
fi

source venv/bin/activate

if [ "$PYTHONPATH" = "" ]; then
    echo "setting PYTHONPATH"
    export PYTHONPATH=$(pwd)/app;
fi

echo "python=$(which python)"
echo "PYTHONPATH=${PYTHONPATH}"
