import telebot, re, os
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

def send_first(message):
  link = "tg://openmessage?id=" + str(message.chat.id) + "&message_id=1"
  teks = "<a href='" + link + "'>Di sini</a>"
  bot.reply_to(message, teks)

@bot.message_handler(regexp=".*")
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
  pola = "^[,.!/]first(|@zipra_bot)$"
  if re.search(pola, pesan):
    send_first(message)
  print(message)

bot.polling()