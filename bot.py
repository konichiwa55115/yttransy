import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
import shutil
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery

bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6030811502:AAF0tj9q_2BH1HpmRZLkuvBQttmxYdYFw6o"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت قص الصوتيات , فقط أرسل الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming & filters.text  )
def _telegram_file(client, message):

  
  user_id = message.from_user.id 
  url = message.text
  
  message.reply_text("جار التحميل\n\n hh:mm:ss/hh:mm:ss")
  subprocess.call(['mkdir','downloads'])
  subprocess.call(['yt-dlp','--extract-audio','--audio-format','mp3','-o','downloads/'+"%(title)s.%(ext)s",url])
  subprocess.call(['uploadgram','-1001821573758','./downloads/'])
  shutil.rmtree('./downloads/')
bot.run()
