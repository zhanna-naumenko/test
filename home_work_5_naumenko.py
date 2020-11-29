my_value = input("Введите число: ")
zero = '0'
count = my_value.count(zero)
print(count)

##########################################

my_value = int(input("Введите число: "))
if my_value == 0:
    print(1)
    exit()
count_zero = 0
while my_value % 10 == 0:
    my_value //= 10
    count_zero += 1
print(count_zero)

###########################################

my_list_1 = [1, 2, 3, 4, 5, 6, 8]
my_list_2 = [10, 15, 20, 25, 33, 45]
my_result = []
for value in my_list_1:
    if not value % 2:
        my_result.append(value)
for value in my_list_2:
    if value % 2:
        my_result.append(value)
print(my_result)

############################################

my_list = [10, 15, 20, 25, 33, 45]
new_list = []
for symbol in my_list[1:]:
    new_list.append(symbol)
for symbol in my_list[0::-1]:
    new_list.append(symbol)
print(new_list)

#############################################

my_list = [11, 15, 23, 25, 33, 45, 89, 67, 0]
for symbol in my_list[0::-1]:
    my_list.append(symbol)
my_list.pop(0)
print(my_list)

###############################################

my_str = "56 больше чем 12 но меньше чем 122"
word_list = my_str.split()
num_list = []
for word in word_list:
    if word.isnumeric():
        num_list.append(int(word))
print(sum(num_list))

##################################################

my_str = "agkhjdckjadsdcn"
my_number = 2
my_str = my_str + "_" if len(my_str) % 2 else my_str
new_str = [my_str[value:value+my_number] for value in range(0, len(my_str), my_number)]
print(new_str)

##################################################

my_str = "My_long str"
l_limit = "o"
r_limit = "t"
sub_str = my_str[my_str.find(l_limit)+1:my_str.find(r_limit)]
print(sub_str)

###################################################

my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = []
revers = my_str[::-1]
sub_str = revers[revers.find(r_limit):revers.find(l_limit)]
revers_sub = sub_str[::-1]
print(revers_sub)

###################################################

my_str = [2, 4, 1, 5, 3, 9, 0, 7, 3, 9, 4]
result = []
for value in range(1, len(my_str) - 1):
    if my_str[value - 1] < my_str[value] > my_str[value + 1]:
        result.append(value)
print(len(result))