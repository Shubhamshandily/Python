#Hash Table #Hash Map
emp_details={'Shub':'001','Dev':'002','Priya':'003'}
print(emp_details)
print(type(emp_details))

new_dict=dict(Dave='004',Adam='005')
print(new_dict)
print(type(new_dict))

#Nested Dict
New_emp_details={'Employee':{'Dava':{'Id':'0001','Slary':'5000','Desigation':'Team Lead'},
                 'Avaa':{'id':'0002','Salary':'4000','Desigantion':'Designer'}}}
print(New_emp_details)
print(type(New_emp_details))

                #Operations in Hash TablE


print(new_dict['Dave'])
print(emp_details['Dev'])
print(emp_details)
print(emp_details.keys())
print(emp_details.values())               #Acessing Iteams
print(emp_details.get('Dev'))
for x in emp_details:
     print(x)

for x in emp_details.values():
     print(x)
for x,y in emp_details.items():
     print(x,y)

print(emp_details)
emp_details['Dev']='004'                  #Updating Iteams
emp_details['Chrish']='005'
print(emp_details)

emp_details.pop('Dev')
print(emp_details)
emp_details.popitem()                    #Deleting Iteam
print(emp_details)
del emp_details['Shub']
print(emp_details)




                 #Dict to Data Frame
import pandas as pd
df=pd.DataFrame(New_emp_details['Employee'])
print(df)
