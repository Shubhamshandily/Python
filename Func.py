#Python Function
print("****************Function***************")
print("\nInbulit Function***")

print("\n abs()")
x=abs(3+5j)
print(x)

print("\n all()")
list=[True,True,True]
x=all(list)
print(x)

print("\n ascii()")
x=ascii("Hey my name is stale")
print(x)

print("\n bool()")
x=bool(5)
print(x)

print("\n enumerate()")
x=('Mango','Tango','Cherry')
y=enumerate(x)
print(y)

print("\n Format()")
x=format(.5,'%')
print(x)

print("\n getattr()")
class Person:
    name='James'
    age='26'
    country='Spain'
x=(getattr(Person,'age'))
print(x)

print("\n id()")
x=('Apple','Mango','Avocardo')
y=id(x)
print(y)

print("\n len()")
mylist='Hey Python'
x=print(len(mylist))

print("\n map()")
def myfun(n):
    return len(n)
x=map(myfun,('apple','rose','jamoon'))
print(x)

print("\n min()")
x=print(min(1,55,99,6548,2,-6))

print("\n pow()")
x=print(pow(4,3))

print("\n setattr()")
class Person:
    name='James'
    age='26'
    country='Spain'
x=(setattr(Person,'age',40))
print(x)

print("\n sorted()")
a=('b','g','c','d','a')
x=sorted(a)
print(x)
