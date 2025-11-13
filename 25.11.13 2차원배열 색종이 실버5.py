lst = [[0]*100 for _ in range(100)]
n = int(input())
result = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            lst[x+i][y+j] += 1

for i in range(100):
    for j in range(100):
        if lst[i][j] != 0:
            result += 1

print(result)