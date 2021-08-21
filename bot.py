import telebot, re, os, requests
from googletrans import Translator
from datetime import datetime

#Setup Environment
UD_API = "http://api.urbandictionary.com/v0/define?term={}"
i = re.IGNORECASE
reg = re.search
res = re.split
t = telebot.TeleBot(os.environ.get('TOKEN'), parse_mode="HTML")
tr = Translator().translate
bot = telebot.TeleBot(os.environ.get('TOKEN'), parse_mode="HTML")
languages_code = ['auto', 'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
if LOG_CHANNEL == None:
    raise ValueError("LOG_CHANNEL isn't specified!")

#Strings
start = "Halo, perkenalkan namaku " + bot.get_me().first_name + ".\nSaya masih dalam pengembangan oleh @Pra210906\n\nKetik /help untuk melihat bantuan"
bantu = "Bantuan tersedia:\n\n<code>ping, translate</code>\n\nKamu bisa menggunakan titik(.), koma(,), garing(/), dan seru(!)."

print("---BOT STARTED---")
bot.send_message(LOG_CHANNEL, "@zipra_bot started successfully!")

# function handlers
def start_handler(msg):
    if msg.chat.type != "private":
        bot.reply_to(msg, "Ya, PM saya aja kalo pengen liat perintah yang tersedia")

def ping_handler(msg):
    waktu_awal = datetime.utcfromtimestamp(int(msg.date))
    pesan = bot.reply_to(msg, "<b>PONG!</b>")
    waktu_akhir = datetime.now()
    total_waktu = waktu_akhir - waktu_awal
    hasil = "<b>PONG!</b>\n\n⌛️<code>" + str(total_waktu.total_seconds()) + "</code> detik"
    bot.edit_message_text(hasil, msg.chat.id, pesan.message_id)

def translate_handler(msg, rex):
    tujuan = rex[3]
    if rex[3] in languages_code:
        hasil = tr(msg.reply_to_message.text, dest=tujuan)
        hasil_terjemahan = "Ditranslate dari <code>" + hasil.src + "</code>\n\n" + hasil.text
        bot.reply_to(msg, hasil_terjemahan)
    else:
        hasil_terjemahan = "Maaf, kayaknya kode bahasa <code>" + tujuan + "</code> nggak ada deh. \n\nUntuk mengetahui kode bahasa lebih lanjut, <a href='https://telegra.ph/Kode-kode-Bahasa-08-09'>cek disini deh</a>"
        bot.reply_to(msg, hasil_terjemahan)

def bc_handler(msg, rex):
    hitungan = rex[1]
    try:
        hasil = eval(hitungan)
        bot.reply_to(msg, hasil)
    except Exception as e:
        bot.reply_to(msg, "<code>" + str(e) + "</code>")

def ud_handler_extra(hasil, ln, lists):
    for i in range(ln):
        hasil += "<a href='" + lists[i].get("permalink") + "'><b>DEFINITION #"+str(i+1)+"</b></a>:\n"+lists[i].get("definition")+"\n\n<b>EXAMPLE</b>:\n"+lists[i].get("example")+"\n\n\n"
    return hasil

def ud_handler(msg, rex):
    word = rex[1]
    try:
        r = requests.get(UD_API.format(word)).json()
    except Exception as e:
        bot.reply_to(msg, "<code>" + str(e) + "</code>")
    lists = r.get("list")
    hasil = "Word: "+word+"\n\n"
    if len(lists)==0:
        bot.reply_to(msg, "UrbanDictionary for " + word + " isn't available")
    elif len(lists) < 3:
        length = len(lists)
        hasil = ud_handler_extra(hasil, length, lists)
        bot.reply_to(msg, hasil)
    else:
        length = 3
        hasil = ud_handler_extra(hasil, length, lists)
        bot.reply_to(msg, hasil)

def adminlist_handler(msg):
    chat_id = msg.chat.id
    result = bot.reply_to(msg, "Mengloading....")
    isi = bot.get_chat_administrators(chat_id)
    hasil = "Daftar admin di grup <code>" + msg.chat.title + "</code>\n\n"
    for i in isi:
        nama = str(i.user.first_name)
        status = i.status
        if i.custom_title == None:
            custom_title = "Admin"
        else:
            custom_title = i.custom_title
        hasil += nama + " sebagai <b>" + status + "</b> [<code>" + custom_title + "</code>]\n"
    bot.edit_message_text(hasil, chat_id, result.message_id)
        

#message handlers
@bot.message_handler(regexp=".+", content_types=['text', 'photo', 'video', 'sticker'])
def handler(msg):
    try:
        pesan = msg.text
        pola = r"^[,./!]start(|@zipra_bot)$"
        if reg(pola, pesan, i):
            start_handler(msg)
        pola = r"^[,./!]ping(|@zipra_bot)$"
        if reg(pola, pesan, i):
            ping_handler(msg)
        pola = r"^[,./!](tl|tr|trans|translate)(|@zipra_bot)\s+(.{2,5})$"
        if reg(pola, pesan, i):
            translate_handler(msg, res(pola, pesan))
        pola = r"^[,./!]bc\s+(.+)"
        if reg(pola, pesan, i):
            bc_handler(msg, res(pola, pesan))
        pola = r"^[,./!]ud\s+(.+)"
        if reg(pola, pesan, i):
            ud_handler(msg, res(pola, pesan))
        pola = r"^[,./!]adminlist$"
        if reg(pola, pesan, i):
            adminlist_handler(msg)
    except Exception as e:
        bot.send_message(msg.chat.id, "<code>" + str(e) + "</code>")

bot.polling()
