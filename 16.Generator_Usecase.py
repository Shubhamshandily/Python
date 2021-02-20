#Generator Use Case
print("****************Generator Use Case***************")
print("Fibonnacci Series***")
def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s
for x in fib():
    if x<50:
        break
    print(x, end=" ")
    
print("Number Stream***")
a=range(100)
b=(x for x in a)
print (b)
for y in b:
    print(y)
#Even Number
print("N stream for Even number")
a=range(2,100,2)
b=(x for x in a)
print (b)
for y in b:
    print(y)
#Odd Numbers
print("Odd Numbers")
a=range(1,100,2)
b=(x for x in a)
print (b)
for y in b:
    print(y)
    
#Signwave
print("Sign wave***")
'''import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
def s(flip =2):
    x= np.linspace(0, 14, 100)
    for i in range(1,5):
        plt.plot(x,np.sin(x + i* .5) * (7 - i) * flip)
sb.set()
s()
plt.show()'''

#Genrator function
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
def s(flip =2):
    x= np.linspace(0, 14, 100)
    for i in range(1,5):
        plt.plot(x,np.sin(x + i* .5) * (7 - i) * flip)
sb.set()
s()
plt.show()
print(next(s))
