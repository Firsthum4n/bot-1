import telebot
from telebot import types

from keyboard import webAppKeyboard
import requests
from urllib.parse import urlencode


bot = telebot.TeleBot('7409547676:AAHL1hZVam5v9PUJteN4E-q9FNvzYy06YWE')


@bot.message_handler(commands=['start'])
def start_handler(message):
    user = message.from_user
    telegram_id = user.id
    telegram_username = user.first_name

    params = {
        'telegram_id': telegram_id,
        'telegram_username': telegram_username
    }
    bot.send_message(message.chat.id, 'Привет, Нажми на кнопку TRUE SIGHT что бы узнать кто победит или menu что бы узнать больше ', reply_markup=webAppKeyboard(params))




if __name__ == '__main__':
   bot.infinity_polling()