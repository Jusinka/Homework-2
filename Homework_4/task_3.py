A = int(input("Введіть число A: "))
B = int(input("Введіть число B: "))

if A < B:
    for num in range(A, B + 1):
        print(num, end=" ")
else:
    for num in range(A, B - 1, -1):
        print(num, end=" ")