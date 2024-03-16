from telebot import *
import re

key = '6832492619:AAGiws8xtXKx_4mz3wZb6UsvMHKGbU4XojM'
bot = telebot.TeleBot(key)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     text="Привет, Я бот обнаружения в ваших сообщениях регулярных выражений")
