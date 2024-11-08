import telebot
from telebot import types
from urllib.parse import urlencode


def webAppKeyboard(params):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    webApplink = types.WebAppInfo(f"https://trusight.ru/users/api//register?{urlencode(params)}")
    one_butt = types.KeyboardButton(text="💥TRUE SIGHT💥", web_app=webApplink)
    keyboard.add(one_butt)
    return keyboard
