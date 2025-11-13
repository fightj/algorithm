n, m = map(int, input().split())

lst1 = [list(map(int, input().split())) for _ in range(n)]
lst2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(lst1[i][j] + lst2[i][j], end=' ')
    print()

# map, end=' '문법을 오랜만에 다시 상기 시킬 수 있었음