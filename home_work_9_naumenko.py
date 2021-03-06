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

def change_first_symbol(word):
    return word.capitalize()

def change_last_symbol(word):
    punctuation = ",.!?"
    word = word[:-1] + random.choice(punctuation) if len(word) > 3 else word
    return word

def change_word_to_number(word):
    if len(word) <= 3:
        number_list = [str(random.randint(0, 9)) for _ in range(len(word))]
        word = "".join(number_list)
    return word

def add_paragraph(string_to_transform):
    lines = string_to_transform.splitlines()
    for word in lines:
        return "\n" + word


def random_word_transform(word):
    state = random.randint(1, 6)
    if state == 1:
        word = change_first_symbol(word)
    elif state == 2:
        word = change_last_symbol(word)
    elif state == 3:
        word = change_word_to_number(word)
    elif state == 4:
        word = add_paragraph(word)
    return word


def transform_words(string_to_transform):
    words = string_to_transform.split()
    new_words = []
    for word in words:
        new_word = random_word_transform(word)
        new_words.append(new_word)
    return " ".join(new_words)


result = create_random_string()
result = transform_string_with_spaces(result)
result = transform_words(result)

print(result)

##################################################################

