def fake_string(input_string, old_word, new_word, replacements):
    new_string = input_string.replace(old_word, new_word, replacements)
    return new_string

input_text = 'DC makes good movies, DC makes good comics'
old_word = 'DC'
new_word = 'Marvel'
replacements = 2

result = fake_string(input_text, old_word, new_word, replacements)
print(result)