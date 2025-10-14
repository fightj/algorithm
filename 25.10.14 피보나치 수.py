def solution(n):
    answer = 0
    p = [0, 1]
    
    while len(p)-1 < n:
        c = p[-1] + p[-2]
        p.append(c)
           
    answer = p[-1] % 1234567
    return answer

