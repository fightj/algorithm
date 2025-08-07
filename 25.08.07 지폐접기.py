def solution(wallet, bill):
    answer = 0
    w1, w2 = wallet[0], wallet[1]
    b1, b2 = bill[0], bill[1]
    suc = True
    while suc:
        if (b1 <= w1 and b2 <= w2) or (b2 <= w1 and b1 <= w2):
            suc = False
        else:
            b1, b2 = fun1(b1,b2)
            answer +=1
    return answer

def fun1(a,b):
    if a >= b:
        a = a//2
    else:
        b = b//2
    return a, b

# ----------------------------
# 새로운 함수를 작성하고 가져다 쓰는 연습을 했음. 문제 자체는 어려운 부분이 없었음.