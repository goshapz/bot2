from datetime import datetime, timedelta


def get_week():
    now = datetime.now()
    sep = datetime(now.year if now.month >= 9 else now.year - 1, 9, 1)
    d1 = sep - timedelta(days=sep.weekday())
    d2 = now - timedelta(days=now.weekday())
    parity = ((d2 - d1).days // 7) % 2
    return "Неделя - {}".format("нижняя" if parity else "верхняя")


def get_nextweek():
    now = datetime.now() + timedelta(days=7)
    sep = datetime(now.year if now.month >= 9 else now.year - 1, 9, 1)
    d1 = sep - timedelta(days=sep.weekday())
    d2 = now - timedelta(days=now.weekday())
    parity = ((d2 - d1).days // 7) % 2
    return "Неделя - {}".format("нижняя" if parity else "верхняя")
