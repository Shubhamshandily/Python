#Pattern
def pattern(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ") 
        k=k - 1
        for j in range(0, i + 1):
                print("* ",end="")
        print("\r")
pattern(5)

#inverse pyramid
def pattern(n):
 k=2*n-2
 for i in range(n,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0, i+1):
        print("* ",end="")
    print("\r")
pattern(5)

#right start pattern
def pattern(n):
    for i in range(0,n):
        for j in range(0,i + 1):
            print("* ",end="")
        print("\r")
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(5)

#left start pattern
def pattern(n):
    k=2*n-2
    for i in range(0, n-1):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    k=-1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k=k+2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(5)

#hour Glass
def pattern(n):
 k=n-2
 for i in range(n,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0, i+1):
        print("* ",end="")
    print("\r")
 k=2*n-2
 for i in range(0,n+1):
     for j in range(0,k):
         print(end=" ") 
     k=k - 1
     for j in range(0, i + 1):
         print("* ",end="")
     print("\r")
pattern(5)

#right alphabetical triangle
def pattern(n):
    x=65
    for i in range(0,n):
        ch=(chr(x))
        x=x+1
        for j in range(0, i + 1):
         print(ch,end=" ")
        print("\r")
pattern(10)
