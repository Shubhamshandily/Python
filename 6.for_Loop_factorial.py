#For loop
fruits=['Mango','Apple','Watermelom']
for fruit in fruits:
    print("current fruit:",fruit)
print("Executed")
#Factorial
num=int(input("Number:"))
factorial = 1
if num<0:
        print("Number can not be Negative")
elif num==0:
    print("Factorial= 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
print(factorial)
