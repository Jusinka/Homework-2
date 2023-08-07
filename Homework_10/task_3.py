def shift_list(lst, n):
    if n == 0:
        return lst

    length = len(lst)
    n = n % length

    if n < 0:
        n = length + n

    return lst[-n:] + lst[:-n]



original_list = [1, 2, 3, 4, 5]
shifted_list = shift_list(original_list, -2)
print(shifted_list)