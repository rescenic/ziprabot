# Ziprabot

Sebuah proyek bot telegram yang menggunakan library [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

## Menjalankan secara local

Pastikan kamu sudah menginstall [Python 3.9](https://docs.python-guide.org/starting/installation/) dan git CLI. Tutorial ini bisa mencakup di Linux, macOS, Windows, dan Android (Termux)

```sh
$ git clone https://github.com/ridhwan-aziz/ziprabot.git
$ cd ziprabot
```
Lalu, buat bot di [@BotFather](https://t.me/BotFather). Lalu isi TOKEN di .env

Jalankan bot

```sh
$ pip install -Ur requirements.txt
$ python bot.py
```

## Deploy ke Heroku

Khusus pengguna termux, install termux melalui nodejs

```sh
$ pkg update -y
$ pkg install nodejs
$ npm i -g heroku
```
Cara deploy

```sh
$ heroku create [NAMA_APP]
$ git push heroku main

$ heroku run python bot.py
```
atau

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
