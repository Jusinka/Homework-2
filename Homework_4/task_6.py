def count_elements_with_neighbors_greater_than_neighbors(numbers):
    count = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            count += 1
    return count

# Вхідний список чисел
numbers = [5, 8, 2, 7, 12, 6, 9]

result = count_elements_with_neighbors_greater_than_neighbors(numbers)
print(f"Кількість елементів, які більше обох своїх сусідів: {result}")