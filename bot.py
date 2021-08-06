from googletrans import Translator
import telebot, re, os

#Setup
tr = Translator()
bot = telebot.TeleBot(os.environ.get('TOKEN'), parse_mode="HTML")

print("Logging Started\n")

# Some strings
start = "Halo, perkenalkan namaku " + bot.get_me().first_name + ".\nSaya masih dalam pengembangan oleh @Pra210906"

def send_welcome(message):
  if message.chat.type != "private":
    bot.reply_to(message, "Hola, PM saya saja kalau ingin melihat bantuan ya...")
  else:
    bot.send_message(message.chat.id, start)

def send_pong(message):
  bot.reply_to(message, "<b>PONG!</b>")

def send_info(message):
  ingfo = "<b>Info Pengguna</b>\n\n👤 ID Pengguna: <code>"+str(message.from_user.id)+"</code>\n🙋 Nama depan: "+message.from_user.first_name+"\n💁🏼 Nama Belakang: "+message.from_user.last_name+"\n🤡 Username: @"+message.from_user.username+"\n🔗 Link: <a href='tg://user?id="+str(message.from_user.id)+"'>link</a>"
  bot.reply_to(message, ingfo)

def send_tes(message):
  bot.reply_to(message, "ya?")

def send_translation(msg, reg):
  try:
    smntr = tr.translate(msg.reply_to_message.text, dest=reg[3])
    hasil = smntr.text
    bot.reply_to(msg, hasil)
  except:
    pesan = "Ups, tidak ada kode bahasa: <code>" + reg[3] + "</code>. Kalau mau tau kode bahasa, coba cek <a href='https://www.google.com'>di sini</a> deh."
    bot.reply_to(msg, pesan)
@bot.message_handler(regexp=".*", content_types=['text', 'photo', 'video'])
def send(message):
  pesan = message.text
  pola = "^[$,.!/](start|help)(|@zipra_bot)$"
  if re.search(pola, pesan):
    send_welcome(message)
  pola = "^[,.!/]ping(|@zipra_bot)$"
  if re.search(pola, pesan):
    send_pong(message)
  pola = "^[,.!/]info(|@zipra_bot)$"
  if re.search(pola, pesan):
    send_info(message)
  pola = "^[,./!]tes(|@zipra_bot)$"
  if re.search(pola, pesan):
    send_tes(message)
  pola = "^[,./!](tr|tl|trans|translate)(|@zipra_bot)\s+(\w+)"
  if re.search(pola, pesan):
    send_translation(message, re.split(pola, pesan))

bot.polling()

