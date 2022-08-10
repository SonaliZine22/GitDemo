from itertools import product
a =[1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))

from itertools import permutations
a = [1, 2, 3]
per = permutations(a, 2)
print(list(per))

from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a)
print(list(acc))
acc1 = accumulate(a, func = operator.mul)
print(list(acc1))

from itertools import groupby


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break
a= [1, 2, 3, 4]
for i in cycle(a):
    print(i)







