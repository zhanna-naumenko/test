from random import randint
import io
import os
import random


class EmailGenerator:
    number = 11
    sting = "Word!"


email_generator_instance = EmailGenerator
print(email_generator_instance.number)
print(email_generator_instance.sting)

email_generator_instance.number = 56
print(email_generator_instance.number)