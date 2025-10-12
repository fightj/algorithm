def solution(s):
    a = s.split(' ')
    b = []
    for i in a:
        i = int(i)
        b.append(i)
    b.sort()
    
    answer = "{0} {1}".format(b[0],b[-1])
    return answer


# 간단한 최댓값 최솟값 해결 문제. 하지만 문자열 파싱에서 시간이 많이 소모됨.
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
# 이건 아주 간단한 풀이.
# 프린트를 할때 
f'{min(s)} {max(s)}'
# 이렇게 표현해도 됨.