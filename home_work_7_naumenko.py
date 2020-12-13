#№1
import random

my_list = [str(random.randrange(101)) for _ in range(20)]
print(my_list)

##################################################
#№2

def create_coordinates():
    """Creates coordinates"""
    return tuple(random.randint(-10, 10) for _ in range(2))

triangle = {"A": create_coordinates(),
            "B": create_coordinates(),
            "C": create_coordinates()}
print(triangle)

##################################################
#№3 Помню, что Вы говорили, что лучше делать через f строку, но если бы Вы не подсказали, сделала бы так.
#Поэтому и оставила такое решение. Но на будущее конечно же учту, что правилнее делать через f строку.

def my_print(my_str):
    print("***", my_str, "***")

my_str = "I'm the string"
my_print(my_str)

###################################################
#№4a

persons = [{"name": "John", "age": 15},
           {"name": "Kevin", "age": 95},
           {"name": "Malcom", "age": 36},
           {"name": "Jack", "age": 45},
           {"name": "Harry", "age": 17},
           {"name": "Jason", "age": 15},
           {"name": "Melvin", "age": 84}]

youngest_person = min(person["age"] for person in persons)
print(*[person["name"] for person in persons if person["age"] == youngest_person])

###################################################
#№4b

longest_name_person = max(len(person["name"]) for person in persons)
print(*[person["name"] for person in persons if len(person["name"]) == longest_name_person])

###################################################
#№4c

print(*[sum(person["age"] for person in persons) // len(persons)])


####################################################
#№5a
my_dict_1 = {"vegetable": "carrot", "weight": 150, "availability": "yes", "calories": 62}
my_dict_2 = {"vegetable": "potato", "weight": 250, "availability": "yes", "condition": "good"}

unite_dict_keys = list(set(my_dict_1).intersection(my_dict_2))
print(unite_dict_keys)

####################################################
#№5b

difference_dict_keys = list(set(my_dict_1).difference(my_dict_2))
print(difference_dict_keys)

####################################################
#№5c

new_dict = {key: my_dict_1[key] for key in difference_dict_keys}
print(new_dict)

####################################################
#№5d.1

new_dict_1 = {key: my_dict_1[key] for key in list(set(my_dict_1).difference(my_dict_2))}
new_dict_2 = {key: my_dict_2[key] for key in list(set(my_dict_2).difference(my_dict_1))}
unite_dicts_differences = {**new_dict_1, **new_dict_2}
print(unite_dicts_differences)

####################################################
#№5d.2

intersection_keys = set(my_dict_1).intersection(my_dict_2)
unite_dicts_same = {key: [my_dict_1[key], my_dict_2[key]] for key in intersection_keys}
print(unite_dicts_same)
