def solution(s):
    # 1. 문자열 전처리
    s = s[2:-2]              # 바깥쪽 {{ }}
    s = s.split("},{")       # 구분자로 분리
    
    # 2. 문자열을 set으로 변환
    sets = [set(map(int, x.split(','))) for x in s]
    
    # 3. 길이 순서대로 정렬
    sets.sort(key=len)
    
    # 4. 결과 튜플 만들기
    answer = []
    for s in sets:
        new = s - set(answer)   # 이전에 없던 원소만 추출
        answer.append(list(new)[0])
    
    return answer
