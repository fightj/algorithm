def solution(s):
    answer = True
    cnt = 0
    if s[0] == ')':
        answer = False
    elif s[-1] == '(':
        answer = False
    else:
        for i in range(len(s)):
            
            if cnt < 0:
                answer = False
                break
            elif s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
                
        if cnt != 0:
            answer = False
    
    return answer

# ()가 제대로 닫혔는지 확인하는 문제.
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0
# 이건 try, except를 활용한 문제풀이.