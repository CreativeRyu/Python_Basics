list = [[1, 2, 3]]
result = 1

for i in range(1):
    result *= 10
    for j in range(1):
        list[i][j] *= result

print(list)