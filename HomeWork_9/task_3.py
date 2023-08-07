def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


sentence = input('введите текст')
result = longest_word(sentence)
print(result)