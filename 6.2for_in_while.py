#Nested For loop in while loop
travelling=input('yes or no:')
while travelling=='yes':
    num=int(input("Number of people Travelling:"))
    for num in range(1, num+1):
            name=input("Name:")
            age=int(input("Age:"))
            sex=input("M/F:")
            print(name)
            print(age)
            print(sex)
    travelling=input("OOps! Forget Someone")
