def solution(brown, yellow):
    answer = []
    
    for i in range(1, brown//2):
        for j in range(1, brown//2):
            if i*j == yellow and (4 + (2*j) + (2*i)) == brown and len(answer)==0:
                answer.append(j+2)
                answer.append(i+2)
                break
    return answer

# 완전 탐색 문제
# 시간 초과 발생 -> for문 범위를 줄여서 해결