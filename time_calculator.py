"""_summary_
"""


def add_time(start, duration, day=None):
    """_summary_

    Args:
        start (_type_): _description_
        duration (_type_): _description_
        day (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    horas_start = int(start.split(':')[0])
    minutos_start = int(start.split(':')[1][0:2])
    pm_am = start.split(' ')[1]

    horas_duration = int(duration.split(':')[0])
    minutos_duration = int(duration.split(':')[1])

    minutos_novo = minutos_start+minutos_duration

    horas_novo = 0
    if minutos_novo > 60:
        horas_novo = minutos_novo//60
        minutos_novo = minutos_novo % 60
    if len(str(minutos_novo)) == 1:
        minutos_novo = '0' + str(minutos_novo)

    horas_novo = horas_novo+horas_duration+horas_start

    week = ['Sunday', 'Monday', 'Tuesday',
            'Wednesday', 'Thursday', 'Friday', 'Saturday']
    dia = 0
    contagem_dias = 0
    days_later = ''

    if day is not None:
        day = day.lower()
        day = day.capitalize()
        dia = week.index(day)

    while horas_novo > 12:
        horas_novo = horas_novo - 12
        if pm_am == 'PM':
            dia += 1
            contagem_dias += 1
            if dia > 6:
                dia = 0

            pm_am = 'AM'
        else:
            pm_am = 'PM'

    if horas_novo == 12:
        if pm_am == 'AM':
            pm_am = 'PM'
        else:
            pm_am = 'AM'
            contagem_dias += 1
            dia += 1

    if contagem_dias != 0:
        if contagem_dias == 1:
            days_later = ' (next day)'
        else:
            days_later = ' ('+str(contagem_dias)+' days later)'

    if day is not None:
        day = week[dia]
        new_time = str(horas_novo)+':'+str(minutos_novo) + ' ' + \
            pm_am+', '+day+days_later
    else:
        new_time = str(horas_novo)+':'+str(minutos_novo) + \
            ' '+pm_am+days_later

    return new_time


print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))
