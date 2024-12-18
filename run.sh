#!/bin/sh

# cd /home/projects/check_co2/
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py &
#docker-compose up