#Strings
ping = "Perintah: <code>/ping</code>\nPola: <code>^[,./!]ping(|@zipra_bot)$</code>\n\nUntuk mengecek apakah botnya aktif atau tidak."

#list
list_help={'ping': ping}

#def
def get_help(hlp):
  return list_help[hlp]
