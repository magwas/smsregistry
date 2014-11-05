#!/bin/bash
set -e
export PYTHONPATH=src
python -d tests/sms.py
python -d tests/smsstorage.py
