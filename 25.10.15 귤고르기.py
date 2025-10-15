def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    a = [0]*10000001
    
    for i in tangerine:
        a[i] += 1
    a.sort(reverse = True)
    while k > 0:
        k -= a[0]
        a.pop(0)
        answer += 1
        
    return answer

# 이렇게 했더니 시간 초과가 남.

def solution(k, tangerine):
    answer = 0
    a = set([])
    for i in tangerine:
        a.add(i)
        
    b = []
    
    for i in a:
        b.append(tangerine.count(i))
        
    b.sort()
    t = 1
    while k >0:
        k -= b[len(b)-t]
        answer +=1
        t += 1
        
    return answer

# 이번엔 set()를 활용해봤는데 이것 역시 시간초과

def solution(k, tangerine):
    answer = 0
    a = []
    tangerine.sort()
    
    cnt = 1
    for i in range(1, len(tangerine)):
        if tangerine[i-1] == tangerine[i]:
            cnt += 1
        else:
            a.append(cnt)
            cnt = 1  # 새로운 그룹 시작
    
    # 마지막 그룹 추가
    a.append(cnt)
    
    # 개수 내림차순 정렬
    a.sort(reverse=True)
    
    b = 0
    while k > 0 and b < len(a):
        k -= a[b]
        answer += 1
        b += 1
        
    return answer
#  정답코드
# 이전 값과 같은지 비교하고 같으면 cnt를 차곡차곡 쌓아서 이전값과 달라지면 append

import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)
    
    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer
# counter함수를 이용하면 다음과 같이 해결이 가능함. (다른 사람 풀이법)
# counter를 사용하면 	Counter({3: 2, 2: 2, 5: 2, 1: 1, 4: 1}) 이런 딕셔너리 형태로 저장됨