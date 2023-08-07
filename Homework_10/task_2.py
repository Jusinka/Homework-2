def is_palindrome(text):

    cleaned_text = ''.join(filter(str.isalpha, text.lower()))


    return cleaned_text == cleaned_text[::-1]


input_text = input("Введіть текст: ")

if is_palindrome(input_text):
    print("Введений текст є паліндромом.")
else:
    print("Введений текст не є паліндромом.")