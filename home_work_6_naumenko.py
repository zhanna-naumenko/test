#№1

my_list = ["zero", "one", "two", "three", "four", "five", "six"]
new_list = []
for index, value in enumerate(my_list):
    if index % 2:
        new_list.append(value[::-1])
    else:
        new_list.append(value)
print(new_list)

####################################################################
#№2

my_list = ["alpha", "beta", "animal", "macintosh", "apple"]
new_list = []
start_a = "a"

for value in my_list:
    if value[0] == start_a:
        new_list.append(value)
print(new_list)

######################################################################
#№3

my_list = ["alpha", "beta", "nice", "dice", "apple"]
new_list = []
symbol_a = "a"

for value in my_list:
    if symbol_a in value:
        new_list.append(value)
print(new_list)

########################################################################
#№4

my_list = [120, 55, "55", "nice", "dice", "apple", 33]
new_list = []

for value in my_list:
    if type(value) == str:
        new_list.append(value)
print(new_list)

#########################################################################
#№5

my_string = "asdfghasd"
new_string = []
for value in set(my_string):
    if my_string.find(value) - my_string.rfind(value) == 0:
        new_string.append(value)
print(new_string)

##########################################################################
#№6

my_str_1 = "hello, world"
my_str_2 = "hello, work"
exists = set(my_str_1).intersection(my_str_2)
print(exists)


###########################################################################
#№7

my_str_1 = "hello, world"
my_str_2 = "hello, work"
result = []
for value in set(my_str_1).intersection(set(my_str_2)):
    if my_str_1.find(value) - my_str_1.rfind(value) == 0 and my_str_2.find(value) - my_str_2.rfind(value) == 0:
        result.append(value)
print(result)