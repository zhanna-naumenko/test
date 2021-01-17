from random import randint
import io
import os
import random


class EmailGenerator:
    def __init__(self, path_domains, path_names):
        self.path_domains = path_domains
        self.path_names = path_names
        self.get_names()
        self.get_domains()


    def get_domains(self):
        """Opens file domains.txt and return domains names without dot"""
        with open(self.path_domains, "r") as file_domains:
            domains_name = []
            for line in file_domains.readlines():
                domains_name.append(line.replace(".", "").strip())
        return (domains_name)

    def get_names(self):
        """Opens file names.txt and return only surnames"""
        with open(self.path_names, "r") as data_persons:
            surnames = []
            for line in data_persons.readlines():
                surnames.append(line.split()[1])
        return (surnames)

    def random_domain(self):
        """Return random domain name"""
        return random.choices(self.get_domains())

    def random_name(self):
        """Return random surname"""
        return random.choice(self.get_names())

    def random_number(self):
        """Create random number"""
        return random.randint(100, 1000)

    def random_word(self):
        """Create random word"""
        return "".join(chr(randint(ord("a"), ord("z"))) for _ in range(randint(5, 7)))

    def generate_email(self):
        """Create random e-mail"""
        print(self.random_name() + "." + str(self.random_number()) + "@" + self.random_word() + "." + str(*self.random_domain()))

    def __repr__(self):
        return f"len domains = {len(self.get_domains())}, len names = {len(self.get_names())}"


path_domains = "D:/IT/Phyton/test/domains.txt"
path_names = "D:/IT/Phyton/test/names.txt"
email_generator = EmailGenerator(path_domains, path_names)
print(email_generator.get_domains())
print(email_generator.get_names())
print(email_generator)
email_generator.generate_email()




