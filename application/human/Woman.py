from .Human import Human
import random

class Woman(Human): #Родитель в скабках
    def __init__(self, name = 'Christopher', soname = 'Pratt', age = 18, money = 0):
        super().__init__(name, soname, age, money)
        self.name = 'Настя'
        self.sex = 'female'
        self.stamina = 100

    @staticmethod
    def reproduce(fother = None, mother = None):
        if fother and mother and fother.sex == 'male' and mother.sex == 'female':
            print('Можно размножаться')
            if random.randint(0,1) == 0:
                return Human()
            return Woman()
        print('Размножаться нельзя')
        return None
    
    def shopping(self):
        self.money -= random.randint(0, 10)
        self.happiness += random.randint(0,10)
        print(self.name + ' пробежалась по магазинчикам <3')
        return self.happiness
    
    def fishing(self):
        self.happiness -= 5
        print(' Лучше бы прошлась по магазинам...') #Тупа сексизм)
        return self.happiness
