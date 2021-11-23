from dotenv import load_dotenv
import os
import telebot
from telebot import TeleBot
import base
import date

load_dotenv()
token = os.getenv("ACCESS_TOKEN")
bot: TeleBot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Понедельник", "Вторник")
    keyboard.row("Среда", "Четверг", 'Пятница')
    keyboard.row('Расписание на текущую неделю', 'Расписание на следующую неделю')
    base.register_user(message.from_user.first_name, message.from_user.last_name, message.chat.id)
    bot.send_message(message.chat.id, 'Здраствуйте', reply_markup=keyboard)


@bot.message_handler(commands=['week'])
def start(message):
    bot.send_message(message.chat.id, date.get_week())
    base.register_user(message.from_user.first_name, message.from_user.last_name, message.chat.id)


'''
<День недели>
    ____________
<Предмет> <Кабинет> <Время> <Преподаватель>
…
<Предмет> <Кабинет> <Время> <Преподаватель>
'''


@bot.message_handler(content_types=['text'])
def answer_day(message):
    if message() == 'Понедельник' or message() == 'Вторник' or message()\
            == 'Среда' or message() == 'Четвер' or message() == 'Пятница':
        l = base.return_len(message)
        records = base.subj_time(message)
        if l > 0:
            mes = (message.chat.id, (message + '\n' + '____________\n'
                                           + records[0][0] + ' ' + records[0][1]
                                     + ' ' + records[0][2] + ' ' + base.return_teacher(records[0][0]) + '\n'))
            if l > 1:
                mes = mes + (message.chat.id, (+ records[1][0] + ' ' + records[1][1]
                                         + ' ' + records[1][2] + ' ' + base.return_teacher(records[1][0]) + '\n'))
                if l > 2:
                    mes = mes + (message.chat.id, (+ records[2][0] + ' ' + records[2][1]
                                                   + ' ' + records[2][2] + ' ' + base.return_teacher(
                                records[2][0]) + '\n'))
                    if l > 3:
                        mes = mes + (message.chat.id, (+ records[3][0] + ' ' + records[3][1]
                                                       + ' ' + records[3][2] + ' ' + base.return_teacher(
                                    records[3][0]) + '\n'))
        bot.send_message(message.chat.id, mes)


bot.infinity_polling()
