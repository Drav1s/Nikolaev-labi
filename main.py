from math import *

print("ax^2 + bx + c = 0:")
a = int(input('Коэффициент a:'))
b = int(input('Коэффициент b:'))
c = int(input('Коэффициент c:'))

D = b ** 2 - 4 * a * c
print('Дискриминат:', D)
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)
elif D < 0:
    print("Нет решений")
