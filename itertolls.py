#itertools
from itertools import product
print (list(product([1,2,3],[1,2,5])))
print

#permutations
from itertools import permutations
print
print(list(permutations(range(3))))
print

print(list(permutations([1,2,3],2)))
print

#combination
from itertools import combinations
print(list(combinations(range(3),2)))
