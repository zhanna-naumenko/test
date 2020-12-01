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
#исправить
my_list = ["120", "55", "nice", "dice", "apple"]
new_list = []

for value in my_list:
    if value.isalpha():
        new_list.append(value)
print(new_list)

#########################################################################
#№5Дана строка my_str. Создать список в который поместить те символы из my_str,
#которые встречаются в строке только один раз.


##########################################################################
#№6Даны две строки. Создать список в который поместить те символы,
#которые есть в обеих строках хотя бы раз.


###########################################################################
#№7 Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
#но в каждой только по одному разу.

str1_ = "Гарри Поттер и Филосовский камень"
str2_ = "Гарри Поттер и Тайная комната"
res = []
for value in str1_:
    k = str1_.find(value) - str1_.rfind(value)
    if k == 0:
        if value in str2_ and str2_.find(value) - str2_.rfind(value) == 0:
            res.append(value)
print(res)
