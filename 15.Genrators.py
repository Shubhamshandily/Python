#Generators
def new(dict):
    for x,y in dict.items():
        yield x,y
a={1:"Hey",2:"Sam"}
b=new(a)
#print(b)
next(b)

def newfunc(i):
    while i<3:
        yield i
        i+=1
j=newfunc(2)
next(j)

def new():
    n=3
    yield n
    n=n*n
    yield n
v=new()
next(v)
#************For loop in gentators*************
def new():
    n=3
    yield n
    n=n*n         #for loop print all iteration and stop
    yield n
v=new()
for x in v:
    print(x)
#*****************Generator Expression************
print("*********Generator Expression***********")
a=range(8)
print("List comp",end=":")
q=[x+2 for x in a]
print(a)
print("Gen exp",end=":")
r=(x+2 for x in a)
print(r)
for x in r:
    print(x)
print("Gen exp",end=":")
r=(x+2 for x in a)
print(r)
print(min(r))


