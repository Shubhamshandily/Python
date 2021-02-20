#Operatores

x=10
y=20
print(x+y)
print(x-y)
print(x*y)
print(x/y)                          #Arthimetic operators
print(x%y)
print(x//y)
print(x^y)
print(x**y)


#Assignment
print("\n**Assignment**")
a=5
a+=5
print(a)
a-=5
print(a)
a*=5
print(a)
a/=5
print(a)
a%=5
print(a)
a//=5
print(a)
a**=5
print(a)

#Comparison
print("\n**Comparison**")
b=input("B:")
c=input("C:")
compare=(b==c)
print(compare)
compare=(b!=c)
print(compare)
compare=(b>c)
print(compare)
compare=(b<c)
print(compare)
compare=(b>=c)
print(compare)
compare=(b<=c)
print(compare)

#Conditional
print("\n**Conditional**")
if b==c:
    print("Equals")
elif b>=c:
    print("Grater")
else:
    print("smaller")

#Logical
print("\n**Logical**")
d=10
print(d>10 and d>5)
print(d>8 and d>5)
print(d>10 or d>5)
print(d>10 or d>45)
print(d>= 10 and d>=5)
print(not(d>10 and d>5))
print(not(d>10 or d>5))

#Identity Operators
print("\n**Identity**")
list1=[10,20,30]
list2=[10,20,30]
x=list1
print(x is list1)
print(list1 is list2)
print(list1 is not list2)

#Membership Operators
print("\n**Membership**")
print(x in list1)
print(list2 in list1)
print(list1 in list2)
print(10 in list1)
print([10,20,30] in list1)
print(50 not in list1)
print('banana' in list1)

#differance b\w is and ==
print(list1==list2)

#Bitwise Operators
print("\n**Bitwise**")
print(10 & 12)
print(10|12)
print(10>>2)
print(10<<2)
print(10^12)
print(~(10 & 12))
