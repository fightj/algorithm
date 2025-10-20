# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
# 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
# 곱할 수 있는 배열만 주어집니다.
# 입출력 예
# arr1	arr2	return
# [[1, 4], [3, 2], [4, 1]]  /	[[3, 3], [3, 3]]    ->	[[15, 15], [15, 15], [15, 15]]
# [[2, 3, 2], [4, 2, 4], [3, 1, 4]]  /	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]   ->	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]

# arr1의 각 행을 arr2의 각 열과 곱해서 더한 값 구하기.

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        row_result = []
        for j in range(len(arr2[0])):
            value = 0
            for k in range(len(arr2)):
                value += arr1[i][k] * arr2[k][j]
            row_result.append(value)
        answer.append(row_result)
    return answer

# 3중첨 for문을 통해서 행을 먼저 구하고 append하는 방식.
# i와 j와 k를 손으로 쓰면서 for문의 중첩을 이해하는데 도움이 됨