
my_string = "Hello World"
print(my_string.count('l'))
print(my_string.startswith('H'))
print(my_string.endswith('D'))
char = my_string[1]
print(char)
print(my_string.replace("World", "Universe"))
string1 = my_string.split(" ")   # convert to list
print(string1)
string2 = " ".join(string1)   # convert to string
print(string2)

string = "           Hello Universe             "
str1 = string.strip()
print(str1)
print(string)

my_string = "how are you doing"
for i in my_string:
    print(i)

if "you" in my_string:
    print(my_string)
else:
    print("none")

my_list = my_string.split(" ")
print(my_list)
st = " ".join(my_list)
print(st)

var = 3
my_string1 = "the variable value is %d" %var
print(my_string1)

var1 = 3.123456
my_string2 = "the variable value is %f " %var1
print(my_string2)

# or

# my_string2 = f"the variable is {var}"
# print(my_string2)

my_string2 = "{} {}".format("tha variable value is", var1)
print(my_string2)

