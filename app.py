from human.Human import Human
from human.Woman import Woman

a = Human('Вован', 'Князев', 35)
b = Woman('Настя', 'Аитова', 18)

a.work()
a.eat()
b.work()
b.work()
b.work()
a.fishing()
b.shopping()
b.fishing()

print(b.money)