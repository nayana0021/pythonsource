# 파이썬 자료형
# 2. 리스트  (자바 배열, List 같은 개념)           (*엄청중요* 파이썬에서는 리스트,딕셔너리 굉장히 중요)
# []

# 리스트 생성
list1 = []  # 대괄호를 열어 생성한다
list2 = ['a', 1, 3.15, True]
print(list1)
print(list2)
list3 = ['a', 1, 3.15, True, ["b", 35, 45]]
print(list3)

# 리스트 인덱싱
print(list2[0])
print(list2[2])
print(list2[-1])    # 마지막에 있는 것 가져옴
print(list3[-1])
print(list3[-1][1])  # 2차원 배열의 개념으로 가져옴 - 마지막의 것 중 인덱스1의 값

print()

# 리스트 슬라이싱
print(list2[0:2])
print(list3[:-1])
print(list3[4:])    # [['b', 35, 45]]
print(list3[4]) # ['b', 35, 45]
print(list3[4][:2]) # ['b', 35]

list4 = [1,2,["a","b", ["Life", "is"]]]
# is 문자열
print(list4[2][2][1])
print(list4[-1][-1][-1])

# + : 연결
a = [1,2,3]
b = [4,5,6]
print(a+b)  # [1, 2, 3, 4, 5, 6]
print(a[0]+b[1]) # 인덱싱으로 더하기 하면 산술 더하기가 됨

# * : 반복
print(a * 3)

# 리스트 특정 요소 수정
a[1] = 7
print(a)    # [1, 7, 3]

a[2] = "Life"
print(a)

b[1:2] = [10,11]    # 범위를 줌 [4, 10, 11, 6] 범위를 줘야 하나의 요소로 들어감
print(b)

b[1] = [15,16,17]   # [4, [15, 16, 17], 11, 6] 요소로 안 들어가고 리스트로 들어감
print(b)

# 리스트 요소 삭제
del b[1]
print(b)

b[0:1] = []
print(b)

numbers = [273,103,5,32,65,9,72,800,99]
for number in numbers:
    if number >= 100:
        print("100 이상의 수 ", number)

print()

# 273은 3 자릿수입니다.
# 103은 3 자릿수입니다.
# 5는 1 자릿수입니다.

for number in numbers:
    print("{}는 {} 자릿수입니다".format(number,len(str(number))))

# () : 튜플
list4 = list([1,2,3]) # 그냥 ()로만 감싸면 튜플로 인식하기 때문에 에러가 남
print(list4)

# 리스트 함수
# append() : 리스트 뒤에 요소 추가
list4.append(5)
print(list4)
# list4.append(6,7,8)
# print(list4)    # TypeError: list.append() takes exactly one argument (3 given)
list4.append([6,7,8])   # [1, 2, 3, 5, [6, 7, 8]]
print(list4)