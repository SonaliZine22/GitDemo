list = [1, "str", 2, 5, 10.5]

print(list)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = list1 + list2
print(list3)
list1.insert(2, "string")
list2.append("End")  # add at the of list
print(list1)
print(list2)
del list3[4]
print(list3)
list4 = [0] * 5
print(list4)

my_list = ["banana", "cherry", "apple", 10, 80.0]
a = my_list[1:3]   # gives index from 1 to 2. 3 skip
b = my_list[::-1]  # gives list in reverse order
c = my_list[::2]   # only gives 2* index
print(a)
print(b)
print(c)
my_tuple = tuple(my_list)  # Converted list to tuple
print(my_tuple)
