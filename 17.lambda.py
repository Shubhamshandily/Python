#Lambda function
#Syntax: lambda argument:expression
print("Lambda function")
x=lambda a:a*a
print(x(5))

#**********Lambda Function within user defined function*******
print("\n**********Lambda Function within user defined function*******")
def A(x):
    return (lambda y:x+y)
t=A(5)
print(t(8))
u=A(9)
print(u(5))

#***********Lambda within filter()***********************
print("\n********Lambda within map()")
mylist=[1,2,3,4,5,6,7,8,]
new_list=list(filter(lambda a:(a/3==2),mylist))#Syntax: filter(function,iterable))
print(new_list)

#***********Lambda within Map()***********************
#map(fun,iterables)
print("\n#***********Lambda within Map()***********************")
mylist=[1,2,3,4,5,6,7,8,9]
new_lis=list(map(lambda a:(a/3!=2),mylist))
print(new_lis)

#***********Lambda within reduce()***********************
print("\n#***********Lambda within reduce()***********************")
#reduce(function,sequence)
from functools import reduce #or from functools import *
print(reduce(lambda a,b:(a+b),[23,55,88,95]))

from functools import * #or from functools import *
print(reduce(lambda a,b:(a+b),[23,55,88,95]))



#Algebric Function In lambda*********
print("\nAlgebric Function In lambda********************")
#LInear Equatiom
print("\n Linear Equation****")
s=lambda a: a*a
print(s(4))

#3X+4Y Equation
print("\n 3X+4Y\n")
d=lambda x,y: 3*x+4*y
print(d(4,5))

#Quadratic Equation
print("\nQuadratic Equation")
print("\n (a+b)^2)\n")
z=lambda a,b: (a+b)**2
print(z(5,4))

#***********    Map-Reduce Function*******************
print("\n#***********    Map-Reduce Function*******************")
#map(func,iterables)
print("Map")
def new(a):
    return a*a
x=map(new,[1,2,3,4,5,6])
print(x)
#print(list(x))
print(tuple(x))

print("Map")
def new(a,b):
    return a*b
x=map(new,[1,2,3,4,5,6],[5,6,8,4,4,5])
print(x)
print(tuple(x))

#Lambda in map()
print('\nLambda in map()')
lst=[1,2,3,4]
X=list(map(lambda x: x+3,lst))
print(X)
#Filter()
print("\nFilter()")
def new1(i):
    if i>=3:
        return i
j=filter(new1,(1,2,3,4,5,6,7))
print(j)
print(tuple(j))

#Lamba filter
v=filter(lambda i:i>3,(1,2,3,4,5))
print(v)
print(tuple(v))

#Reduce Function()
print("\n REduce function")
from functools import *
def red(x,y):
    return x+y
s=reduce(red,[1,2,3,4,5,6])
print(s)

#Lmbda reduce
from functools import *
print(reduce(lambda x,y: x*y,[1,2,3,4,5]))


#Filter within map
print("\n Filter within map")
c=map(lambda x:x*x, filter(lambda x: (x>=2),(1,2,3,4)))
print(tuple(c))

d=filter(lambda x: (x>=2),map(lambda x:(x*x) ,[1,2,3,4,5]))
print(set(d))

#Map and filter in reduce
print("\n map and filter in reduce")
g=reduce(lambda x,y:x+y, map(lambda x:x*x,x),filter(lambda x: (x>=3),[1,2,3,4,5]))
print(tuple(g))
