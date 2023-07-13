import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
import shutil
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery

CHOOSE_UR_LANG = " Choose Your folmula ! "
CHOOSE_UR_LANG_BUTTONS = [
    [InlineKeyboardButton("vid 360p",callback_data="vid 360p")],
     [InlineKeyboardButton("vid 720p",callback_data="vid 720p")],
     [InlineKeyboardButton("aud",callback_data="aud")]
]


bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6030811502:AAF0tj9q_2BH1HpmRZLkuvBQttmxYdYFw6o"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " االسلام عليكم أنا بوت التحميل من يوتيوب  ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming & filters.text  )
def _telegram_file(client, message):

  
  user_id = message.from_user.id 
  global url
  url = message.text  
  cmd(f'mkdir downloads')
  message.reply(
             text = CHOOSE_UR_LANG,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_LANG_BUTTONS)

        )

@bot.on_callback_query()
def callback_query(CLIENT,CallbackQuery):
  CallbackQuery.edit_message_text(
      
      "جار التنزيل "
  )   
  if CallbackQuery.data == "vid 360p":
      cmd(f'yt-dlp -f 18 -o downloads/+"%(title)s.%(ext)s" {url}')
  elif CallbackQuery.data == "vid 720p":
      cmd(f'yt-dlp -f 22 -o downloads/+"%(title)s.%(ext)s" {url}')
  elif CallbackQuery.data == "aud":
      cmd(f'yt-dlp --extract-audio --audio-format mp3  -o downloads/+"%(title)s.%(ext)s" {url}')
  cmd(f'sudo uploadgram -1001821573758 ./downloads/')
  shutil.rmtree('./downloads/')
  CallbackQuery.edit_message_text(
      
      "تم التنزيل ✅"
  )   


bot.run()
