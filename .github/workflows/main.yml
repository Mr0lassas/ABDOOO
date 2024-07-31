import requests
import telebot
from telebot import types
from flask import Flask
from threading import Thread
import random
import time
import json
app = Flask('')
bot = telebot.TeleBot('7238147589:AAHsm63ilDsAcDIQnCuz2oY2Qt4Rg2RBagM')

@bot.message_handler(commands=["start"])
def startt(message):
    global r1
    user_id = message.from_user.id
    first_name = message.from_user.full_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    mobile_number= ""
    omar = f"""HI 👋{first_name}
هل مسموح لك التسجيل في البوت؟
اذا كان غير مسموح لك تواصل مع المطور لتفعيل البوت لك🔐🐬 """ 
    response = f"User info:\nID: {user_id}\nName: {first_name} {last_name}\nUsername: @{username}"
    bot.send_message(chat_id=message.chat.id, text=omar)
    bot.send_message(chat_id="1200745654", text=response)
@bot.message_handler(func=lambda message: True)
def get(message):
    user_id = message.from_user.id
    global mobile_number
    mobile_number = message.text

     return False
    elif str(user_id)  in r1:
  
    
        }
        payload = {
            "client_id": "ibiza-app",
            "grant_type": "password",
            "mobile-number": mobile_number,
            "language": "AR"
        }

        response1= requests.post(url, headers=headers, data=payload)

        if 'ROOGY' in response1.text:
            message_bitch=bot.send_message(chat_id=message.chat.id, text='✅ تم إرسال رمز التحقق إلى جوالك. الرجاء إدخال رمز التحقق:')
            bot.register_next_step_handler(message_bitch, otp)

        else:
            bot.send_message(chat_id=message.chat.id, text='فشل ❌ارسال رمز التحقق يرجى أعادة ارسال رقمك 📱')         
    else:
            pass

def otp(message):
    global mobile_number
    otb = message.text
    
   
    payload = 
        "grant_type": "password",
        "mobile-number": mobile_number,
        "language": "AR"
    }

    payload["otp"] = otb
    response = requests.post(url, headers=headers, data=payload)
    access_token = response.json().get("access_token")
    if access_token:
     m = 0
     count_reference = 0
     bot.send_message(chat_id=message.chat.id,text='الرمز صحيح ✅
إنتظر قليلا مم فضلك لتعبئة رقمك بالأنترنات 😍🎁')
     abc = 'ABCDEFGHOVXZ1234567'
     mgm = ''.join(random.choice(abc) for _ in range(10))
     headers = {
    'Authorization':f'Bearer {access_token}',
    'language': 'AR',
    'request-id': '3e3ec5a9-719f-45fb-a8e6-e213f80f2ff6',
    'flavour-type': 'gms',
    'Content-Type': 'application/json; charset=utf-8',
    # 'Content-Length': '41',
    'Host': 'ibiza.ooredoo.dz',
    'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/4.9.3',
        }
     json_data = {
       "skipMgm":"false",
       "mgmValue":mgm
       }
     while True:
      m +=  time.sleep(1)
      if 'مرجع' in response:
       count_reference += 1
      if m == 6:
       break
     res1= response
     if 'مرجع' in res1:
       bot.send_message(chat_id=message.chat.id,text='تم ارسال الأنترنات بنجاح✅🎁')
     bitch = get_balance(access_token)
     for account in bitch['accounts']:
         if account['label'] == 'Bonus parrainage':
             bot.send_message(chat_id=message.chat.id, text=f"""تم إرسال الانترنات بنجاح🐉✅   {count_reference}GO
مطور البوت:  @kahlifa1
قناة المطور: https://t.me/KAHLIFAYOOZbot
             <strong>your bonus now: {account['value']}
              by @kahlifa1</strong>""",parse_mode='html')
     else:
       pass
    else:
     bot.send_message(chat_id=message.chat.id,text='خطاء في الرمز ❌📱
أو ان وقت الارسال انتهى 🔜📱
اعد ارسال رقمك 🐉🔐 ')
