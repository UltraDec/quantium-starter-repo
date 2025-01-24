#!/usr/bin/bash

. ./venv/bin/activate

python -m pytest test_app.py

exitCode=$?

if [ $exitCode -eq 0 ]
then
  exit 0
else
  exit 1
fi