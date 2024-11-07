import telebot
import requests
from urllib.parse import urlencode


bot = telebot.TeleBot('7409547676:AAHL1hZVam5v9PUJteN4E-q9FNvzYy06YWE')



API_URL = 'http://trusight.ru/users/api/'

@bot.message_handler(commands=['start'])
def start_handler(message):
    user = message.from_user
    telegram_id = user.id
    telegram_username = user.username

    # Создание ссылки для авторизации
    params = {
        'telegram_id': telegram_id,
        'telegram_username': telegram_username
    }
    url = f"{API_URL}/register?{urlencode(params)}"

    bot.send_message(message.chat.id, f"Перейдите по этой ссылке, чтобы авторизоваться: {url}")



bot.polling(none_stop=True)