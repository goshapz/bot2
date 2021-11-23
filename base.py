import psycopg2
import date
from dotenv import load_dotenv
import os

load_dotenv()
db = os.getenv("DATABASE")
us = os.getenv("USR")
pas = str(os.getenv("PASSWORD"))
ht = os.getenv("HOST")
pt = os.getenv("PORT")
conn = psycopg2.connect(database=db,
                        user=us,
                        password=pas,
                        host=ht,
                        port=pt)

cursor = conn.cursor()


def register_user(a, b, c):
    username = (a + ' ' + b)
    cursor.execute("SELECT * from telusers WHERE chat_id =%s", (str(c),))
    records = list(cursor.fetchall())
    if not records:
        cursor.execute('insert into telusers(chat_id, username) VALUES (%s, %s);',
                       (str(c), str(username)))
        conn.commit()


def subj_time(a):
    if date.get_week() == 'Неделя - нижняя':
        a = a + 'Н'
        return return_timetable(a)
    else:
        a = a + 'В'
        return return_timetable(a)


def return_teacher(a):
    cursor.execute("SELECT full_name from teacher WHERE subject=%s", (str(a),))
    records = str(cursor.fetchone())
    return records


def return_len(a):
    if date.get_week() == 'Неделя - нижняя':
        cursor.execute("SELECT count(*) from timetable WHERE day=%s", (str(a + 'Н'),))
    if date.get_week() == 'Неделя - верхняя':
        cursor.execute("SELECT  count(*) from timetable WHERE day=%s", (str(a + 'В'),))
    records = str(cursor.fetchone())
    return records


def return_timetable(a):
    cursor.execute("SELECT subject, room_numb, start_time from timetable WHERE day=%s", (str(a),))
    records = list(cursor.fetchall())
    return records
