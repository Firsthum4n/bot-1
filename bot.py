import telebot
from telebot import types

bot = telebot.TeleBot('7409547676:AAHL1hZVam5v9PUJteN4E-q9FNvzYy06YWE')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message( message.chat.id, 'Привет, медвед????)\n????', parse_mode="Markdown", reply_markup=webAppKeyboard())


def webAppKeyboard():  # создание клавиатуры с webapp кнопкой
    keyboard = types.ReplyKeyboardMarkup(row_width=1)  # создаем клавиатуру
    webAppTest = types.WebAppInfo("https://trusight.ru")  # создаем webappinfo - формат хранения url
    one_butt = types.KeyboardButton(text="Т", web_app=webAppTest)  # создаем кнопку типа webapp
    keyboard.add(one_butt)  # добавляем кнопки в клавиатуру

    return keyboard  # возвращаем клавиатуру


bot.polling(none_stop=True)