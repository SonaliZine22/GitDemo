
myset = set()
print(myset)
myset.add(1)
myset.add("name")
myset.add(3)
myset.add(10.5)
print(myset)
print(myset.pop())

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3, 10, 11, 12}
print(setA.union(setB))
print(setA.intersection(setB))
print(setA.difference(setB))
print(setB.difference(setA))
print(setA.symmetric_difference(setB))
setC = {1, 2, 3, 4, 5, 6}
setD = {1, 2, 3}
setE = {7, 8}
print(setD.issubset(setC))
print(setC.issuperset(setD))
print(setC.isdisjoint(setE))

setA = {1, 2, 3, 4, 5, 6}
setB = setA
print(setB)
setB.add(7)
setB = setA.copy()
print(setB)
print(setA)
