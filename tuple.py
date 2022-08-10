
tuple = ("max", 28, "Boston", "Jorge")
print(tuple)
print(len(tuple))
print(type("max"))
print(tuple[-1])
print(tuple[::-1])
print(tuple[::2])
i1, *i2, i3 = tuple
print(i1)
print(i2)
print(i3)


my_tuple = ("apple", "cherry", "mango", "strawberry", "mango")
my_list = list(my_tuple)
print(my_list)
print(my_tuple.index("cherry"))
print(my_tuple.index("mango"))
print(my_tuple[1:4])


