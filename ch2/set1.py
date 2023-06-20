# 파이썬 자료형
# 5. 집합
# set() : 자바의 Set 과 동일
# 중복을 허용하지 않음 - 중복 데이터를 담아도 지워버림
# 순서가 없음(==> 인덱싱 사용 불가)

set1 = set()
set2 = set([1, 12, 13, 14])
set3 = set([1, 4, 5, 6, 6, 6])

print(set1)
print(set2)
print(set3) # {1, 4, 5, 6} - 중복제거하고 나옴

t1 = (1,3,5,7)
set4 = set(t1)
print(set4) # {1, 3, 5, 7} - 키 밸류 형태가 아니어서  set 구조임

dict1 = {"a":10,"b":20,"c":30}
set5 = set(dict1)
print(set5) # {'b', 'c', 'a'} - 순서가 없음 아무렇게나 나올수있음 , 키 값만 가지고 나옴

str1 ="abcdefg"
print(set(str1))    # {'c', 'd', 'e', 'g', 'a', 'b', 'f'}

# 딕셔너리 리스트 문자열 셋구조로 될수있음


# set => list, tuple
print(list(set2))   # [1, 12, 13, 14]
print(tuple(set2))  # (1, 12, 13, 14)

# 함수
# 교집합, 합집합, 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print("교집합")
print(s1 & s2)
print(s1.intersection(s2))

print("합집합")
print(s1 | s2)
print(s1.union(s2))

print("차집합")
print(s1 - s2)
print(s1.difference(s2))

# add() - 1개의 값만 추가
s1.add(9)
print(s1)

# update() - 여러 개의 값 추가
s1.update([10,11,12])
print(s1)

# remove() - 특정 값 제거
s1.remove(10)
print(s1)