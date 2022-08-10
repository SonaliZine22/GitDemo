
dict1 = {"name" : "Tushar", "age" : 30, "city" : "pune"}
print(dict1)
dict1["email"] = "Tushar@gmail.com"
print(dict1)
print(dict1["age"])

dict2 = dict(name ="mary", age=35, hobby= "travelling")
dict1.update(dict2)
print(dict1)
print(dict1["city"])

my_dict = {3: 9, 6: 36, 9: 81, 12: 144}
print(my_dict[6])
my_tuple = (3, 7)
mydict = {my_tuple: 15}
print(mydict)

dic = {}
dic["firstname"] = "Rahul"
dic["lastname"] = "kumar"
dic["gender"] = "Male"
dic["age"] = 35
print(dic)
for key in dic:
    print(key)

if "firstname" == "Rahul" in dic:
    print("yes")
else:
    print("no")

