def solution(players, m, k):
    answer = 0
    server_plus = []
    for i in range(24):
        person = players[i]
        access_person = m-1
        for a in server_plus:
            if i < a[0] + k:
                access_person += a[1] * m
        if person > access_person:
            plus = (person - access_person) // m
            if (person - access_person) % m != 0:
                plus += 1
            server_plus.append([i,plus])
            print(i)
            answer += plus
    return answer

# ------------------------------------------------------
# 비교적 간단한 문제지만 server_plus 배열을 만들어서 증설한 시각과 갯수를 배열로 관리하여 for문 마다 access_person수 계산
# 그리디 문제