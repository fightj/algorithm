lst1 = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
idx_x, idx_y = 0, 0

for i in range(9):
    for j in range(9):
        if max_num < lst1[i][j]:
            max_num = lst1[i][j]
            idx_x = i
            idx_y = j

print(max_num)
print(idx_x+1, idx_y+1)