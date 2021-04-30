day1 = int(input("Введите количество километров в первый день: "))
target = int(input("Введите целевое количетсво комлометров: "))

i = 1
next_day = 0
protz = 0

while next_day < target:
    protz = float(day1*0.1)
    next_day = float(day1+protz)
    day1 = next_day
    i += 1

print(f"Спортсмен достигнет результата {next_day:.2f} на {i} день.")

