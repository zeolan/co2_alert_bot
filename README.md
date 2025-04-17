# Test project to familiarize with Telegram Bot and it's APIs

## 1. Setup virtual environment

```
python -m venv .venv
```

## 2. Activate virtual environment

```
source .venv\Scripts\activate
```

## 3. Install dependencies

```
pip install -r requirements.txt
```

## 4. Set environment variable BOT_TOKEN

Add .env file with BOT_TOKEN variable or
export it

## 5. Run app

```
. run.sh
```

## 5. Run app on the prod server

```
. check_bot_runing.sh
```

This will check if script is already running, and will start it if script isn't running.  
Every time app restarts, appropriate message will be written in **co2_bot.log**.  
Application logs will be written on the **logs/app.log**.

or add this line to the crontab (using crontab -e command)

```
@reboot cd /home/projects/check_co2 && sh ./check_bot_running.sh &
```
