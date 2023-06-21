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

# lambda map

def mul(x):
    return x**2

nums = [1,2,3,6,8,10,11,12,13,14,15]

# map(함수, 리스트)
print(list(map(mul, nums)))     # [1, 4, 9, 36, 64, 100, 121, 144, 169, 196, 225]

print(list(map(lambda x: x**2, nums)))  # 바로 정의해서 사용이 가능하다 - 람다 맵 함수랑 주로 쓰임

nums = list(range(1,11))    # 1~10 리스트 생성

# 3의 배수만 문자열로 변경한 리스트 반환 ==> str(3) ==> '3'
# [1, 2,'3', 4, 5, '6', 7..]

# 새로운 결과를 담을 빈 리스트 생성
nums_result = []

def str_check(nums):
    '''
    리스트 안의 요소가 3의 배수인 경우 문자로 변환
    '''
    for i in nums:
        if i % 3 == 0:
            nums_result.append(str(i))
        else:
            nums_result.append(i)

    return nums_result

print(str_check(nums))  # [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

# filter, map
def str_check2(i):  # map 에 대한 함수는 요소 하나에 대한 함수를 정의한다고 보면 됨
    if i % 3 == 0:
        return str(i)
    else:
        return i

print(list(map(str_check2, nums)))  # [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

print(list(map(lambda i:str(i) if i % 3 == 0 else i, nums))) 