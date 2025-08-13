def solution(storage, requests):
    answer = 0
    n = len(storage)  # 세로길이
    m = len(storage[0])  # 가로길이
    
    # storage를 2차원 리스트로 변환 (수정 가능하도록)
    grid = []
    for i in range(n):
        grid.append(list(storage[i]))
    
    def find_accessible_containers(target_char, current_grid):
        """현재 grid 상태에서 접근 가능한 target_char 컨테이너들을 모두 찾기"""
        accessible_positions = set()
        
        for x in range(n):
            for y in range(m):
                if current_grid[x][y] == target_char:
                    # BFS로 외부까지 도달 가능한지 확인
                    if can_reach_boundary(x, y, target_char, current_grid):
                        accessible_positions.add((x, y))
        
        return accessible_positions
    
    def can_reach_boundary(start_x, start_y, target_char, current_grid):
        """특정 위치에서 경계까지 도달할 수 있는지 BFS로 확인"""
        visited = set()
        queue = [(start_x, start_y)]
        visited.add((start_x, start_y))
        
        while queue:
            x, y = queue.pop(0)
            
            # 경계에 도달했으면 접근 가능
            if x == 0 or x == n-1 or y == 0 or y == m-1:
                return True
            
            # 4방향으로 이동
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited):
                    # 같은 종류 컨테이너이거나 빈 공간('0')이면 이동 가능
                    if current_grid[nx][ny] == current_grid[nx][ny] == '0':
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        return False
    
    for req in requests:
        if len(req) == 2:  # 크레인 사용 (같은 문자 2개)
            target_char = req[0]  # "BB" -> "B"
            # 해당 종류의 모든 컨테이너 제거
            for x in range(n):
                for y in range(m):
                    if grid[x][y] == target_char:
                        grid[x][y] = '0'
        
        else:  # 지게차 사용 (단일 문자)
            target_char = req  # "A"
            # 현재 상태에서 접근 가능한 컨테이너들을 먼저 모두 찾기
            accessible_positions = find_accessible_containers(target_char, grid)
            
            # 디버깅용 출력
            # print(f"Request: {req}, Accessible positions: {accessible_positions}")
            
            # 찾은 위치들을 한 번에 제거
            for x, y in accessible_positions:
                grid[x][y] = '0'
                
        # 각 단계별 grid 상태 출력
        # print(f"After {req}:")
        # for row in grid:
            # print(row)
    
    # 남은 컨테이너 개수 계산
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '0':
                answer += 1
    
    return answer

# ----------------------------------------------------------------------
# dfs로 처음에 시도했다가 틀림.
# claude 도움을 받아서 해결. bfs 문법에 대해서 학습.
# 조심해야 했던 부분 1. 'BB'와 같은 문자열을 'B'로 변경하지 않았음. 2. req가 변경될때마다 한번에 grid를 변경해야함.