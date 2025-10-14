def solution(s):
    answer = -1
    stack = []
    
    for i in s:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    if len(stack) ==0:
        answer = 1
    else:
        answer = 0

    return answer

# 문자열이 abbaacc처럼 같은 문자열이 붙어있으면 짝지어 제거 가능. 전부 제거 가능한지 확인하는 알고리즘
# stack을 활용.
