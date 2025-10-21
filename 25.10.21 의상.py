# 문제 설명
# 코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.

# 예를 들어 코니가 가진 옷이 아래와 같고, 오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

# 종류	이름
# 얼굴	동그란 안경, 검정 선글라스
# 상의	파란색 티셔츠
# 하의	청바지
# 겉옷	긴 코트
# 코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. 예를 들어 위 예시의 경우 동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.
# 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
# 코니는 하루에 최소 한 개의 의상은 입습니다.
# 코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 코니가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.

def solution(clothes):
    answer = 1
    
    category = {}
    for name, cate in clothes:
        category[cate] = category.get(cate, 0) + 1
        
    print(category)
    
    for n in category.values():
        answer = answer * (n+1)
        
    return answer-1

# 처음에는 경우의 수를 itertools를 이용해서 순열로 모든 경우의 수를 계산하려 했음
# 하지만 모든 경우의 수는 그냥 단순 곱셈이 답임
# 이 문제에서는 각 카테고리를 딕셔너리를 이용해서 1차적으로 전처리를 해줘야 했음

# 딕셔너리 관련 함수
# person.setdefault("city", "Busan")

# 🧩 3️⃣ 값 수정 & 추가

# 기존 key 값 수정	person["age"] = 27	"age": 27
# 새로운 key 추가	person["hobby"] = "coding"	"hobby": "coding"
# update()로 여러 개 수정/추가	person.update({"age": 28, "city": "Seoul"})	한 번에 변경 가능

# 🧩 4️⃣ 값 삭제

# 특정 key 삭제	del person["job"]	"job" 제거
# 특정 key 삭제하고 값 반환	person.pop("age")	"age" 제거 후 값 반환
# 맨 마지막 key 제거 (3.7+)	person.popitem()	마지막 (key, value) 튜플 반환
# 전체 비우기	person.clear()	{}

# students = {
#     "A": {"name": "민준", "grade": "A"},
#     "B": {"name": "서연", "grade": "B"}
# }

# print(students["A"]["name"])  # "민준"
