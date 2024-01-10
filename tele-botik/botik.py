import telebot
from telebot import types
import time

bot = telebot.TeleBot('TOKEN')

# Остальной код без изменений до этого момента...

# Изменения в функции check_forbidden_words
forbidden_words = ['хуe', 'xyе', 'хyй', 'xyй', 'хуй', 'бля', 'хуе', 'еба', 'xуй', 'xуе', 'eба', 'пизд', 'ебa', 'дота', 'ебa', 'военкомат']  # Замените на свой список запрещенных слов

def check_forbidden_words(message):
    user_id = message.from_user.id
    user_text = message.text.lower()

    if any(word in user_text for word in forbidden_words):
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.send_message(message.chat.id,
                         f"Пользователь @{message.from_user.username} замучен на час за использование запрещенных слов.")
        mute_user_1(user_id, message.chat.id)

# Изменения в функции mute_user_1
def mute_user_1(user_id, chat_id):
    user_status = bot.get_chat_member(chat_id, user_id).status
    if user_status not in ('administrator', 'creator'):
        bot.restrict_chat_member(chat_id, user_id, can_send_messages=False, can_send_media_messages=False,
                                 can_send_other_messages=False, can_add_web_page_previews=False)

# Изменения в функции mute_user
@bot.message_handler(commands=['mute'])
def mute_user(message):
    user_status_main = bot.get_chat_member(message.chat.id, message.from_user.id).status
    if user_status_main in ('administrator', 'creator') and message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status not in ('administrator', 'creator'):
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
            bot.restrict_chat_member(chat_id, user_id, can_send_messages=False, can_send_media_messages=False,
                                     can_send_other_messages=False, can_add_web_page_previews=False)
            bot.reply_to(message,
                         f"Пользователь {message.reply_to_message.from_user.username} замучен на {duration} минут.")
        else:
            bot.reply_to(message, "Невозможно замутить администратора.")
    else:
        bot.reply_to(message, "Вы должны быть администратором и использовать команду в ответ на сообщение пользователя.")


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


@bot.message_handler(commands=['send_message'])
def spam_input(message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        bot.reply_to(message, "Введите сообщение в личную переписку с ботом")

    else:
        if message.from_user.username == "re_smx":
            sent = bot.send_message(message.from_user.id, "Введите id группы")
            bot.register_next_step_handler(sent, get_id)
        else:
            bot.reply_to(message, "Вы должны обладать правами супер пользователя!")


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
        file = open(filePath, 'a')
        message_user = f"Пользователь @{message.from_user.username} в группе <<{message.chat.title}>> пишет: {message.text}  "
        file.write(message_user)
        file.write("\n")
    check_forbidden_words(message)

def mute_user_1(user_id_get, chat_id):
    user_status = bot.get_chat_member(chat_id, user_id_get).status
    if user_status == 'administrator' or user_status == 'creator':
        bot.send_message("Невозможно замутить администратора.")
    else:
        bot.restrict_chat_member(chat_id, user_id_get, can_send_messages=False, can_send_media_messages=False,
                                 can_send_other_messages=False, can_add_web_page_previews=False)


bot.infinity_polling(none_stop=True, interval=0)
