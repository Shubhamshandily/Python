def func1(name):
    return f"Hello{name}"
def func2(name):
    return f"{name}, How you doin?"
def func3(func4):
     return func4("Dear Learner")
print(func3(func1))
print(func3(func2))
    #******Nested function*****
def fun():
    print("First Function")
    def fun1():
        print("First child fun")
    def fun2():
            print('second chile fun')
    fun2()
    fun1()
fun()

#***********Function2**************************************
print("\n******************Function2***********")
def fun(n):
    def fun1():
        return "Edureka"
    def fun2():
        return "Python"
    if  n==1:
        return fun1
    else:
        return fun2
a=fun(1)
b=fun(2)
print(a())
print(b())
