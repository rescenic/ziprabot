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

def start_handler(msg):
    if msg.chat.type != "private":
        bot.reply_to(msg, "Ya, PM saya aja kalo pengen liat perintah yang tersedia")

def ping_handler(msg):
    bot.reply_to(msg, "<b>PONG!</b>")

def translate_handler(msg, rex):
    tujuan = rex[3]
    if rex[3] in languages_code:
        hasil = tr(msg.message.text, dest=tujuan)
        hasil_terjemahan = "Ditranslate dari <code>" + hasil.src + "</code>\n\n" + hasil.text
        bot.reply_to(msg, hasil_terjemahan)
    else:
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

bot.polling()
