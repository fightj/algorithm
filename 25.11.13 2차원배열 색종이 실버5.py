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


# 보다 더 최적화 하는 방법
lst = [[False]*100 for _ in range(100)]
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            lst[x+i][y+j] = True

result = sum(sum(row) for row in lst)
print(result)
# true, false로 메모리를 더 아낄 수 있음 그리고 더 빠름