import csv
import re

eng_to_ukr = {
    'A': 'А',
    'B': 'В',
    'C': 'С',
    'E': 'Е',
    'H': 'Н',
    'I': 'І',
    'K': 'К',
    'M': 'М',
    'O': 'О',
    'P': 'Р',
    'T': 'Т',
    'Y': 'У',
    'X': 'Х',
    'a': 'а',
    'b': 'в',
    'c': 'с',
    'e': 'е',
    'i': 'і',
    'k': 'к',
    'm': 'м',
    'o': 'о',
    'p': 'р',
    'x': 'х',
}


def replace_eng_chars_with_ukr(text):
    translation = str.maketrans(eng_to_ukr)
    return text.translate(translation)


def find_region_by_auto_numbers(auto_number):
    auto_number = replace_eng_chars_with_ukr(auto_number)

    if not re.fullmatch(r'(\w\w\d{4}\w\w)', auto_number, flags=re.IGNORECASE):
        return False

    with open('ua_auto.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if auto_number[:2] in (row['Код 2004'], row['Код 2013']):
                return row['Регіон']

    return False


user_input = input("Enter the auto number: ")
result = find_region_by_auto_numbers(user_input)
if result:
    print(f"Region: {result}")
else:
    print("No matching region found.")