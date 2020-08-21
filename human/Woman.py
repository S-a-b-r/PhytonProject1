from .Human import Human
import random

class Woman(Human): #Родитель в скабках
    def __init__(self, name = 'Christopher', soname = 'Pratt', age = 18, money = 0):
        super().__init__(name, soname, age, money)
        self.sex = 'female'
        self.stamina = 100

    @staticmethod
    def reproduce(fother = None, mother = None):
        if fother and mother and fother.sex == 'male' and mother.sex == 'female':
            print('Можно размножаться')
            return Human()
        print('Размножаться нельзя')
        return None
    
    def shopping(self):
        self.money -= random.randint(0, 10)
        self.happiness += random.randint(0,10)
        print(self.name + ' пробежалась по магазинчикам <3')
