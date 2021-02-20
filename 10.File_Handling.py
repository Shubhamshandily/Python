#File Handling
'''import os
file =open("/root/Desktop/Demo","w")
file.close()'''

import os
file =open("/root/Desktop/Demo","r")
print(file.read())
file.close()

import os
file =open("/root/Desktop/Demo","r")
print(file.read(10))
file.close()

#Reading Lines
import os
file= open("/root/Desktop/Demo",'r')
print(file.readline())
file.close()

import os
file= open("/root/Desktop/Demo",'r')
print(file.readlines())
file.close()

import os
file= open("/root/Desktop/Demo",'r')
print(file.readline(3))
file.close()
         #********Writing Files#*******
import os
f=open("/root/Desktop/Demo",'w')
print(f.write("This is writing example"))
print(f.write("Which overrite the old text"))
f.close()

import os
f=open("/root/Desktop/Demo",'a')
print(f.write("So exicted to learn this module"))
f.close()

         #**********Creating Files***********
'''import os
f=open("/root/Desktop/Demox",'x')
print(f.write("New file created"))
f.close()

import os
f=open("/root/Desktop/Demoxx",'x')
print(f.write("New file created"))
f.close()'''
#****************DEleting Files**********************
#import os
#os.remove("/root/Desktop/Demoxx")

#2
import os
if os.path.exists("/root/Desktop/Demo_creat"):
    os.remove("/root/Desktop/Demo_creat")
else:
                  print("Does not exists")
