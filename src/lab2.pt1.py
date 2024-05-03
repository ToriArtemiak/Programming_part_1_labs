import math

a = 0.5
b = 0.9
h = 0.02
x = a

while x <= b:
    if x < 0.6:
        print("| x = ", x, " | F(x) =", math.cos(math.sqrt(x)), "|")
    elif 0.6 <= x < 0.7:
        print("| x = ", x, " | F(x) =", math.cos(x ** 2) / math.sin(x ** 2), "|")
    else:
        print("| x = ", x, " | F(x) =", math.atan(x ** 3) , "|")
    x += h
    x = round(x, 4)
