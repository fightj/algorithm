lst = [[-1]*15 for _ in range(5)]

for i in range(5):
    data = input()
    for j in range(len(data)):
        lst[i][j] = data[j]
result = ''

for i in range(15):
    for j in range(5):
        if lst[j][i] != -1:
            result += lst[j][i]

print(result)