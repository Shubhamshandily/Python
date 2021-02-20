#Loops
count=0
while count<9:
    print("Number:",count)
    count=count+1
print("Done")

#Guessing Random Number'''
import random
n=20
to_be_guessed = int(n* random.random()) +1
guess =0
while guess != to_be_guessed:
    guess =int(input("New Number:"))
    if guess>0:
        if guess> to_be_guessed:
            print("Number is too large")
        elif guess<to_be_guessed:
            print("Number is too small")
    else:
        print("Sorry, you are giving up!")
        break
else:
    print("Congrates, you are winner")






