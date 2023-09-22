# RADHEEFBOT

[![Telegram Bot](https://github.com/fauzaanu/radheefbot/actions/workflows/telegram.yml/badge.svg)](https://github.com/fauzaanu/radheefbot/actions/workflows/telegram.yml)

A telegram bot that uses the radheef.com api and google translate


### INLINE SUPPORTED

You can type @radheefbot on any chat and get a result.


### HOW IT WORKS

**One Word** 
- Goes through google translate to ensure its dhivehi and hits radheef API
- If radheef API has no results the same word is returned

**More than one word**
- Goes through google translate
- returns the google translate response


Google translate uses my fork of the unofficial py-googletrans package
The official repo still needs to accept my pull that includes dhivehi along with the update of httpx package

the requirements.txt includes this repo so you can clone and run

```
pip install -r requirements.txt
```

you need a .env file with 
```
TOKEN="telegram_api_key_from_bot_father"
```

### USAGE
You can simply add the run.bat to windows task sheduler

Running on any other system is pretty straightforward the bot is the inline_bot.py file

```
python inline_bot.py
```

It is highly recommended to create a virtual environment when running python

### TRY IT LIVE
The bot is live on [https://t.me/Radheefbot](https://t.me/Radheefbot)

I have this hosted on my personal PC and due to this you may see some downtime.

If someone is interested in hosting this for a long period (More than 1 Year), under the @radheefbot handle, Please contact me on telegram 
(Feel free to self host on your own handles!)

