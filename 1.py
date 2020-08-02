# Найти корень линейного уравнения
# a * x^2 + b * x + c = 0;
import math
a = 1
b = 4
c = -5
D = b ** 2 - 4 * a * c
if D < 0:
    print('Мы тут за комплексные числа не шарим, иди сам решай такие уравнения')
elif D == 0:
    print((-b + math.sqrt(D))/ 2 / a)
else:
    x1 = (-b + math.sqrt(D))/ (2 * a)
    x2 = (-b - math.sqrt(D))/ (2 * a)
    print(x1, x2)