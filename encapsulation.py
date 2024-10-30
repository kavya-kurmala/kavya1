from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def milege(self):
        pass
class Electric_car(Car):
    def milege(self):
        return f'milege'
class Disel_car(Electric_car):
    def play(self):
        return f'playing songs!'
class Motor_car(Disel_car):
    def cleaning(self):
        return f'cleaning car!'
mc=Motor_car()
print(mc.play())
print(mc.cleaning())
dc=Disel_car()
print(dc.play())
ec=Electric_car()
print(ec.milege())
#car=Car()
#print(car())
