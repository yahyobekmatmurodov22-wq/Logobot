from telebot import TeleBot
from PIL import Image, ImageDraw, ImageFont
import random
import io

# Telegram bot tokenni kiriting
BOT_TOKEN = "8499581383:AAFM_VeLWiPb013xgahO0BCawmHrSdclnHs"
bot = TeleBot(BOT_TOKEN)

# Ranglar ro‘yxati
colors = ["red", "blue", "green", "purple", "orange", "cyan", "magenta", "gold", "lime"]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🎨 Logo yasovchi botga hush kelibsiz!\n\nLogo yaratish uchun /logo <matn> deb yozing.\nMasalan: /logo Otabek")

@bot.message_handler(commands=['logo'])
def logo_yarat(message):
    try:
        # Foydalanuvchi matni
        text = message.text.replace("/logo", "").strip()
        if not text:
            bot.reply_to(message, "Iltimos, logoda yoziladigan so‘zni kiriting.\nMasalan: /logo Yahyobek")
            return

        # Tasvir yaratish
        img = Image.new("RGB", (500, 200), color=random.choice(colors))
        draw = ImageDraw.Draw(img)

        # Shrft (default Pydroid’da mavjud bo‘lgan)
        font = ImageFont.load_default()

        # Matn o‘lchamini hisoblash (yangi usul)
        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]

        # Markazga joylashtirish
        position = ((500 - w) / 2, (200 - h) / 2)

        # Matn rangini aniqlash
        text_color = random.choice(["white", "black", "yellow"])

        # Matnni chizish
        draw.text(position, text, font=font, fill=text_color)

        # Rasmni yuborish
        bio = io.BytesIO()
        img.save(bio, "PNG")
        bio.seek(0)
        bot.send_photo(message.chat.id, bio, caption=f"✅ Sizning logongiz: {text}")

    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {e}")

print("🤖 Logo bot ishga tushdi!")
bot.polling(none_stop=True)