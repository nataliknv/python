duration = int(input ('Введите время в секундах:'))
if duration < 60:
    print(duration, ' сек')
elif (duration > 59) and (duration < 3600):
    min = duration // 60
    sec = duration % 60
    print(min, 'мин', sec, 'сек')
elif (duration > 3599) and (duration < 86400):
    sec = duration % 60
    hour = duration // 3600
    min = duration // 60 % 60
    print(hour, 'час', min, 'мин', sec, 'сек')
else:
    sec = duration % 60
    day = duration // 86400
    hour = (duration - (day*86400)) // 3600
    min = duration // 60 % 60
    print(day, 'дн', hour, 'час', min, 'мин', sec, 'сек')




