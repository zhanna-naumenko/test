import json
import re


def open_json_file():
    """Opens file data.json"""
    with open("data.json", "r", encoding="utf-8") as file:
        mathematics = json.load(file)
    return mathematics


print(open_json_file())


#################################################################

def sort_names(mathematic):
    """Sorting full name or name from file data.json"""
    name_math = mathematic["name"]
    full_name = name_math[name_math.rfind(" ")+1]
    return full_name


names_of_mathematics = sorted(open_json_file(), key=sort_names)
print(names_of_mathematics)
#################################################################
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

def sort_dates(date_of_death):
    """Sorting dates of death of mathematics"""
    years_math = date_of_death["years"]
    years = re.findall(r"\d+$", years_math)
    return years

math_year_death = sorted(open_json_file(), key=sort_dates)
print(math_year_death)
#################################################################

def sort_lens_of_text(text):
    phrase_math = text["text"]
    return len(phrase_math)

phrase_len = sorted(open_json_file(), key=sort_lens_of_text)
print(phrase_len)
