# 조건문
# if, if~else, if~elif~else
# {} 사용 안함, 탭 사용

if True:
    print("True")

a = 200
if a < 100:
    print("a는 100보다 작다")
print("조건문에서 하나의 블럭 개념은 들여쓰기로 구분")

# a 는 100보다 크고 200보다 작거나 같다
if 100 < a <= 200:   # 자바에서는 안되지만 파이썬에서는 됨      # a > 100 and a <= 200:
    print("a 는 100보다 크고 200보다 작거나 같다")

# 세 개의 변수 선언, 12,6,18 값 담기
# 가장 큰 수 찾기
a,b,c = 12, 6, 18

max = a
if max < b:
    max = b
if max < c :
    max = c
print("가장 큰 수 {}".format(max))

a = 55
if a < 100:
    print("a는 100보다 작다")
else:
    print("a는 100보다 작다")

# 숫자 입력받은 후 짝, 홀 구분하여 출력
# num1 = int(input("숫자 입력 : "))
# if num1 % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

import datetime

now = datetime.datetime.now()
print(now)  # 2023-06-14 11:51:13.672747

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))

# 오전/ 오후 출력
if now.hour < 12:
    print('오전')
else:
    print('오후')

# 삼항연산자 now.hour < 12 ? "오전" : "오후" (X) 이렇게는 못 쓰고 좀 다름 ↓
#   참일 때 실행 구문 if 조건 else 거짓일 때 실행구문

str = "안녕하세요" if True else "반갑습니다"
print(str)

# str1 = "오전" if now.hour < 12 else "오후"
# print(str1)

print('오전' if now.hour < 12 else '오후')

# 다중조건 if ~ elif ~ else
num = 90
if num >= 90:
    print("A 등급")
elif num >= 80:
    print("B 등급")
elif num >= 70:
    print("C 등급")
elif num >= 60:
    print("D 등급")
else:
    print("F 등급")

print()

# age, height 변수 선언, 27,180 값 담기
# 나이가 20세 이상
#       키가 170 이상이면 "A지망 지원 가능" 출력
#       키가 160 이상이면 "B지망 지원 가능" 출력
#       나머지 지원불가 출력
# 나이가 20세 미만 시 "20세 이상 지원 가능" 출력
age, height = 27, 180

if age > 20:
    if height >= 170:
        print("A지망 지원가능")
    elif height >= 160:
        print("B지망 지원가능")
    else:
        print("지원불가")
else:
    print("20세 이상 지원 가능")

# 계산기 : 두 개의 수 입력, 연산자(+,-,*,/,//,%,**) 입력
num1 = int(input("Num1 입력 : "))
opt = input("연산자 입력 : ")
num2 = int(input("Num2 입력 : "))

result = 0
if opt == "+":
    result = num1 + num2
elif opt == "-":
    result = num1 + num2
elif opt == "*":
    result = num1 + num2
elif opt == "/":
    result = num1 + num2
elif opt == "//":
    result = num1 + num2
elif opt == "%":
    result = num1 % num2
elif opt == "**":
    result = num1 ** num2

print("{} {} {} = {}".format(num1,opt,num2,result))
