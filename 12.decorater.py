def fun1(fun):
    def wrapper():
        print("hello")
        fun()
        print("Welcome to function tutorial")
    return wrapper
def fun2():
    print("pythonInsta")

fun2=fun1(fun2)
fun2()
#********DEcorater*******
print("\n***************DEcorater Exampke*********")
def fun1(fun):
    def wrapper():
        print("hello")
        fun()
        print("Welcome to function tutorial")
    return wrapper
@fun1
def fun2():
    print("PythonInsta")
fun2()

#*********Basic Decorator*******************
print("\n**********************Basic DEcorator********************")
def fun1(fun):
    def wrapper(*args,**kwargs):
        print("Hello")
        fun(*args, **kwargs)
        print("Welcome to decorator")
    return wrapper
@fun1
def fun2(name):
    print(f"{name}")
fun2("Shubham")
    
#*******************************************************
print("\n***************************************************")
def fun1(fun):
    def wrapper(*args, **kwargs):
        print("it worked")
    return wrapper
@fun1
def fun2(name):
    print(f"{name}")
fun2("Python")
