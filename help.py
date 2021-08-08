#Strings
ping = "Perintah: <code>/ping</code>\n\nUntuk mengecek apakah botnya aktif atau tidak."
translate_string = "Perintah: <code>/tr /tl /trans /translate</code>\n\nReply ke suatu pesan untuk mentranslate teks. Info tentang list kode bahasa <a href='https://www.google.com'>di sini</a>\n\nContoh: /tr en"

#list
list_help={'ping': ping, 'translate': translate_string}

#def
def get_help(hlp):
  return list_help[hlp]
