import telebot, re, os
from googletrans import Translator

#Setup Environment
reg = re.search
res = re.split
tr = Translator().translate
bot = telebot.TeleBot(os.environ.get('TOKEN'), parse_mode="HTML")
languages_code = ['auto', 'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']

#Strings
start = "Halo, perkenalkan namaku " + bot.get_me().first_name + ".\nSaya masih dalam pengembangan oleh @Pra210906\n\nKetik /help untuk melihat bantuan"
bantu = "Bantuan tersedia:\n\n<code>ping, translate</code>\n\nKamu bisa menggunakan titik(.), koma(,), garing(/), dan seru(!)."

<<<<<<< HEAD
def start_handler(msg):
    if msg.chat.type != "private":
        bot.reply_to(msg, "Ya, PM saya aja kalo pengen liat perintah yang tersedia")

def ping_handler(msg):
    bot.reply_to(msg, "<b>PONG!</b>")
=======
def send_info(message):
    ingfo = "<b>Info Pengguna</b>\n\n👤 ID Pengguna: <code>"+str(message.from_user.id)+"</code>\n🙋 Nama depan: "+message.from_user.first_name+"\n💁🏼 Nama Belakang: "+message.from_user.last_name+"\n🤡 Username: @"+message.from_user.username+"\n🔗 Link: <a href='tg://user?id="+str(message.from_user.id)+"'>link</a>"
    bot.reply_to(message, ingfo)

def send_translation(msg, reg):
    print(msg)
    if msg.reply_to_message != None:
        if msg.reply_to_message.text != None:
            teks = msg.reply_to_message.text
        else:
            teks = msg.caption
    try:
        smntr = tr.translate(teks, dest=reg[3])
        hasil = "Diterjemahkan dari <code>" + smntr.src + "</code>\n\n" + smntr.text + "</code>"
        bot.reply_to(msg, hasil)
    except:
        pesan = "Ups, tidak ada kode bahasa: <code>" + reg[3] + "</code>. Kalau mau tau kode bahasa, coba cek <a href='https://telegra.ph/kode-kode-bahasa-08-09'>di sini</a> deh."
        bot.reply_to(msg, pesan)
>>>>>>> 059687cbda8291fff57da7be2b2ba9a7dfdce946

def translate_handler(msg, rex):
    tujuan = rex[3]
    if rex[3] in languages_code:
        hasil = tr(msg.message.text, dest=tujuan)
        hasil_terjemahan = "Ditranslate dari <code>" + hasil.src + "</code>\n\n" + hasil.text
        bot.reply_to(msg, hasil_terjemahan)
    else:
<<<<<<< HEAD
        hasil_terjemahan = "Maaf, kayaknya kode bahasa <code>" + tujuan + "</code> nggak ada deh. \n\nUntuk mengetahui kode bahasa lebih lanjut, <a href='https://telegra.ph/Kode-kode-Bahasa-08-09'>cek disini deh</a>"
        bot.reply_to(msg, hasil_terjemahan)

#message handlers
@bot.message_handler(content_types=['text', 'photo', 'video', 'sticker'])
def handler(msg):
    pesan = msg.text
    pola = "^[,./!]start(|@zipra_bot)$"
    if reg(pola, pesan):
        start_handler(msg)
    pola = "^[,./!]ping(|@zipra_bot)$"
    if reg(pola, pesan):
        ping_handler(msg)
    pola = "^[,./!](tl|tr|trans|translate)(|@zipra_bot)\s+(.{2,5})$"
    if reg(pola, pesan):
        translate_handler(msg, res(pola))
=======
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
    pola = "^[,./!](tr|tl|trans|translate)(|@zipra_bot)\s+(\w+)"
    if re.search(pola, pesan):
        send_translation(message, re.split(pola, pesan))
    pola = "^[,./!]help(|@zipra_bot)\s{0,}(\w{0,})"
    if re.search(pola, pesan):
        send_help(message, re.split(pola, pesan))
>>>>>>> 059687cbda8291fff57da7be2b2ba9a7dfdce946

bot.polling()
