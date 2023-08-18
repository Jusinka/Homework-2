numbers = []
while True:
    num = int(input("Введіть число (0 для завершення): "))
    if num == 0:
        break
    numbers.append(num)

count = len(numbers)
sum_of_numbers = sum(numbers)
product = 1
for num in numbers:
    product *= num

average = sum_of_numbers / count

max_value = max(numbers)
max_index = numbers.index(max_value) + 1

even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = count - even_count

sorted_numbers = sorted(numbers, reverse=True)
second_largest = sorted_numbers[1]

max_count = numbers.count(max_value)

print("Кількість введених чисел:", count)
print("Сума чисел:", sum_of_numbers)
print("Добуток чисел:", product)
print("Середнє арифметичне:", average)
print("Значення найбільшого елемента:", max_value)
print("Порядковий номер найбільшого елемента:", max_index)
print("Кількість парних елементів:", even_count)
print("Кількість непарних елементів:", odd_count)
print("Значення другого за величиною елемента:", second_largest)
print("Кількість елементів, що дорівнюють найбільшому елементу:", max_count)