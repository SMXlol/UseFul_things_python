import telebot
from telebot import types
import time

bot = telebot.TeleBot(
    '5813989102:AAGC6F9pb4uNRxT_4J4CVX92N7Yu6igR5ZA')  # в TOKEN мы вводим непосредственно сам полученный токен.

chat_id_spam = 0
spam_message = "0"


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Помощь")
    btn2 = types.KeyboardButton("❓ А у создателя есть тг канал???")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, Я бот для управления чатом. Используй кнопки внизу чтобы узнать больше...".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,
                 "/kick - кикнуть пользователя\n/mute - замутить пользователя на определенное время\n/unmute - "
                 "размутить пользователя\n/get_id - получить никнейм, id группы и id  человека\n/spam - отправка "
                 "сообщений в группу через бота")


@bot.message_handler(commands=['kick'])
def kick_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно кикнуть администратора.")
        else:
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} был кикнут.")
    else:
        bot.reply_to(message,
                     "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите кикнуть.")


@bot.message_handler(commands=['mute'])
def mute_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно замутить администратора.")
        else:
            duration = 60  # Значение по умолчанию - 1 минута
            args = message.text.split()[1:]
            if args:
                try:
                    duration = int(args[0])
                except ValueError:
                    bot.reply_to(message, "Неправильный формат времени.")
                    return
                if duration < 1:
                    bot.reply_to(message, "Время должно быть положительным числом.")
                    return
                if duration > 1440:
                    bot.reply_to(message, "Максимальное время - 1 день.")
                    return
            bot.restrict_chat_member(chat_id, user_id, until_date=time.time() + duration * 60)
            bot.reply_to(message,
                         f"Пользователь {message.reply_to_message.from_user.username} замучен на {duration} минут.")
    else:
        bot.reply_to(message,
                     "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите замутить.")
@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True,
                                 can_send_other_messages=True, can_add_web_page_previews=True)
        bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} размучен.")
    else:
        bot.reply_to(message,
                     "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите размутить.")


@bot.message_handler(commands=['spam'])
def spam_input(message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        bot.reply_to(message, "Введите сообщение в личную переписку с ботом")

    else:
        sent = bot.send_message(message.from_user.id, "Введите id группы")
        bot.register_next_step_handler(sent, get_id)


def get_id(message):
    global chat_id_spam
    chat_id_spam = message.text
    sent = bot.send_message(message.from_user.id, "Введитe сообщение которым вы хотите спамить")
    bot.register_next_step_handler(sent, spam_message1)
    return chat_id_spam


def spam_message1(message):
    global spam_message
    spam_message = str(message.text)
    sent = bot.send_message(message.from_user.id, "Введитe кол-во сообщений")
    bot.register_next_step_handler(sent, cout)


def cout(message):
    x = 0
    spam = int(message.text)
    print("GG", spam)
    print("GG", spam_message)
    print('GG', chat_id_spam)
    user_id = message.from_user.username
    print(user_id)
    chat_id = chat_id_spam
    for i in range(spam):
        bot.send_message(chat_id=chat_id, text=spam_message)
        time.sleep(2)
        x = x + 1
    j = str(x)
    bot.send_message(message.from_user.id, "Спам завершён!")
    bot.send_message(message.from_user.id, j)


# получаем ай ди пользователя и чата
@bot.message_handler(commands=['get_id'])
def user_id(message):
    if message.reply_to_message:
        user_id_get = message.reply_to_message.from_user.id
        chat_id_get = message.chat.id
        bot.send_message(chat_id_get,
                         f'id чата: {chat_id_get}, id пользователя {message.reply_to_message.from_user.username}: {user_id_get}')


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "👋 Помощь":
        bot.send_message(message.chat.id, text="Привеет... Держи помощь!!!)")
        help(message)
    elif message.text == "❓ А у создателя есть тг канал???":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Канал S(MI)X", url='https://t.me/SMXrehub')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "Привет, нажми на кнопку и перейди в тг канал))))".format(message.from_user),
                         reply_markup=markup)
    else:
        filePath = 'chat_history.txt'
        file = open(filePath, 'w')
        message_user = f"Пользователь {message.from_user.username} пишет: {message.text}  "
        file.write(message_user)
        file.write("\n")


bot.infinity_polling(none_stop=True)