def solution(n):
    answer = 0
    t = n
    a = ''
    while n > 0:
        a += str(n % 2)
        n //= 2
    cnt = 0
    for i in a:
        if i =='1':
            cnt += 1
    
    repeat = True
    while repeat:
        t += 1
        num = t
        b = ''
        while num > 0:
            b += str(num % 2)
            num //= 2
        b_cnt = 0
        for i in b:
            if i == '1':
                b_cnt += 1
                
        if cnt == b_cnt:
            answer = t
            repeat = False
            
    return answer

