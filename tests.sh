#!/bin/bash
set -e
export PYTHONPATH=src
python -d tests/sms.py
python -d tests/smsstorage.py
python -d tests/database.py
python -d tests/maintest.py
python -d tests/mailer.py
