# 문제 설명
# 정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

# n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
# i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
# 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
# 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
# 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
# 정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 107
# 0 ≤ left ≤ right < n2
# right - left < 105
# 입출력 예
# n	left	right	result
# 3	2	5	[3,2,2,3]
# 4	7	14	[4,3,3,3,4,4,4,4]


# 기존 풀이 (시간 초과)
def solution(n, left, right):
    answer = []
    arr = [[0]*n for _ in range(n)] 
#초기에는 arr = [[0]*n] * n 이렇게 했는데, 이건 잘못된 것임.이건 같은 리스트 객체를 n번 참조하는 형태예요. 그래서
# arr[i][i] = i+1  -> [[1, 2, 3], [1, 2, 3], [1, 2, 3]] 이렇게 나오게 됨.

# 한 번 할 때마다 “i번째 열 전체”가 바뀝니다.
# i=0 → 첫 번째 열이 전부 1
# i=1 → 두 번째 열이 전부 2
# i=2 → 세 번째 열이 전부 3

    for i in range(n):
        arr[i][i] = i+1
        for j in range(i, -1, -1):
            arr[i][j] = i + 1
            arr[j][i] = i+ 1
    lst = []        
    for i in range(n):
        for j in arr[i]:
            lst.append(j)
    
    return lst[left:right+1]

# 저렇게 풀이를 했더니 시간 초과남.
# 시간 복잡도 O(n^2)

def solution(n, left, right):
    answer = []
    for k in range(left, right + 1):
        row = k // n
        col = k % n
        # arr[row][col]에 들어갈 값을 arr 패턴 기반으로 계산
       
        val = max(row, col) + 1
        answer.append(val)
    return answer

# 이게 정답 코드. 시간 복잡도 O(right - left + 1)