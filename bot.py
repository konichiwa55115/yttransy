import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery

bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6361913700:AAE2M_10WumBBFRhxod1dPOUbE2W6CwDNHI"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت قص الفيديوهات , فقط أرسل الفيديو هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming & filters.video | filters.document  )
def _telegram_file(client, message):

  
  user_id = message.from_user.id 
  file = message
  global file_path
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  global realname
  realname, ext = os.path.splitext(filename)
  global mp3file
  mp3file = realname+".mp3"
  global mp4file
  mp4file = realname+".mp4"
  message.reply_text("الآن أرسل نقطة البداية والنهاية بهذه الصورة \n\n hh:mm:ss/hh:mm:ss",reply_markup=ForceReply(True))


@bot.on_message(filters.private & filters.reply)
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          endstart = message.text ;await message.delete()
          strt, end = os.path.split(endstart);strt_point=strt 
          end_point = end
  
          subprocess.call(['ffmpeg','-i',file_path,'-ss',strt_point,'-to',end_point,'-c','copy',mp4file,'-y'])
          with open(mp4file, 'rb') as f:
            await bot.send_video(message.chat.id, f)
          subprocess.call(['unlink',file_path])
          subprocess.call(['unlink',mp4file])

        


bot.run()
