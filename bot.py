import jwt
import telebot
from django.urls import reverse


bot = telebot.TeleBot('7409547676:AAHL1hZVam5v9PUJteN4E-q9FNvzYy06YWE')


def handle_start(message):
    user_telegram_id = message.from_user.id
    user_name = message.from_user.first_name

    # Отправка запроса к API Django
    login_url = f"{reverse('login')}?telegram_id={user_telegram_id}&username={user_name}" # Добавлен username

    bot.send_message(message.chat.id, f"Авторизуйтесь на сайте: {login_url}")

@bot.message_handler(commands=['start'])
def handle_start(message):
    handle_start(message)

@bot.message_handler(func=lambda message: message.text.startswith('/login'))
def handle_login(message):
    # Получение токена из сообщения
    token = message.text.split()[1]

    # Проверка токена
    try:
        # Проверка токена
        decoded_token = jwt.decode(token, 'django-insecure-+)g(0g+=!#i%*coegez9^-*u6n5=o+fv7qd3#_iws#lql$=2sn', algorithms=['HS256'])

        # Успешная авторизация
        bot.send_message(message.chat.id, 'Вы успешно авторизованы!')

    except:
        bot.send_message(message.chat.id, 'Неверный токен')

bot.polling(none_stop=True)