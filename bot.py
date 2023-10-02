import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
import shutil
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery
from yt_dlp import YoutubeDL



CHOOSE_UR_MOD = " Choose Your mode ! "
CHOOSE_UR_MOD_BUTTONS = [
    [InlineKeyboardButton("من البداية",callback_data="frmstrt")],
     [InlineKeyboardButton("استكمال",callback_data="cont")]
]


bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6361913700:AAE2M_10WumBBFRhxod1dPOUbE2W6CwDNHI"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " االسلام عليكم أنا بوت التحميل من يوتيوب  ",disable_web_page_preview=True)
@bot.on_message(filters.command('clear') & filters.private)
def command2(bot,message):
    cmd('rm file.txt')
    shutil.rmtree('./downloads/')

@bot.on_message(filters.private & filters.reply )
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          global hazard
          hazard = message.text ;await message.delete()
          await message.reply(
             text = CHOOSE_UR_LANG2,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_LANG2_BUTTONS))



@bot.on_message(filters.private & filters.incoming & filters.text  )
def _telegram_file(client, message):

  global user_id
  user_id = message.from_user.id 
  global felo
  felo = message
  global url
  url = message.text
  cmd(f'''yt-dlp --flat-playlist -i --print-to-file url file.txt {url}''')
  message.reply(
             text = CHOOSE_UR_MOD,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_MOD_BUTTONS)

        )

@bot.on_callback_query()
def callback_query(CLIENT,CallbackQuery):
  CallbackQuery.edit_message_text(
      
      "جار التنزيل "
  )
  global numbofvid
  cmd(f'wc -l < file.txt > res.txt')
  with open('res.txt', 'r') as file:
        temp = file.read().rstrip('\n') 
  numbofvid = int(temp)
  cmd('unlink res.txt')
  
  if CallbackQuery.data == "frmstrt":
      CallbackQuery.edit_message_text("تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
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
       try :
        cmd(f'''yt-dlp -ciw  --extract-audio --audio-format mp3  -o "{video_title}"  "{link}"''')
        cmd(f'''python3 speech.py RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH "{video_title}.mp3" "{video_title}.txt"''')
        with open(f'''{video_title}.txt''', 'rb') as f:
         bot.send_document(user_id, f,caption=video_title)
        cmd(f'''rm res.txt "{video_title}.mp3" "{video_title}.txt"''' )   
       except FileNotFoundError: 
         pass  
       zaza += 1    
       cmd(f'unlink file.txt')
  
  elif CallbackQuery.data == "cont":
      CallbackQuery.edit_message_text("تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
      zaza = int(hazard) +1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')   
       with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{link}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)    
       try :
        cmd(f'''yt-dlp -ciw  --extract-audio --audio-format mp3  -o "{video_title}"  "{link}"''')
        cmd(f'''python3 speech.py RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH "{video_title}.mp3" "{video_title}.txt"''')
        with open(f'''{video_title}.txt''', 'rb') as f:
         bot.send_document(user_id, f,caption=video_title)
        cmd(f'''rm res.txt "{video_title}.mp3" "{video_title}.txt"''' )   
       except FileNotFoundError: 
         pass  
       zaza += 1    
       cmd(f'unlink file.txt')
  
bot.run()
