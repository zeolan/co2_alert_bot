#!/bin/bash

while :
do
    echo "Cheking if bot is running..." >/dev/null
    if ! $(pgrep -x "python" >/dev/null)
    then
        echo "Bot isn't running, restart it"
        echo `date` >> co2_bot.log
        sh ./run.sh
        echo $? >> co2_bot.log
    else
        echo "Bot is running, OK" >/dev/null
    fi
    sleep 3m
done