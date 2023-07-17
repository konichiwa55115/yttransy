import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
import shutil
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery
from yt_dlp import YoutubeDL

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

  global user_id
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
  cmd(f'yt-dlp --flat-playlist -i --print-to-file url file.txt {url}')
  global numbofvid
  cmd(f'wc -l < file.txt > res.txt')
  with open('res.txt', 'r') as file:
        temp = file.read().rstrip('\n') 
  numbofvid = int(temp)
  cmd('unlink res.txt')
  if CallbackQuery.data == "vid 360p":
      zaza = 1 
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')   
       with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{link}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None) 
       cmd(f'yt-dlp -f 18 -o downloads/"%(title)s.%(ext)s" {link}')
       with open(f'./downloads/{video_title}.mp4', 'rb') as f:
        bot.send_video(user_id, f,caption=video_title)
       shutil.rmtree('./downloads/')
       cmd(f'unlink res.txt')
       zaza += 1           

  elif CallbackQuery.data == "vid 720p":
      zaza = 1 
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')
       with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{link}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None) 
       cmd(f'yt-dlp -f 22 -o downloads/"%(title)s.%(ext)s" {link}')
       with open(f'./downloads/{video_title}'+".mp4", 'rb') as f:
        bot.send_video(user_id, f,caption=video_title)
       shutil.rmtree('./downloads/')
       cmd('unlink res.txt')
       zaza += 1           
      
  elif CallbackQuery.data == "aud":
      zaza = 1 
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')   
       with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{link}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)     
       cmd(f'yt-dlp --extract-audio --audio-format mp3  -o downloads/"%(title)s.%(ext)s" {link}')
       with open(f'./downloads/{video_title}'+".mp3", 'rb') as f:
        bot.send_audio(user_id, f,caption=video_title)
       shutil.rmtree('./downloads/')
       cmd('unlink res.txt')
       zaza += 1           
  CallbackQuery.edit_message_text(
      
      "تم التنزيل ✅"
   )   
  cmd(f'unlink file.txt')

bot.run()
