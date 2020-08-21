import random

class Human:
    def __init__(self, name = 'Christopher', soname = 'Pratt', age = 18, money = 0):
        self.sex = 'male'
        self.stamina = 150
        self.name = name
        self.soname = soname
        self.age = age
        self.money = money
        self.happiness = 100

    def __del__(self):
        print(self.name, 'Экземпляр уничтожен!')

    def getName(self):
        print( self.sex + ' ' + self.name + ' ' + self.soname)
    
    def eat(self):
        if self.money > 0:
            self.money -= 1
            self.stamina +=10
            print(self.name +' '+  self.soname + ' покушаль. Осталось денег:' + str(self.money) + ' Здоровье:' + str(self.stamina))
        else:
            print('Нет денег! Пора идти на работу =( ')

    def work(self):
        self.money += 5
        self.happiness -= 5
        self.stamina -= 10
        print('Пятилетку в четыре года! Рабочий день ' + self.name + ' завершен')

    def fishing(self):
        if(self.sex == 'male'):
            self.money -= random.randint(0, 10)
            self.stamina -= random.randint(0, 10)
            self.happiness += random.randint(0, 50)
            print(' У ' + self.name + ' рыбалочка удалась на славу')
        else:
            self.happiness -= 5
            print(' Лучше бы прошлась по магазинам...') #Тупа сексизм)