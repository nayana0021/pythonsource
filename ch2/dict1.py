# 파이썬 자료형
# 4. 딕셔너리(자바의 Map 동일 : key, value) - key값 중복 안됨 value 중복 가능
# {} 사용

# key 값은 str, int 가능
# value 값은 str, int, list, tuple, dictionary
dict1 = {"name": "park", "age": "12"}
print(dict1)    # {'name': 'park', 'age': '12'}

# 특정 키에 해당하는 value 출력
print(dict1["name"])
print(dict1["age"])
# print(dict1["addr"])      KeyError: 'addr' - 없는 값은 keyError

dict2 = {0: "Hello Python", 1: "Hello Java"}
print(dict2)
print(dict2[0])

dict3 = {"arr": [1, 2, 3, 4]}
print(dict3)    # {'arr': [1, 2, 3, 4]}
print(dict3["arr"])  # [1, 2, 3, 4]

# 요소 추가
dict1["birth"] = "0616"
print(dict1)

dict2[2] = ["Hello Spring", "Hello JSP"]
# {0: 'Hello Python', 1: 'Hello Java', 2: ['Hello Spring', 'Hello JSP']}
print(dict2)

dict3["rank"] = (16, 17, 18)
print(dict3)

# 각 숫자가 몇 개씩 나오는지 구 한 후 딕셔너리 생성
# {1:3, 2:4, 6:1......}
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]

# 비어 있는 dict 생성
counter = {}
# counter[1]=3
for number in numbers:
    # {1: 3, 2: 4, 6: 1, 8: 2, 4: 3, 3: 3, 9: 3, 5: 2, 7: 2} 키 밸류값으로 만들어줌
    counter[number] = numbers.count(number)

print(counter)

# 요소 삭제
del dict1["birth"]
print(dict1)

# 함수
# get(키값)
print(dict1.get("name"))
# None  dict1["addr"]이렇게 하면 키에러가 나서 안전하게 코딩하려면 get을 쓴다
print(dict1.get("addr"))

# keys() : 딕셔너리 내 키 값 가져오기 - 확인할 때 쓰는 개념
print(dict1.keys())  # dict_keys(['name', 'age'])

# values()
print(dict1.values())   # dict_values(['park', '12'])

# items() : key, value 쌍으로 가져오기
print(dict1.items())    # dict_items([('name', 'park'), ('age', '12')])

# in() : 키가 포함되어 있는가?
print("name" in dict1)  # True
print(4 in dict2)  # False

my_info = {"name": "kim", "age": 35, "city": "seoul"}

for k in my_info.keys():
    print(k)    # name /age /city

for v in my_info.values():
    print(v)   # kim /35 /seoul

for k, v in my_info.items():
    print(k, v)  # name kim / age 35 /city seoul

info = {v for v in my_info.values()}
print(info)  # {'seoul', 35, 'kim'}

info = [v for v in my_info.values()]
print(info)  # ['kim', 35, 'seoul']

info = {(k, v) for k, v in my_info.items()}
print(info)  # {('name', 'kim'), ('city', 'seoul'), ('age', 35)} 안에는 튜플 구조

# 딕셔너리 생성하기
# "A" = 90, "B" = 80, "C" = 70 등급을 딕셔너리로 생성하기
dict1 = {"A": 90, "B": 80, "C": 70}

# B 키에 해당하는 값 출력하기
print(dict1["B"])
print(dict1.get("B"))   # B 값이 없어서 오류가 날수도있기때문에

# B 키 값을 삭제한 후 딕셔너리 출력하기
del dict1["B"]
print(dict1)


# 성인 : 10000, 청소년 : 7000, 아동 : 3000 데이터를 딕셔너리 생성
dict2 = {"성인": 10000, "청소년": 7000, "아동": 3000}

# 위 딕셔너리에 소아 : 0 항목 추가
dict2["소아"] = 0
print(dict2)

# 키 값만 출력하기
# for k in dict2.keys():
#     print(k)
print(dict2.keys())  # dict_keys(['성인', '청소년', '아동', '소아'])

# value 값만 출력하기
# for v in dict2.values():
#     print(v)
print(dict2.values())   # dict_values([10000, 7000, 3000, 0])

# list(), tuple()
print(list(dict2.keys()))   # 리스트로 돌려받을거야 ['성인', '청소년', '아동', '소아']
print(tuple(dict2.keys()))  # 튜플로 돌려받을거야 ('성인', '청소년', '아동', '소아')

print(type(dict1))  # <class 'dict'> - 중괄호를 쓰면 딕셔너리 구조로 인식

# key, value 전부 지우기
dict1.clear()
print(dict1)    # {} - 안에 내용이 지워짐
