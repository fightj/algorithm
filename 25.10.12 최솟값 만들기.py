def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse = True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

# 두 배열에서 무작위 번째 숫자를 꺼내서 각각 곱한 후 누적 합이 최소가 되게 만드는 문제.
# 두 리스트를 정렬하여 각각 오름차순, 내림차순으로 정렬하여 각 숫자를 곱한 값이 최소가 됨.

def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
# 이건 sum, zip 함수를 이용해서 좀 더 간단하게 풀이한 예시