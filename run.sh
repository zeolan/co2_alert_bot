#!/bin/sh

# cd /home/projects/check_co2/

if [ -d ".venv" ]; then
  . .venv/scripts/activate
else
  python -m venv .venv
  . .venv/bin/activate
  pip install -r requirements.txt
fi

python main.py &
#docker-compose up