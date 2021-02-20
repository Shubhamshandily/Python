#Specilized collection

#namedtuple
from collections import namedtuple
a= namedtuple('Courses','Name,Technology')
s= a('Data Science','Python')
s = a._make(['Artificial intellegence','python'])#Using list
print(s)
print(s)

#deque
from collections import deque
a= (['s','H','U','B','H','A','M'])
d= deque(a)
print(d)
d.append('THAKUR')
print(d)
d.appendleft('mong')
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.insert(4,'j')
print(d)

#Chainmap
from collections import ChainMap
a={1:'ML',2:'AI'}
b={3:'Big data',4:'Deep learning'}
d=ChainMap(a,b)
print(d)

#Counter
from collections import Counter
a=[1,1,1,4,4,6,6,'y',0,4,7,'u','u',7,6,5,4,3,2,18,9,0]
b=Counter(a)
print(b)
print(list(b.elements()))
print(b.most_common())
sub ={4:2,2:1}
print(b.subtract(sub))
print(b.most_common())

#OrderedDict
from collections import OrderedDict
a= OrderedDict()
a[1]='S'
a[2]='H'
a[3]='U'
a[4]='B'
a[5]='H'
a[6]='A'
a[7]='M'
print(a)
a[1]='V'
print(a)

#Defaultdict
from collections import defaultdict
d=defaultdict(int)
d[1] ='python'
d[2]='edureka'
print(d)
print(d[3])

#UserDict
#UserList
#UserString

