# 문제 설명
# XX게임에는 피로도 시스템(0 이상의 정수로 표현합니다)이 있으며, 일정 피로도를 사용해서 던전을 탐험할 수 있습니다. 이때, 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있습니다. "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며, "소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다. 예를 들어 "최소 필요 피로도"가 80, "소모 피로도"가 20인 던전을 탐험하기 위해서는 유저의 현재 남은 피로도는 80 이상 이어야 하며, 던전을 탐험한 후에는 피로도 20이 소모됩니다.

# 이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데, 한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다. 유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# k는 1 이상 5,000 이하인 자연수입니다.
# dungeons의 세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하입니다.
# dungeons의 가로(열) 길이는 2 입니다.
# dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"] 입니다.
# "최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다.
# "최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수입니다.
# 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다.
# 입출력 예
# k	dungeons	result
# 80	[[80,20],[50,40],[30,10]]	3
# 입출력 예 설명
# 현재 피로도는 80입니다.

# 만약, 첫 번째 → 두 번째 → 세 번째 던전 순서로 탐험한다면

# 현재 피로도는 80이며, 첫 번째 던전을 돌기위해 필요한 "최소 필요 피로도" 또한 80이므로, 첫 번째 던전을 탐험할 수 있습니다. 첫 번째 던전의 "소모 피로도"는 20이므로, 던전을 탐험한 후 남은 피로도는 60입니다.
# 남은 피로도는 60이며, 두 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 50이므로, 두 번째 던전을 탐험할 수 있습니다. 두 번째 던전의 "소모 피로도"는 40이므로, 던전을 탐험한 후 남은 피로도는 20입니다.
# 남은 피로도는 20이며, 세 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 30입니다. 따라서 세 번째 던전은 탐험할 수 없습니다.
# 만약, 첫 번째 → 세 번째 → 두 번째 던전 순서로 탐험한다면

# 현재 피로도는 80이며, 첫 번째 던전을 돌기위해 필요한 "최소 필요 피로도" 또한 80이므로, 첫 번째 던전을 탐험할 수 있습니다. 첫 번째 던전의 "소모 피로도"는 20이므로, 던전을 탐험한 후 남은 피로도는 60입니다.
# 남은 피로도는 60이며, 세 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 30이므로, 세 번째 던전을 탐험할 수 있습니다. 세 번째 던전의 "소모 피로도"는 10이므로, 던전을 탐험한 후 남은 피로도는 50입니다.
# 남은 피로도는 50이며, 두 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 50이므로, 두 번째 던전을 탐험할 수 있습니다. 두 번째 던전의 "소모 피로도"는 40이므로, 던전을 탐험한 후 남은 피로도는 10입니다.
# 따라서 이 경우 세 던전을 모두 탐험할 수 있으며, 유저가 탐험할 수 있는 최대 던전 수는 3입니다.

import itertools
def solution(k, dungeons):
    answer = 0
    a = list(itertools.permutations(dungeons))
    
    for i in range(len(a)):
        current = k
        cnt = 0
        for need_e, e in a[i]:
            if current < need_e:
                continue
            else:
                current -= e
                cnt += 1
        if cnt > answer:
            answer = cnt
            
    return answer

# 던전의 최대 갯수가 8개라는 점에서 그냥 가능한 모든 순서를 itertools의 permutations툴을 이용해서 순열을 만들었음
# 그리고 나서 가능한 모든 경우의 수를 다 계산.
# itertools.permutations(특정 리스트)를 사용하면 해당 리스트로 만들 수 있는 모든 순열을 반환해줌

# data = [1, 2, 3]
# result = list(itertools.permutations(data))
# 이렇게 하면 결과
# [(1, 2, 3), (1, 3, 2),
#  (2, 1, 3), (2, 3, 1),
#  (3, 1, 2), (3, 2, 1)]

# 순열 길이 지정 (r)이 가능함. 
# data = [1, 2, 3]
# result = list(itertools.permutations(data, 2))
# 이렇게 하면 결과
# [(1, 2), (1, 3),
#  (2, 1), (2, 3),
#  (3, 1), (3, 2)]

# 문자열에서도 가능
# for p in itertools.permutations("ABC", 2):
#     print(''.join(p))
# AB
# AC
# BA
# BC
# CA
# CB

import itertools

data = [1, 2, 3]

# 순열
print(list(itertools.permutations(data, 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 조합
print(list(itertools.combinations(data, 2)))
# [(1, 2), (1, 3), (2, 3)]

# 중복 조합
print(list(itertools.combinations_with_replacement(data, 2)))
# [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

# product도 있음. 모든 가능한 곱집합(cartesian product) 을 만들어주는 함수예요.
# 쉽게 말해, “중복을 허용한 모든 순서쌍(혹은 n쌍)”을 만듭니다.

import itertools

data = [1, 2, 3]
result = list(itertools.product(data, repeat=2))
print(result)
# [(1, 1), (1, 2), (1, 3),
#  (2, 1), (2, 2), (2, 3),
#  (3, 1), (3, 2), (3, 3)]

colors = ["red", "blue"]
sizes = ["S", "M", "L"]

result = list(itertools.product(colors, sizes))
print(result)

# [('red', 'S'), ('red', 'M'), ('red', 'L'),
#  ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]



# 이건 다른 사람의 DFS 풀이

answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
