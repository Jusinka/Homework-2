def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]

    common_numbers = set(list1) & set(list2)
    unique_to_list1 = set(list1) - set(list2)
    unique_to_list2 = set(list2) - set(list1)

    print("Числа, що містяться одночасно у першому та другому списку:", common_numbers)
    print("Числа, що містяться у першому, але відсутні у другому списку:", unique_to_list1)
    print("Числа, що містяться у другому, але відсутні у першому списку:", unique_to_list2)

if __name__ == "__main__":
    main()