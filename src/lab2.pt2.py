import math

a = 0.5
b = 0.7
h = 0.05
d = 0.001

x = a
k = 1
result = 0

while x <= b:
    while True:
        element = (x + 2) / k * (k + 2)
        result += element
        prev_element = element
        k += 1
        if abs(element - prev_element) <= d:
            print("Error! the element is less than fault")
            break
    x += h
    print(" the sum {k} times:", result,'x equals:', round(x, 1))

