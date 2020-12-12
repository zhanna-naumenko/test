from random import randint
import io
import os
import random

def open_file_domains():
    """Opens file domains.txt and return domains names without dot"""
    with open("D:/IT/Phyton/test/domains.txt", "r") as file_domains:
        domains_name = []
        for line in file_domains.readlines():
            domains_name.append(line.replace(".", "").strip())
    print(domains_name)

open_file_domains()
###########################################################

def open_file_names():
    """Opens file names.txt and return only surnames"""
    with open("D:/IT/Phyton/test/names.txt", "r") as data_persons:
        surnames = []
        for line in data_persons.readlines():
            surnames.append(line.split()[1])
    print(surnames)

open_file_names()

###########################################################

def random_domain():
    """Opens file domains.txt and return random domain name without dot"""
    with open("D:/IT/Phyton/test/domains.txt", "r") as file_domains:
        domain_name = []
        for line in file_domains.readlines():
            domain_name.append(line.replace(".", "").strip())
    print(random.choice(domain_name))

def random_name():
    """Opens file names.txt and return random surname"""
    with open("D:/IT/Phyton/test/names.txt", "r") as data_persons:
        surname = []
        for line in data_persons.readlines():
            surname.append(line.split()[1])
    print(random.choice(surname))


random_number = random.randint(100, 1000)
random_word = "".join(chr(randint(ord("a"), ord("z"))) for _ in range(randint(5, 7)))



email = random_name() + "." + str(random_number) + "@" + str(random_word) + "." + random_domain()
print(email)

