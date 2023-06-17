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
    counter[number]=numbers.count(number)   # {1: 3, 2: 4, 6: 1, 8: 2, 4: 3, 3: 3, 9: 3, 5: 2, 7: 2} 키 밸류값으로 만들어줌

print(counter)

# 요소 삭제
del dict1["birth"]
print(dict1)

# 함수
# get(키값)
print(dict1.get("name"))
print(dict1.get("addr"))    # None  dict1["addr"]이렇게 하면 키에러가 나서 안전하게 코딩하려면 get을 쓴다

