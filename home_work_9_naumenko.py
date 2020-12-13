import random
import string

def create_random_string(min_limit = 100, max_limit = 1000) -> str:
    """Creates random string"""
    new_string = [random.choice(string.ascii_lowercase) for _ in range(random.randint(min_limit, max_limit))]
    return "".join(new_string)

def transform_string_with_spaces(string_to_transform):
    number_spaces = []
    while len(number_spaces) < len(string_to_transform) // 6:
        number = random.randint(5, len(string_to_transform) - 5)
        if number not in number_spaces:
            number_spaces.append(number)
    for number in number_spaces:
        string_to_transform = string_to_transform[:number] + " " + string_to_transform[number + 1:]
    return string_to_transform

def random_word_transform(word):
    return word

def transform_words(string_to_transform):
    words = string_to_transform.split()
    new_words = []
    for word in words:
        new_word = random_word_transform(word)
        new_words.append(new_word)
    return " ".join(new_words)

result = create_random_string()
result = transform_string_with_spaces(create_random_string())
result = transform_words(result)
print(result)
