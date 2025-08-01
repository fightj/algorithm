def solution(n, w, num):
    idx = num - 1
    col = idx // w
    row = idx % w
    
    if col % 2 == 1:
        row = w - row - 1
        
    max = 100//w
    count = 1
    
    for i in range(col+1, max):
        if i % 2 == 0:
            target = i * w + row
        elif i%2==1:
            target = i * w + (w - row -1)
        
        
        if target < n:
            count +=1
            
    return count
# ----------------------------------------------
# 지그재그 문제.
# 문제 풀이 접근 방법: 타겟 상자위치 (col, row)를 구한 다음 위에 상자 번호가 n보다 작거나 같은지 확인.
