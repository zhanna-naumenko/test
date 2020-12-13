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
    return (domains_name)

print(open_file_domains())
###########################################################

def open_file_names():
    """Opens file names.txt and return only surnames"""
    with open("D:/IT/Phyton/test/names.txt", "r") as data_persons:
        surnames = []
        for line in data_persons.readlines():
            surnames.append(line.split()[1])
    return (surnames)

print(open_file_names())

###########################################################

def random_domain():
    """Return random domain name"""
    return random.choices(open_file_domains())

def random_name():
    """Return random surname"""
    return random.choice(open_file_names())

def random_number():
    """Create random number"""
    return random.randint(100, 1000)


def random_word():
    """Create random word"""
    return "".join(chr(randint(ord("a"), ord("z"))) for _ in range(randint(5, 7)))


def random_email():
    """Create random e-mail"""
    print(random_name() + "." + str(random_number()) + "@" + random_word() + "." + str(*random_domain()))

random_email()
