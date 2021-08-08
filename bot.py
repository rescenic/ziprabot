from googletrans import Translator
import telebot, re, os
from help import get_help

#Setup
tr = Translator()
bot = telebot.TeleBot(os.environ.get('TOKEN'), parse_mode="HTML")
print("Logging Started\n")

# Some strings
start = "Halo, perkenalkan namaku " + bot.get_me().first_name + ".\nSaya masih dalam pengembangan oleh @Pra210906\n\nKetik /help untuk melihat bantuan"
bantu = "Bantuan tersedia:\n\n<code>ping</code>\n\nKamu bisa menggunakan titik(.), koma(,), garing(/), dan seru(!)."

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
    if msg.reply_to_message:
        if msg.reply_to_message.text:
            teks = msg.reply_to_message.text
        else:
            teks = msg.reply_to_message.caption
    try:
        smntr = tr.translate(teks, dest=reg[3])
        hasil = "Diterjemahkan dari <code>" + smntr.src + "</code>\n\n" + smntr.text + "</code>"
        bot.reply_to(msg, hasil)
    except:
        pesan = "Ups, tidak ada kode bahasa: <code>" + reg[3] + "</code>. Kalau mau tau kode bahasa, coba cek <a href='https://www.google.com'>di sini</a> deh."
        bot.reply_to(msg, pesan)

def send_help(msg, reg):
    ups = str(reg[2])
    if msg.chat.type != "private":
        bot.reply_to(msg, "Hola, PM saya saja kalau ingin melihat bantuan ya...")
    elif ups == "":
        bot.send_message(msg.chat.id, bantu)
    else:
        try:
            bot.reply_to(msg, get_help(ups))
        except:
            bot.reply_to(msg, "Ngga ada bantuan buat <code>" + ups + "</code>. Mungkin perintah itu tidak tersedia atau kamu yang salah ketik 🤔")

@bot.message_handler(regexp=".*", content_types=['text', 'photo', 'video'])
def send(message):
    pesan = message.text
    pola = "^[$,.!/]start(|@zipra_bot)$"
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
    pola = "^[,./!]help(|@zipra_bot)\s{0,}(\w{0,})"
    if re.search(pola, pesan):
        send_help(message, re.split(pola, pesan))

bot.polling()

