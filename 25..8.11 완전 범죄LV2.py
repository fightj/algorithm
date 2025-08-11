def solution(info, n, m):
    # 메모이제이션용 딕셔너리
    memo = {}
    
    def dfs(idx, a, b):
        # 이미 계산된 상태인지 확인
        if (idx, a, b) in memo:
            return memo[(idx, a, b)]
        
        # 모든 물건을 처리했을 때
        if idx == len(info):
            # 두 도둑 모두 붙잡히지 않은 경우
            if a < n and b < m:
                result = a  # A도둑의 흔적 개수 반환
            else:
                result = float('inf')  # 불가능한 경우
            memo[(idx, a, b)] = result
            return result
        
        # 현재 물건을 A도둑이 훔치는 경우
        result_a = float('inf')
        if a + info[idx][0] < n:  # A도둑이 붙잡히지 않는 경우만
            result_a = dfs(idx + 1, a + info[idx][0], b)
        
        # 현재 물건을 B도둑이 훔치는 경우
        result_b = float('inf')
        if b + info[idx][1] < m:  # B도둑이 붙잡히지 않는 경우만
            result_b = dfs(idx + 1, a, b + info[idx][1])
        
        # 두 경우 중 A도둑의 흔적이 더 적은 경우 선택
        result = min(result_a, result_b)
        memo[(idx, a, b)] = result
        return result
    
    result = dfs(0, 0, 0)
    return -1 if result == float('inf') else result

# ---------------------------------------------------
# dfs와 메모이제이션 활용 문제
# dfs만으로는 시간초과 발생.