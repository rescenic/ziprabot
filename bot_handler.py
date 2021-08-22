from datetime import datetime
from bot_env import *

def start_handler(msg):
    if chattype != "private":
        bot.reply_to(msg, "Ya, PM saya aja kalo pengen liat perintah yang tersedia")
    else:
        bot.reply_to(msg, start)

def ping_handler(msg):
    waktu_awal = datetime.utcfromtimestamp(int(msg.date))
    pesan = bot.reply_to(msg, "<b>PONG!</b>")
    waktu_akhir = datetime.now()
    total_waktu = waktu_akhir - waktu_awal
    hasil = "<b>PONG!</b>\n\n⌛️<code>" + str(total_waktu.total_seconds()) + "</code> detik"
    bot.edit_message_text(hasil, chatid, pesan.message_id)

def translate_handler(msg, rex):
    tujuan = rex[3]
    if rex[3] in languages_code:
        hasil = tr(msg.reply_to_message.text, dest=tujuan)
        hasil_terjemahan = "Ditranslate dari <code>" + hasil.src + "</code>\n\n" + hasil.text
        bot.reply_to(msg, hasil_terjemahan)
    else:
        hasil_terjemahan = "Maaf, kayaknya kode bahasa <code>" + tujuan + "</code> nggak ada deh. \n\nUntuk mengetahui kode bahasa lebih lanjut, <a href='https://telegra.ph/Kode-kode-Bahasa-08-09'>cek disini deh</a>"
        bot.reply_to(msg, hasil_terjemahan)


def ud_handler_extra(hasil, ln, lists):
    for i in range(ln):
        hasil += "<a href='" + lists[i].get("permalink") + "'><b>DEFINITION #"+str(i+1)+"</b></a>:\n"+lists[i].get("definition")+"\n\n<b>EXAMPLE</b>:\n"+lists[i].get("example")+"\n\n\n"
    return hasil

def ud_handler(msg, rex):
    word = rex[1]
    r = requests.get(UD_API.format(word)).json()
    lists = r.get("list")
    result = "Word: " + word + "\n\n"
    if len(lists) == 0:
        bot.reply_to(msg, "UrbanDictionary for {} isn't available".format(word))
    elif len(lists) < 3:
        length = len(lists)
        result = ud_handler_extra(result, length, lists)
        bot.reply_to(msg, result)
    else:
        length = 3
        hasil = ud_handler_extra(result, length, lists)
        bot.reply_to(msg, result)

def adminlist_handler(msg):
    if chattype == "private":
        return bot.send_message(chatid, "{}".format(adminlisterror))
    result = bot.reply_to(msg, "Mengloading.....")
    admins = bot.get_chat_administrators(chatid)
    pesan = "❗️Anggota di <b> {} </b>❗️\n".format(title)
    for i in admins:
        nama = str(i.user.first_name)
        status = i.status
        if i.custom_title == None:
            custom_title = "Admin"
        else:
            custom_title = i.custom_title
        pesan += "✅{} sebagai <b>{}</b>[<code>{}</code>]\n".format(nama, status, custom_title)
    pesan += "\n<b>🔰 Jumlah anggota</b>: {}".format(bot.get_chat_members_count(chatid))
    bot.edit_message_text(pesan, chatid, result.message_id)

#message handlers
@bot.message_handler(regexp=".+", content_types=['text', 'photo', 'video', 'sticker'])
def handler(msg):
    global chatid, title, chattype
    chattype = msg.chat.type
    chatid = msg.chat.id
    title = msg.chat.title
    pesan = msg.text
    try:
        pola = r"^[,./!]start(|@zipra_bot)$"
        if reg(pola, pesan, i):
            start_handler(msg)
        pola = r"^[,./!]ping(|@zipra_bot)$"
        if reg(pola, pesan, i):
            ping_handler(msg)
        pola = r"^[,./!](tl|tr|trans|translate)(|@zipra_bot)\s+(.{2,5})$"
        if reg(pola, pesan, i):
            translate_handler(msg, res(pola, pesan))
        pola = r"^[,./!]ud\s+(.+)"
        if reg(pola, pesan, i):
            ud_handler(msg, res(pola, pesan))
        pola = r"^[,./!]adminlist$"
        if reg(pola, pesan, i):
            adminlist_handler(msg)
    except Exception as e:
        bot.send_message(msg.chat.id, "<code>"+str(e)+"</code>")

bot.polling()
