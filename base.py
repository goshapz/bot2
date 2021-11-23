import psycopg2
import date

conn = psycopg2.connect(database="botdb",
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


def register_user(a: object, b: object, c: object) -> object:
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
        return_timetable(a)
    else:
        a = a + 'В'
        return_timetable(a)


def return_teacher(a):
    cursor.execute("SELECT full_name from teacher WHERE subject=%s", (str(a),))
    records = str(cursor.fetchall())


def return_len(a):
    cursor.execute("SELECT subject, room_numb, start_time from timetable WHERE day=%s", (str(a),))
    records = list(cursor.fetchall())
    return len(records)


def return_timetable(a):
    cursor.execute("SELECT subject, room_numb, start_time from timetable WHERE day=%s", (str(a),))
    records = list(cursor.fetchall())
    return records
