import re

def format_phone_number(phone_number):

    cleaned_number = re.sub(r'\D', '', phone_number)


    if len(cleaned_number) == 10:

        formatted_number = f'(+38) {cleaned_number[:3]} {cleaned_number[3:6]}-{cleaned_number[6:8]}-{cleaned_number[8:10]}'
        return formatted_number
    else:
        return 'Failed to recognize number'


user_input = input("Введіть номер телефону: ")

formatted_result = format_phone_number(user_input)
print(formatted_result)