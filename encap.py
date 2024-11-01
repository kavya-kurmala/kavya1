from abc import ABC,abstractmethod
class Vehicle:
    @abstractmethod
    def milege(self):
        pass
class Car(Vehicle):
    def milege(self):
        print(f'milege is 30kmph')
        
car1=Car()
car1.milege()
veh=Vehicle()
veh.milege()
