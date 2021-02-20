print('Abstract Class***')
from abc import ABC, abstractmethod

class cars(ABC):
    @abstractmethod
    def price_inc(self):
        pass
        
class supercar(cars):
    def __init__(self,modelname,yearm,price,cc):
        super.__init__(modelname,yearm,price)
        self.cc=1500
    def price_inc(self):
        self.price=int(self.price*2)

        
Honda=supercar('City',2017,250000,500)
Tata=cars('Bolt',2020,600000)


#print(help(Honda))
Honda.price_inc()
print(Honda.price)
print(Honda.__dict__)
