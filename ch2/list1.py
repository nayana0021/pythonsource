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

# sort() : 원본을 순서대로 정렬 - 원래의 요소를 바꿈
print("정렬 전 ", numbers)
numbers.sort()  # 오름차순 정렬
print("정렬 후 ", numbers)  # [5, 9, 32, 65, 72, 99, 103, 273, 800]

alpha = ["a","z","c","b","f"]
alpha.sort()
print("정렬 후 ", alpha)    # ['a', 'b', 'c', 'f', 'z']

alpha = ["a","z","A","b","D","f"]
alpha.sort()
print("정렬 후 ", alpha)    # ['A', 'D', 'a', 'b', 'f', 'z'] 아스키코드 순서 - 대문자부터 출력됨

han = ["고양이", "강아지","원숭이","호랑이"]
han.sort()
print("정렬 후 ", han)  # ['강아지', '고양이', '원숭이', '호랑이']

numbers = [273,103,5,32,65,9,72,800,99]
numbers.sort(reverse=True)  # 내림차순 정렬
print("정렬 후 ", numbers)  # [800, 273, 103, 99, 72, 65, 32, 9, 5]

# reverse() : 리스트 뒤집기
han.reverse()   # ['강아지', '고양이', '원숭이', '호랑이']
print("reverse 후 ", han)   # '호랑이', '원숭이', '고양이', '강아지']

# index(찾고자하는 요소) : 요소가 존재하면 위치를 반환

print(han[0])   # 호랑이
print(han.index("호랑이"))  # 0
# print(han.index("구름"))  # ValueError: '구름' is not in list - 인덱스의 특징 : 못 찾으면 value 에러

# insert(위치, 요소)
han.insert(1,"악어")
print("insert 후 ", han)    # insert 후  ['호랑이', '악어', '원숭이', '고양이', '강아지']

# remove(삭제할 요소) : 
# list = [1,3,3,5] ==> list.remove(3) : 첫번째 찾은 3 만 제거 - 요소 하나밖에 못 지움
han.remove("고양이")
print("remove 후 ", han)    # remove 후  ['호랑이', '악어', '원숭이', '강아지']

# pop() : 리스트 요소 중 마지막 요소 꺼내기 - 제거의 의미.. 인덱스 지정이 가능하나 기본적으로 마지막요소 제거
item = han.pop()
print("pop 대상 ",item) # pop 한 것 확인 가능하다 **

han.pop()
print("pop 후 ", han)   # pop 후  ['호랑이', '악어', '원숭이'] 
han.pop(1)
print("pop 후 ", han)   # pop 후  ['호랑이', '원숭이'] 위치를 지정해주면 그 위치에 해당하는 요소 꺼내줌

# count()
a = [1,2,3,1]
print("리스트에 포함된 1의 개수 ",a.count(1))   # 리스트에 포함된 1의 개수  2

# clear() : 리스트 요소 모두 삭제
a.clear()
print("clear 후 ",a)    # clear 후  []

# 리스트 안에 요소가 비어 있는 경우 False 임
list9 = []
if list9:
    print("True")
else:
    print("False")  # 결과 False 

str = ""    # 문자열도 내용이 없는 경우 False
if str:
    print("True")
else:
    print("False")  # # 결과 False 

# in
print("p" in "python")  # True

fruits = ["사과","딸기","배","자몽"]
print("사과" in fruits) # True
print("메론" not in fruits) # True

# 리스트 출력
for fruit in fruits:
    print(fruit)

print()

# enumerate() : index 부여 
for fruit in enumerate(fruits):
    print(fruit)
# (0, '사과') - 튜플 구조임
# (1, '딸기')
# (2, '배')
# (3, '자몽')

print()

for idx, fruit in enumerate(fruits): # 아주 많이 쓰는 형태
    print(idx,fruit)
# 0 사과
# 1 딸기
# 2 배
# 3 자몽
print()
for idx, fruit in enumerate(fruits, start=1): # 인덱스를 줄 수도 있음 기본값은 1
    print(idx,fruit)

# 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# 70, 60, 55, 75, 95, 90, 80, 85, 100, 88
# 중간고사 점수를 리스트로 생성하고, A 학급의 평균을 구하기
a_class = [70, 60, 55, 75, 95, 90, 80, 85, 100, 88]

total = 0
for num in a_class:
    total += num
print("A 학급 평균 : %.2f" % (total / len(a_class)))

# sum() 이용
print("A 학급 평균 : %.2f" % (sum(a_class) / len(a_class)))

# 1 ~ 20 리스트 생성 : [1,2,3,4....]

list1 = list(range(1,21))   # 리스트 만듬 1 ~ 20까지
print(list1)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


list3 = []
for x in range(1,101):
    list3.append(x)
print(list3)

# comprehension     향상된 for문 같은 개념..
list3 = [x for x in range(1,101)]   # 1 ~ 100 까지
print(list3)

list4 = ["갑","을","병","정","경"]
# 정을 제외하고 출력
for x in list4:
    if x != "정":
        print(x)
    
# 
list5 = [x for x in list4 if x != "정"]
print(list5)    # ['갑', '을', '병', '경']

# 1~100 숫자 중에서 홀수만 리스트로 생성
list6 = list(range(1,101,2))
print(list6)

list7 = []
for i in range(1,101,2):
    list7.append(i)
print(list7)


list8 = [x for x in range(1,101,2)]
print(list8)

# 아래의 리스트에서 소문자만 추출해서 새로운 리스트로 생성 후 출력
list9 = ["A","b","c","D","e","F","G","h"]

list10 = []
for x in list9:
    if x.islower():
        list10.append(x)

print(list10)

# list comprehension
list10 = [x for x in list9 if x.islower()]
print(list10)

# [1,2,3,4] ==> [2,4,6,8]
print([ x * 2 for x in [1,2,3,4]])

# [0,1,2,3,4] ==> [0,1,4,9,16]
print([ x * x for x in [0,1,2,3,4]])

# [1, 2, 3]
# [[1, 2, 3], [2, 3, 4,], [3, 4, 5]]
list1 = [1,2,3]

list2 = []

for x in list1:
    list2.append([x,x+1,x+2])
    
print(list2)    # [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

print([[x,x+1,x+2]for x in list1])