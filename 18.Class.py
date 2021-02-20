#Class
print("*******************CLASS****************")
#instance
print("Instance***")
class cars():
    pass
Honda=cars()
Tata=cars()

Honda.modelname='City'
Honda.years=2017
Honda.price=250000

Tata.modelname='Bolt'
Tata.years=2020
Tata.price=400000

print(Tata.price)

#Common object
print('\ncommon object***\n')
class cars():
    def __init__(self,modelname,yearm,price):
        self.modelname=modelname
        self.yearm=yearm
        self.price=price
Honda=cars('City',2017,250000)
Tata=cars('Bolt',2020,600000)
Honda.cc=1500 #Instance variable for Honda

print(Tata.price)
print(Honda.__dict__)
print(Tata.__dict__)

#Updating class*****************************
print('Updating onject***')
class cars():
    def __init__(self,modelname,yearm,price):
        self.modelname=modelname
        self.yearm=yearm
        self.price=price
    def price_inc(self):
        self.price=int(self.price*1.5)
        
Honda=cars('City',2017,250000)
Tata=cars('Bolt',2020,600000)
Honda.cc=1500 #Instance variable for Honda

print(Tata.price)
Tata.price_inc()

print(Tata.price)
#Super class
print('\nSuper class***\n')
class supercar(cars):
    pass
Honda=cars('City',2017,250000)
Tata=cars('Bolt',2020,600000)
Honda.cc=1500
#print(help(Honda))
Honda.price_inc()
print(Honda.price)
print(Honda.__dict__)
