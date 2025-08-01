def solution(s, t, start):
    answer = 0

    for i in range(len(s)):
        is_valid = True

        # 희망 시간 → 분 단위로 변환
        hope = s[i] // 100 * 60 + s[i] % 100

        for j in range(7):
            # 요일 계산 (1 = 월요일, 7 = 일요일)
            weekday = (start + j - 1) % 7 + 1
            if weekday in [6, 7]:  # 주말은 패스
                continue

            # 출근 시간 → 분 단위로 변환
            commute = t[i][j] // 100 * 60 + t[i][j] % 100

            if commute > hope + 10:  # 10분 초과하면 실격
                is_valid = False
                break

        if is_valid:
            answer += 1

    return answer
# ---------------------------------------------------------
# 단순한 문제. 하지만 시간 변환을 하지 않아서 예외 케이스에서 틀린 문제.