from human.Human import Human
from human.Woman import Woman

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

print(add(1,2,7))