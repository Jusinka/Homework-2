def hide_email(email):

    at_index = email.find('@')


    first_part = email[:2]


    last_part = email[at_index:]


    hidden_part = '*' * (at_index - 3)


    hidden_email = first_part + hidden_part + last_part

    return hidden_email



email = input("somebody_email@gmail.com")
result = hide_email(email)
print(result)