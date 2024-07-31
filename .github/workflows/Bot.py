import requests
import telebot
import yaml
from flask import Flask
from threading import Thread
import random
import time
import json

app = Flask(__name__)

# Load configuration from YAML file
with open('bot.yml', 'r') as file:
    config = yaml.safe_load(file)

bot = telebot.TeleBot(config['telegram_bot_token'])

@bot.message_handler(commands=["start"])
def startt(message):
    global r1
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    mobile_number = ""
    omar = f"""HI 👋 {first_name}
هل مسموح لك التسجيل في البوت؟
اذا كان غير مسموح لك تواصل مع المطور لتفعيل البوت لك🔐🐬""" 
    response = f"User info:\nID: {user_id}\nName: {first_name} {last_name}\nUsername: @{username}"
    bot.send_message(chat_id=message.chat.id, text=omar)
    bot.send_message(chat_id=config['developer_chat_id'], text=response)

@bot.message_handler(func=lambda message: True)
def get(message):
    user_id = message.from_user.id
    global mobile_number
    mobile_number = message.text

    # Ensure `r1` and `url`, `headers` are defined here
    if str(user_id) in r1:
        url = config['api_url']
        headers = config['headers']

        payload = {
            "client_id": "ibiza-app",
            "grant_type": "password",
            "mobile-number": mobile_number,
            "language": "AR"
        }

        response1 = requests.post(url, headers=headers, data=payload)

        if 'ROOGY' in response1.text:
            message_bitch = bot.send_message(chat_id=message.chat.id, text='✅ تم إرسال رمز التحقق إلى جوالك. الرجاء إدخال رمز التحقق:')
            bot.register_next_step_handler(message_bitch, otp)
        else:
            bot.send_message(chat_id=message.chat.id, text='فشل ❌ارسال رمز التحقق يرجى أعادة ارسال رقمك 📱')         
    else:
        pass

def otp(message):
    global mobile_number
    otb = message.text

    url = config['api_url']
    headers = config['headers']

    payload = {
        "grant_type": "password",
        "mobile-number": mobile_number,
        "language": "AR",
        "otp": otb
    }

    response = requests.post(url, headers=headers, data=payload)
    access_token = response.json().get("access_token")
    if access_token:
        m = 0
        count_reference = 0
        bot.send_message(chat_id=message.chat.id, text='الرمز صحيح ✅ إنتظر قليلا مم فضلك لتعبئة رقمك بالأنترنات 😍🎁')
        abc = 'ABCDEFGHOVXZ1234567'
        mgm = ''.join(random.choice(abc) for _ in range(10))
        headers = {
            'Authorization': f'Bearer {access_token}',
            'language': 'AR',
            'request-id': '3e3ec5a9-719f-45fb-a8e6-e213f80f2ff6',
            'flavour-type': 'gms',
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'ibiza.ooredoo.dz',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/4.9.3',
        }
        json_data = {
            "skipMgm": "false",
            "mgmValue": mgm
        }
        while True:
            m += time.sleep(1)
            if 'مرجع' in response:
                count_reference += 1
            if m == 6:
                break
        res1 = response
        if 'مرجع' in res1:
            bot.send_message(chat_id=message.chat.id, text='تم ارسال الأنترنات بنجاح✅🎁')
            bitch = get_balance(access_token)
            for account in bitch['accounts']:
                if account['label'] == 'Bonus parrainage':
                    bot.send_message(chat_id=message.chat.id, text=f"""تم إرسال الانترنات بنجاح🐉✅   {count_reference}GO
مطور البوت:  @kahlifa1
قناة المطور: https://t.me/KAHLIFAYOOZbot
                    <strong>your bonus now: {account['value']}
                     by @kahlifa1</strong>""", parse_mode='html')
        else:
            pass
    else:
        bot.send_message(chat_id=message.chat.id, text='خطاء في الرمز ❌📱 أو ان وقت الارسال انتهى 🔜📱 اعد ارسال رقمك 🐉🔐 ')

if __name__ == "__main__":
    app.run(threaded=True)
