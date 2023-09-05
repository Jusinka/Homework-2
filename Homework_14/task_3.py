import re

def validate_password(password):

    if len(password) < 8:
        return False


    if not re.search(r'[a-z]', password):
        return False


    if not re.search(r'[A-Z]', password):
        return False


    if not re.search(r'[0-9]', password):
        return False


    if not re.search(r'[$#@+=-]', password):
        return False

    return True


user_password = input("Введіть пароль: ")

if validate_password(user_password):
    print("Пароль відповідає вимогам.")
else:
    print("Пароль не відповідає вимогам.")