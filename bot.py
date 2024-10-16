import telebot
from telebot import types

bot = telebot.TeleBot('7409547676:AAHL1hZVam5v9PUJteN4E-q9FNvzYy06YWE')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message( message.chat.id, 'Привет и Добро пожаловать в True sight 👁 \nНажми на START что бы начать.', parse_mode="Markdown")

bot.polling(none_stop=True)