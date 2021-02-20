#************USER DEFINED FUNCTION************
print("**************User Defined Function*****************\n")
def test():
    print("This is learning process test of function")
    
test()

#Parameterize function
print("\nParameterize function***\n")
def test2(t_name):
    print(t_name+" Chocolate")
test2('American')
test2('Mexican')

#Default Parameter
print('\nDefault Parameter***\n')
def test3(University='Columbia'):
    print("I'm from "+University+' University')
test3('New York')
test3('Howard')
test3()
test3('MIT')

#REturn Value
print('\nREtrurn Value***\n')
def fun(x):
    return 5*x
print(fun(5))
print(fun(6))

#RECURSION
print('\nRECURSION***\n')
'''def tri_recursion(k):
    if(k>0):
        result= k+tri_recursion(k-1)
        print(result)
    else:
        result=0
        return result
print('\n\nREcursion Example REsult')
tri_recursion(6)'''

#EX2
def func(a):
    if a==0:
        return
    else:
        print(a)
        func(a-1)
func(3)

#Recursion Factorial
def func1(a):
    if a==0:
        return 1
    else:
        return func1(a-1)*a
print(func1(5))
