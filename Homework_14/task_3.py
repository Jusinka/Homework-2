import re

def validate_password(password):
    error_messages = []

    if len(password) < 8:
        error_messages.append("Пароль должен содержать не менее 8 символов.")

    if not re.search(r'[a-z]', password):
        error_messages.append("Пароль должен содержать хотя бы одну строчную букву.")

    if not re.search(r'[A-Z]', password):
        error_messages.append("Пароль должен содержать хотя бы одну заглавную букву.")

    if not re.search(r'[0-9]', password):
        error_messages.append("Пароль должен содержать хотя бы одну цифру.")

    if not re.search(r'[$#@+=-]', password):
        error_messages.append("Пароль должен содержать хотя бы один из символов: $, #, @, +, =, -")

    if error_messages:
        return "\n".join(error_messages)
    else:
        return "Пароль відповідає вимогам."

user_password = input("Введіть пароль: ")
validation_result = validate_password(user_password)

if validation_result == "Пароль відповідає вимогам.":
    print(validation_result)
else:
    print("Помилка пароля:",validation_result)

