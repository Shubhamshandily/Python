#Array
import array
a=array.array('i',[1,2,3,4,5])
print(a)                           #Without Alias

import array as arr
a=arr.array('i',[1,2,3,4,5])       #With Alias i.e arr
print(a)

from array import *
a=array('i',[1,2,3,4,5])          #Third method to impot all array ,modul
print(a)

#Accesing Array Element
print(a[2])
print(a[-2])

                   #Basic Array Operation

print (a)
print(len(a))                        #finding lenght

a.append(7)
print(a)
a.insert(4,6)                        #Adding Element
print(a)
a.extend([7,5,6])
print(a)

a.pop()
print(a)
a.pop(5)
print(a)                           #Removing Element
a.remove(4)
print(a)

import array
b=array.array('i',[1,2,3,4,5])
c=array.array('i',[5,6,7,8,4,9])   #Array cancatenation
d=array.array('i')
d=b+c
print(d)

import array as arr
f=arr.array('d',[5.2,6.88,8])      #slicing
print(f[0:2])
print(f[::-1])                     #Reverse

                      #Looping through ARRAY



from array import *
d=array('d',[1,2,4,5,6,7,8,9,10])
print (d)
for x in d:
    print(x)                             #For LOOP

for x in d[0:-3]:
    print(x)

print(d)
temp=0
while temp<d[4]:                       #WHILE LOOP
    print(d[temp])
    temp=temp+1

print(d)
tem=0
while tem<len(d):
    print(d[temp])
    tem+=1
