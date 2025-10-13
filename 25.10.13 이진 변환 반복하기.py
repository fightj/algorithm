def solution(s):
    answer = []
    repeat_cnt = 1
    zero_cnt = 0
    
    def change(n):
        result = ''
        while n > 0:
            result += str(n % 2)
            n = n//2
        return result[::-1]
    
    while s != '1':
        t = 0
        for i in s:
            if i == '0':
                zero_cnt += 1
            else:
                t += 1
        if t == 1:
            break
        else:
            s = change(t)
            repeat_cnt +=1
            
    answer.append(repeat_cnt)
    answer.append(zero_cnt)
    return answer

# s가 '1'이 될때까지 0을 제거하고 그 1의 갯수(s의 길이)를 2진으로 변경하고, 그 변경횟수와 0을 제거한 횟수를 각각 anwer[a,b]로 나타내는 문제.
# 배운점: 2진법은 스택형식으로 다 쌓고 순서대로 pop한 결과와 동일함.
#        result[::-1]을 이용해서 문자열을 거꾸로 할 수 있음.