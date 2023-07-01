import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery

bot = Client(
    "merger",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6169974916:AAHl_RThcfUk7kgPTUDhwBtMBqNhbMjExOg"
)

CHOOSE_UR_LANG = "أرسل باقي الصوتيات بالترتيب ثم اضغط دمج الآن  "
CHOOSE_UR_LANG_BUTTONS = [
    [InlineKeyboardButton("دمج الآن",callback_data="دمج الآن")],
]

@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت دمج الصوتيات , فقط أرسل الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming &  filters.audio | filters.voice  )
def _telegram_file(client, message):
  
  global user_id
  user_id = message.from_user.id 
  file = message
  global file_path
  file_path = message.download(file_name="./downloads/")
  with open('list.txt','a') as f:
      f.write(f"file '{file_path}'' \n")
  filename = os.path.basename(file_path)
  realname, ext = os.path.splitext(filename)
  global mp3file
  mp3file = realname+".mp3"
  message.reply(
             text = CHOOSE_UR_LANG,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_LANG_BUTTONS)

        )

@bot.on_callback_query()
def callback_query(CLIENT,CallbackQuery):

  CallbackQuery.edit_message_text(
      
      "جار الدمج"
  )   
  subprocess.call(['ffmpeg','-f','concat','-safe','0','-i','list.txt', mp3file,'-y']) 
  with open(mp3file, 'rb') as f:
         bot.send_audio(user_id, f)
  subprocess.call(['unlink',"list.txt"]) 
  subprocess.call(['unlink',mp3file]) 
  subprocess.call(['unlink',file_path]) 


       

bot.run()
