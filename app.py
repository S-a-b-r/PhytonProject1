from human.Human import Human
from human.Woman import Woman
import Equation
import time
from threading import Thread

e = Equation.Equation()
print(e.equation(2, 1, 3))
a = Human('Вован', 'Князев', 35)
b = Woman('Катя', 'Аитова', 18)

a.work()
a.eat()
b.work()
b.work()
b.work()
a.fishing()
b.shopping()
b.fishing()
c = b.reproduce(a,b)


def pow(power):
    def decorator(func):
        def wrapper(*args, **kwargs):
            i = 0
            result = 1
            while i < power:
                result *= func(*args, **kwargs)
                i+=1
            return result
        return wrapper
    return decorator

@pow(3)
def add( a, b, c):
    return a + b + c

def someFunc1():
    for i in range(10):
        print('Первый поток', i)
        time.sleep(1)

def someFunc2():
    i = 0
    while True:
        print('Второй поток', i)
        i += 1
        time.sleep(0.5)

thread1 = Thread(target=someFunc1, daemon= True)
thread1.start()

thread2 = Thread(target=someFunc2, daemon= True)
thread2.start()

print('Что-то еще хочу сделать')
time.sleep(10)