import requests, re, os, telebot
from googletrans import Translator
from datetime import datetime

#Setup Environment
UD_API = "http://api.urbandictionary.com/v0/define?term={}"
i = re.IGNORECASE
bot = telebot.TeleBot(os.environ.get("TOKEN"), parse_mode="HTML")
reg = re.search
res = re.split
tr = Translator().translate
languages_code = ['auto', 'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
if LOG_CHANNEL == None:
    raise ValueError("LOG_CHANNEL isn't specified!")

#Strings
adminlisterror = "Tidak bisa menampilkan Admin di private chat😡"
start = "Halo, perkenalkan namaku " + bot.get_me().first_name + ".\nSaya masih dalam pengembangan oleh @Pra210906\n\nKetik /help untuk melihat bantuan"
bantu = "Bantuan tersedia:\n\n<code>ping, translate</code>\n\nKamu bisa menggunakan titik(.), koma(,), garing(/), dan seru(!)."