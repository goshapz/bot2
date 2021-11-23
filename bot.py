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
    # base.register_user(message.from_user.first_name, message.from_user.last_name, message.chat.id)
    bot.send_message(message.chat.id, 'Выберите на какие дни нужно расписание.', reply_markup=keyboard)


@bot.message_handler(commands=['week'])
def start(message):
    bot.send_message(message.chat.id, date.get_week())
    # base.register_user(message.from_user.first_name, message.from_user.last_name, message.chat.id)


'''
<День недели>
    ____________
<Предмет> <Кабинет> <Время> <Преподаватель>
…
<Предмет> <Кабинет> <Время> <Преподаватель>
'''


@bot.message_handler(content_types=['text'])
def answer_day(message):
    t = message.text.lower()
    if t == 'понедельник' or t == 'вторник' or t == 'среда' or t == 'четверг' \
            or t == 'пятница':
        tt = str.capitalize(t)
        l = base.return_len(tt)
        records = base.subj_time(tt)
        mes = ''
        if int(l[1]) > 0:
            mes = ((str(tt) + ' \n' + '-------------------\n'
                    + str(records[0][0]) + ' ' + str(records[0][1])
                    + ' ' + records[0][2].strftime('%H:%M') + ' '
                    + str(base.return_teacher(records[0][0])).replace("('", '')
                    .replace("',)", '') + '\n' + '\n'))
            if int(l[1]) > 1:
                mes = mes + ((records[1][0] + ' ' + records[1][1]
                              + ' ' + records[1][2].strftime('%H:%M') + ' '
                              + base.return_teacher(records[1][0]).replace("('", '')
                              .replace("',)", '') + '\n' + '\n'))
                if int(l[1]) > 2:
                    mes = mes + ((records[2][0] + ' ' + records[2][1]
                                  + ' ' + records[2][2].strftime('%H:%M') + ' '
                                  + base.return_teacher(records[2][0]).replace("('", '')
                                  .replace("',)", '')
                                  + '\n' + '\n'))
                    if int(l[1]) > 3:
                        mes = mes + str((records[3][0] + ' ' + records[3][1]
                                         + ' ' + records[3][2].strftime('%H:%M') + ' '
                                         + base.return_teacher(records[3][0]).replace("('", '')
                                         .replace("',)", '') + '\n'))
        bot.send_message(message.chat.id, str(mes))


bot.infinity_polling()
