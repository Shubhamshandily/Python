class Parents:
    def __init__(self,fname,fage):
        self.name=fname
        self.age=fage
    def view(self):
        print(self.name,self.age)
class Child(Parents):
    def __init__(self,fname,fage):
        Parents.__init__(self,fname,fage)
        self.lastname='JHon'
    def view(self):
        print(self.age,self.name,self.lastname)
ob=Child('Shubham', 24)
ob.view()

#TYPE OF INHERITANCE#############################
print('\n TYPES OF INHERITANCE######################## \n')

#Single Inheritance
print("\nSingle Inheritance\n")
class father:
    def fun1(self):
        print("This is a parent class")

class child(father):
    def fun2(self):
        print("This is child class")
ob=child()
ob.fun1()

#Multiple inheritance
print("\nMultiple Inheritance\n")
class father:
    def fun1(self):
        print("This is a parent class")
class Mother:
    def fun3(self):
        print("this is function 3")

class child(father,Mother):
    def fun2(self):
        print("This is child class")
ob=child()
ob.fun1()
ob.fun3()

#Multi level inheritance
print('\n Multi level inheritance\n')
class p:
    def fun1(self):
        print("This is fun 1")
class s(p):
    def fun2(self):
        print("this is fun2")
class gchild(s):
    def fun3(self):
        print("this is fun3")
ob=gchild()
ob.fun1()
ob.fun2()

#Hierarchial Inheritance
print("\n Hierarchial Inheritance")
class p:
    def fun1(self):
        print("This is fun 1")
class s(p):
    def fun2(self):
        print("this is fun2")
class gchild(p):
    def fun3(self):
        print("this is fun3")
ob=gchild()
ob1=s()
ob.fun1()
ob1.fun1()

#Hybride Inheritance
print("\n Hybride INheritance######")
class father:
    def fun1(self):
        print("This is a parent class")
class Mother(father):
    def fun3(self):
        print("this is function 3")
class mother2:
    def fun4(self):
        print("this is function no 4")

class child(father,mother2):
    def fun2(self):
        print("This is child class")
ob=child()
ob.fun1()
ob.fun4()

#Super Class Function                /Super class cAN directly call parent class
print("\nSUPER CLASS FUNCTION\n")
class prent:
    def fun1(self):
        print("This is fun1")
class child(prent):
    def fun2(self):
        super().fun1()
        print("this is fun2")
ob=child()
ob.fun2()


#Method overriding
print('\nMethod Overriding##############\n')
class prent:
    def fun1(self):
        print("This is fun1")
class child(prent):
    def fun1(self):
        print("this is fun2")
ob=child()
ob.fun1()
