sec = int(input("Введите количество секунд: "))

hour = sec//3600
ost = sec % 3600
min = ost//60
sec = ost % 60

hour = str(hour)
hour_l = len(hour)
if len(hour) < 2:
    hour = "0"+hour

min = str(min)
min_l = len(min)
if len(min) < 2:
    min = "0"+min

sec = str(sec)
sec_l = len(sec)
if len(sec) < 2:
    sec = "0"+sec

print("Время равно: {}:{}:{}".format(hour, min, sec))