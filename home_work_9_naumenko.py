import random
import string

def create_random_string(min_limit = 100, max_limit = 1000) -> str:
    """Creates random string"""
    new_string = [random.choice(string.ascii_lowercase) for _ in range(random.randint(min_limit, max_limit))]
    return "".join(new_string)

def transform_string_with_spaces(string_to_transform):
    number_spaces = []
    while len(number_spaces) < len(string_to_transform) // 6:
        number = random.randint(5, -5)
        if number not in number_spaces:
            number_spaces.append(number)
    return string_to_transform



print(create_random_string())
