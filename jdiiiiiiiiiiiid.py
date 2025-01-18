import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import time

# توكن البوت الخاص بك
TOKEN = "7607704903:AAGWAbkr0vOO20O561tIAWTdiBuxvZUdNL4"

# الرابط الأساسي للأرشيف
BASE_URL = "https://archive.org"

# استخراج الروابط وتنظيمها
def fetch_audio_links():
    response = requests.get(f"{BASE_URL}/details/yassindzthomon")
    soup = BeautifulSoup(response.content, "html.parser")

    # استخراج جميع الروابط الصوتية من الصفحة
    links = soup.find_all("a", href=True)
    audio_links = {}

    for link in links:
        href = link['href']
        if href.endswith(".mp3"):  # التأكد أن الرابط خاص بملف صوتي
            # تقسيم الرابط لاستخراج معلومات الحزب والثمن
            parts = href.split("/")[-1].split("-")  # استخراج اسم الملف مثل H01-T01.mp3
            if len(parts) == 2:
                party = parts[0].replace("H", "حزب ")  # استخراج الحزب (H01 → حزب 1)
                thman = parts[1].replace("T", "ثمن ").replace(".mp3", "")  # استخراج الثمن (T01 → ثمن 1)
                name = f"{party} - {thman}"  # دمج الحزب والثمن
                audio_links[name] = BASE_URL + href

    return audio_links

# جلب الروابط الصوتية
audio_links = fetch_audio_links()

# دالة لبدء البوت
def start(update: Update, context: CallbackContext):
    user_name = update.effective_user.first_name  # اسم المستخدم
    update.message.reply_text(
        f"مرحبًا {user_name}! أرسل رقم الثمن (مثل: 1، 2، ... حتى {len(audio_links)}) للحصول على المقطع الصوتي."
    )

# دالة لإرسال المقطع الصوتي
def send_audio(update: Update, context: CallbackContext):
    try:
        # استخراج رقم الثمن الذي أدخله المستخدم
        thman_number = int(update.message.text)
        user_name = update.effective_user.first_name  # اسم المستخدم

        # الحصول على الرابط بناءً على الرقم
        keys = list(audio_links.keys())
        if 1 <= thman_number <= len(keys):
            key = keys[thman_number - 1]  # المفتاح المناسب
            audio_url = audio_links[key]

            # إرسال رسالة الدعاء
            update.message.reply_text(
                f"جزاك الله خيرًا يا {user_name}. استغفر الله وادعُ بالخير لصاحب الفكرة ريثما يتم تجهيز المقطع."
            )

            # إرسال المقطع الصوتي مع المعلومات
            time.sleep(2)  # محاكاة وقت تجهيز المقطع
            context.bot.send_voice(
                chat_id=update.effective_chat.id,
                voice=audio_url,
                caption=f"هذا هو المقطع:\n{key}"
            )
        else:
            update.message.reply_text(f"عذرًا، الرقم يجب أن يكون بين 1 و{len(keys)}.")
    except ValueError:
        update.message.reply_text("يرجى إدخال رقم صحيح.")
    except Exception as e:
        update.message.reply_text(f"حدث خطأ: {str(e)}")

# إعداد البوت
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # أوامر البوت
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, send_audio))

    # تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()