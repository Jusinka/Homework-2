x = float(input("Введіть відстань, пробігнуту першого дня (в кілометрах): "))
y = float(input("Введіть бажану відстань (в кілометрах): "))

distance = x
day = 1

while distance < y:
    distance += distance * 0.1
    day += 1

print("Номер дня, коли відстань буде не менше", y, ": ", day)