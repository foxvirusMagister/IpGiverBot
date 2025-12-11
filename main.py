import subprocess
import os
import telebot
from dotenv import load_dotenv


load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"), parse_mode=None)
password = hash(os.getenv("PASSWD"))
owner_name = hash(os.getenv("OWNER"))
phrase = hash(os.getenv("PHRASE"))
try:
    useown = int(os.getenv("USEOWN"))
except ValueError:
    print("Неверный формат .env файла, части USEOWN")
    print("Ожидается 0 или 1")
    raise


@bot.message_handler(commands=["start"])
def greeter(message):
    '''message that bot send on your /start command'''
    bot.reply_to(message, "Hello, pass first then code")


@bot.message_handler(func=lambda i: True)
def check_message(message):
    '''main message check'''
    words = message.text.split(" ")
    try:
        if len(words) == 2:
            code = hash(words[1])
            passwd = hash(words[0])
            if passwd == password and not useown and code == phrase:
                ip = subprocess.run(["curl", "ifconfig.me"], capture_output=True, text=True, check=True)
                bot.reply_to(message, ip.stdout)
        elif len(words) == 1:
            usrname = hash(message.from_user.username.lower())
            code = hash(words[0])
            if useown and usrname == owner_name and code == phrase:
                ip = subprocess.run(["curl", "ifconfig.me"], capture_output=True, text=True, check=True)
                bot.reply_to(message, ip.stdout)
    except subprocess.CalledProcessError as e:
        print("Произошла ошибка")
        print(e.stderr)
        bot.reply_to(message, "Извините, произошла ошибка!")


if __name__ == "__main__":
    bot.infinity_polling()
