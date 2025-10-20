# 문제 설명
# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
# 입출력 예
# citations	return
# [3, 0, 6, 1, 5]	3
# 입출력 예 설명
# 이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

def solution(citations):
    
    h = 0
    array = []
    for i in range(max(citations), -1, -1):
        if i in array:
            continue
        else:
            array.append(i)
            
        if h > i or i > len(citations):
            continue
        cnt = 0
        for j in citations:
                if j >= i:
                    cnt += 1

        if cnt >= i:
            h = i
            
    return h

# 단순히 구현했는데, 아슬아슬하게 통과.

# 이후 다른 풀이
def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i >= c:
            return i
    return len(citations)

# 약 9000배 차이가 남.
# 즉, 큰 수부터 줄 세워서 해당 인덱스 값이랑 그 인덱스에 해당하는 c를 비교.

# 예: [6, 5, 3, 1, 0]
# → 0번 인덱스: 6 ≥ 1 ✅
# → 1번 인덱스: 5 ≥ 2 ✅
# → 2번 인덱스: 3 ≥ 3 ✅
# → 3번 인덱스: 1 < 4 ❌ → 정답 = 3