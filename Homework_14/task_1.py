import csv
import re

class VehicleRegistration:
    LATIN_CHARS = "ABEIKMHOPCTX"
    CYRILLIC_CHARS = "АВЕІКМНОРСТХ"
    PATTERN = r"(?P<prefix>[А-Я]{2})\s*\d{4}\s*[А-Я]{2}"

    def __init__(self, reg_number):
        self.reg_number = reg_number.upper()

    def is_english(self, s):
        english_alphabet = "abcdefghijklmnopqrstuvwxyz"
        return set(s.lower()).issubset(set(english_alphabet))

    def translate_eng_ua(self, s):
        table = str.maketrans(self.LATIN_CHARS, self.CYRILLIC_CHARS)
        return s.translate(table)

    def is_car_plate_chars(self, s):
        return set(s).issubset(set(self.LATIN_CHARS)) or set(s).issubset(set(self.CYRILLIC_CHARS))

    def get_region(self):
        letters = ''.join(filter(str.isalpha, self.reg_number))
        if not self.is_car_plate_chars(letters):
            raise ValueError(f"{self.reg_number} is not a Ukrainian vehicle registration number")
        if self.is_english(letters):
            return self.translate_eng_ua(self.reg_number)
        return self.reg_number

    @staticmethod
    def identify_region(prefix):
        with open('ua_auto.csv', encoding='utf8') as f:
            dict_reader = csv.DictReader(f)
            for row in dict_reader:
                if row['Код 2004'] == prefix or row['Код 2013'] == prefix:
                    return row['Регіон']
            raise ValueError(f"There is no region with such prefix: '{prefix}'")

def main():
    user_input = input("Enter the vehicle registration number: ")
    vehicle = VehicleRegistration(user_input)
    match = re.search(vehicle.PATTERN, user_input)
    if match is None:
        raise ValueError(f"{user_input} - is an incorrect number")
    code = match.groupdict()
    return VehicleRegistration.identify_region(code['prefix'])

if __name__ == '__main__':
    print(main())