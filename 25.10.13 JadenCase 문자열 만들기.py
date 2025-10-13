def solution(s):
    answer = ''
    
    for i in range(len(s)):
        if i == 0 and isinstance(s[i], str):
            answer += s[i].upper()
        elif s[i-1] == ' ' and isinstance(s[i], str):
            answer += s[i].upper()
        elif s[i-1] != ' ' and isinstance(s[i], str):
            if s[i].isupper():
                answer += s[i].lower()
            else:
                answer += s[i]
            
        else:
            answer += s[i]
            
    return answer

# jadencase만들기 문제.
# 배운점: isinstance함수: 문자열의 타입을 확인. 첫번째 매개변수가 두번째 매개변수의 타입인지 확인
