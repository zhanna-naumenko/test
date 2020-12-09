from random import randint
import io
import os
import random

with open("D:/IT/Phyton/test/domains.txt", "r") as file_domains:
    domains_name = []
    for line in file_domains.readlines():
        domains_name.append(line.replace(".", "").strip())
print(domains_name)


###########################################################

with open("D:/IT/Phyton/test/names.txt", "r") as data_persons:
    surnames = []
    for line in data_persons.readlines():
        surnames.append(line.split()[1])
print(surnames)

###########################################################

random_number = random.randint(100, 1000)
random_word = "".join(chr(randint(ord("a"), ord("z"))) for _ in range(randint(5, 7)))
random_surname = random.choice(surnames)
random_domain = random.choice(domains_name)


email = random_surname + "." + str(random_number) + "@" + str(random_word) + "." + random_domain
print(email)

