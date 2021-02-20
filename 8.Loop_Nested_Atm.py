#Nested loop
print("Welcome to glacticspace Bank ATM")
restart=('y')
chance=3
balance=67000.50
while chance>=0:
    pin= int(input('Please Enter your 4 didgit pin:'))
    if pin==(1234):
             print('You have entered the correct PIN\n')
             while restart not in ("n","NO","N","no"):
                 print('Please prees 1 for your balance\n')
                 print('Please prees 2 for withdrawl\n')
                 print('Please prees 3 to Deposite\n')
                 print('Please prees 4 to return Card\n')
                 option = int(input('Plese Enter your Choice:'))
                 if option==1:
                              print('Your Balance is A$',balance,'\n')
                              restart =input('Would you like to go back?')
                              if restart in('n','N','No','no'):
                               print('Thank You')
                              break
                 elif option==2:
                     option2=('y')
                     withdrawl=float(input("Enter the Amount to be Withdraw\n"))
                     if withdrawl in [50,100,500,1000,2000,5000,10000,20000,40000,50000]:
                                       balance=balance-withdrawl
                                       print("\n Your Balance is now A$",balance)
                                       restart = input('Would you like to go Back?')
                                       if restart in('n','N','NO','no'):
                                        print("Thank you")
                                       break
                     elif withdrawl !=[50,100,500,1000,2000,5000,10000,20000,40000,50000]:
                                          print('Invalid Amount, Re-try again\n')
                                          restart=('y')
                     elif withdrawl==1:
                                           withdrawl = float(input('Please Enter desired amount:'))
                 elif option==3:
                      pay_in= float(input('How much would you like to Deposite?'))
                      balance = balance+pay_in
                      print('\nyour Balance is Now A$',balance)
                      restart=input('Would you like to go back?')
                      if restart in ('n','NO','no','N'):
                          print('Thank you')
                          break
                 elif option==4:
                     print("PlEASE WAIT WHILE YOUR CARD IS RETURNED...\n")
                     print("Thank you, Please visit again!")
                     break
                 else:
                        print('Please Enter a correct number.\n')
                        restart=('y')
                        
    elif pin !=('1234'):
                    print('Incorrect Password')
                    chance= chance-1
                    if chance ==0:
                        print('\n you reach the maximux level, Plese try after sometime')
                        break
