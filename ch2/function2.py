# 람다 함수
# 단일문으로 표현되는 익명함수
# 코드 상에서 한번만 사용이 되는 상황일때 

# def square(x):
#     return x * x

# print(square(5))

square = lambda x: x * x
print(square)   # <function <lambda> at 0x102874680>
print(square(5))

add = lambda a,b: a + b
print(add(5,6))

# 문자열 길이 리턴 함수
def str_len(s):
    return len(s)

strings = ["bob", "charles", "alexander", "teddy"]
strings.sort(key=str_len)   # 정렬 기준 부여 - 문자열 길이 기준
print(strings)  # ['bob', 'teddy', 'charles', 'alenxander'] 

# 3줄로 더 간단해짐
strings.sort(key=lambda s:len(s))
print(strings)

# filter(함수, 리스트)

# 짝수 리스트 생성
even_list=[]

def even(arr):
    for n in arr:
        if n % 2 == 0:
            even_list.append(n)
list1 = [1,2,3,6,8,9,10,12]
even(list1)
print(even_list)

# List comprehenshion
even_list2 = [n for n in list1 if n % 2 == 0]
print(even_list2)

# lambda + filter       filter는 true 인 것만 통과시킴
def even2(n):
    return n % 2 == 0
print(list(filter(even2, list1)))   # [2, 6, 8, 10, 12]

print(list(filter(lambda n: n % 2 == 0, list1)))