def count_points(win, draw, loss):
    return win * 3 + draw * 1 + loss * (-1)

result = count_points(3, 2, 2)
print(result)