import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery

bot = Client(
    "voluemincreaser",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6178182404:AAHHX9ilOcXiqo4m728-N6pR2QZ70CVi4E4"
)



@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا إزالة الضوضاء ورفع مستوى الصوت , فقط أرسل الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming &  filters.audio | filters.voice  )
def _telegram_file(client, message):
  
  global user_id
  user_id = message.from_user.id 
  file = message
  global file_path
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  realname, ext = os.path.splitext(filename)
  global mp3file
  mp3file = realname+".mp3"
  message.reply(
             text = CHOOSE_UR_LANG,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_LANG_BUTTONS)

        )
 
  subprocess.call(['ffmpeg','-i',file_path,'-af',f"arnndn=m=mp.rnnn","mod"+mp3file,'-y']) 
  subprocess.call(['ffmpeg','-i',"mod"+mp3file,'-af', "volume=4",mp3file,'-y']) 
  with open(mp3file, 'rb') as f:
         bot.send_audio(user_id, f)
  subprocess.call(['unlink',mp3file]) 
  subprocess.call(['unlink',"mod"+mp3file])
  subprocess.call(['unlink',file_path]) 


       

bot.run()
