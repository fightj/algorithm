# 문제 설명
# 캐시
# 지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
# 이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
# 어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

# 어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

# 입력 형식
# 캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.
# cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
# cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
# 각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.
# 출력 형식
# 입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력한다.
# 조건
# 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
# cache hit일 경우 실행시간은 1이다.
# cache miss일 경우 실행시간은 5이다.
# 입출력 예제
# 캐시크기(cacheSize)	도시이름(cities)	실행시간
# 3	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	50
# 3	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	21
# 2	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	60
# 5	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	52
# 2	["Jeju", "Pangyo", "NewYork", "newyork"]	16
# 0	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	25

def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    def check(n):
        if len(cache) < 0:
            return False
        for i in range(len(cache)):
            if n == cache[i][0]:
                cache[i][1] = 0
                return True
        return False
    
    def plus(n):
        if len(cache) < cacheSize:
            cache.append([n, 0])
            return True
        return False
    
#     def update_cache(n):
#         if len(cache) < cacheSize:
#             return False
#         min_use_idx = 31
#         min_num = float('-inf')
#         for i in range(len(cache)):
#             if cache[i][1] > min_num:
#                 min_num = cache[i][1]
#                 min_use_idx = i
    
#         cache[min_use_idx] = [n, 0]
#         return True
        
        
    for city in cities:
        city_name = city.upper()
        if check(city_name):
            answer += 1
            
        elif plus(city_name):
            answer += 5
        else:
            cache = sorted(cache, key=lambda x: x[1]) # 주목할 점.
            if len(cache)>0:
                cache[-1] = [city_name, 0]
            # update_cache(city_name)
            answer += 5
            
        for i in range(len(cache)):
            cache[i][1] += 1
            
    return answer

# 우선 이 문제는 LRU 페이지 교체 알고리즘을 알아야 풀 수 있는 문제였다.
# 그래서 구글링을 통해 가장 오랫동안 사용되지 않은 페이지를 교체하는 알고리즘이라는 것을 알게됨
# 그래서 cache라는 리스트에 ['도시명', 교체되지 않은 라운드 수] 형태로 저장함.
# 처음에는 update()라는 함수를 만들어서 페이지를 교체할 때 전부 순회하면서 가장 오랫동안 사용하지 않은 페이지를 찾아서 교체할려했는데 너무 비효율적이라는 생각이듦
# 그래서 cache = sorted(cache, key=lambda x: x[1]) sorted와 lambda를 이용해 특정 위치의 값을 기준으로 오름차순 정렬하기를 선택함