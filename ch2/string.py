# 파이썬 자료형
# 1. 문자열
# "", '', """ """, ''' ''',

#  + : 결합
print("Python " + "is fun")

# * : 복제(곱하기 개념)
print("Python" * 3)  # 3번 반복

print("*" * 50)
print("내 프로그램")
print("*" * 50)

# 인덱싱 : 문자열은 인덱스 값을 가지고 있음(0부터 시작)     (*엄청 중요한 개념*)

str1 = "Life is too short"
print(str1[3])

# 슬라이싱 [시작위치 : 끝위치] => 끝 위치 포함하지 않음     (*엄청 중요한 개념*)
print("str1[2:6]", str1[2:6])
print("str1[:6]", str1[:6])  # 시작위치 지정하지 않은 경우 0
print("str1[:]", str1[:])  # 위치 지정하지 않은 경우 0 ~ 끝까지
print("str1[:-4]", str1[:-4])  # - 값은 오른쪽 끝에서부터 위치를 잡는 경우 -1부터 시작

# len() : 길이 함수
print("str1 길이", len(str1))

str2 = "20230615Sunny"
# 년도, 날씨를 구별해서 변수에 담기
date = str2[:8]
weather = str2[8:]
print(date, weather)

# date 변수에 담긴 값을 년-월-일
year = str2[:4]
month = str2[4:6]
day = str2[6:8]
print(year, month, day, sep="-")  # 구분자 - 로 줌

# 주민등록번호 001205-3234567
# 남자(1,3) / 여자(2,4) 출력
str3 = "001205-3234567"
no = str3[7]

# no 가 1 or 3 남, 2 or 4 여
if no == "1" or no == "3":
    print("남")
elif no == "2" or no == "4":
    print("여")

if int(no) % 2 == 1:
    print("남")
else:
    print("여")

str1 = "대한민국"
for s in str1:
    print(s)

# 대$한$민$국
for s in str1:
    print(s+"$", end="")

print()

# 입력받은 숫자만큼 하트 출력
# 54321
# ❤️❤️❤️❤️❤️
# ❤️❤️❤️❤️
# ❤️❤️❤️
# ❤️❤️
# ❤️
# str1 = (input("숫자 입력 : "))  # 54321
# for i in range(len(str1)):
#     for j in range(int(str1[i])):
#         print("❤️", end="")
#     print()

# 문자열 관련 함수
# count()
print("\n문자열 관련 함수")
str1 = "hobby"
print("원본 문자열에 포함된 특정 문자 개수 ", str1.count("b"))  # b 가 몇개 들어있는지 알려줌

str1 = "python is best choice"

# find() : 없는 경우 -1 반환
print("찾는 문자의 시작 위치 반환", str1.find("b"))
print("찾는 문자의 시작 위치 반환", str1.find("k"))
print("찾는 문자의 시작 위치 반환", str1.find("i", 10))  # 시작위치 10번 다음에 위치한 i의 위치값을 찾아줌
print("찾는 문자의 시작 위치 반환", str1.rfind("i"))

print()

# index() : 못 찾는 경우 ValueError 발생       ValueError: substring not found
print("찾는 문자의 시작 위치 반환", str1.index("b"))
# print("찾는 문자의 시작 위치 반환",str1.index("k"))

# startswith() / endswith() : 특정 문자열로 시작하는지 / 끝나는지 - 자바랑 같은 개념
print(str1.startswith("p"))
print(str1.endswith("p"))

# join() : 주어진 문자열 중간에 삽입 - 자주 쓴다
str2 = ","
print("문자열 삽입", str2.join("abcde"))

# upper() / lower()
print("대문자", "abcdef".upper())
print("소문자", "ABCDEF".lower())

# swapcase() : 대문자 -> 소문자, 소문자 -> 대문자
str1 = "Python is Easy"
print(str1.swapcase())

print("abc" == "ABC")  # 파이썬 대소문자 구별한다

# 공백 제거 : 왼쪽, 오른쪽, 양쪽 나눠서 제거 가능
str1 = "        hi"
print(str1)
print("왼쪽 공백 제거", str1.lstrip())

str1 = "hi      "
print(str1)
print("오른쪽 공백 제거", str1.rstrip())

str1 = "        hi      "
print(str1)
print("양쪽 공백 제거", str1.strip())

# replace()
str1 = "Life is too short"
print("특정 문자열 변경", str1.replace("Life", "Your leg"))

# split() => [](리스트)로 반환 - 공백을 기준으로 나눔
print(str1.split())     # ['Life', 'is', 'too', 'short']

a = "abcd"
print(a.split())  # ['abcd']

a = "a:b:c:d"
print(a.split(":"))     # : 을 기준으로 잘라줘

a = "하나\n둘\n셋"
print(a.splitlines())  # ['하나', '둘', '셋'] : 엔터를 기준으로 나눔
print(a.split())  # ['하나', '둘', '셋'] : 공백의 개념이 들어있으면 나눔

# 문자열 구성 파악 - isdigit(), isalpha(), isalnum(), islower() : 소문자니?, isupper() : 대문자니?
print("12345".isdigit())    # 숫자로만 구성되어 있느냐?
print("12345".isalpha())    # 알파벳으로만 구성되어 있느냐?
print("12345".isalnum())    # 알파벳 or 숫자로 구성되어 있느냐?

# 사이트별 비밀번호를 만들어 주는 프로그램
# http://www.naver.com

# 규칙 1 : http://www. 제외 ==> naver.com
# 규칙 2 : 처음 나오는 . 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자개수 + 글자 내 e 개수 + ! 구성
# 완성된 비밀번호 : nav51!

# str = "http://www.naver.com"
# str1 = str[str.index(".")+1:-4]
# str2 = str1[:3]
# print(len(str2))

url = "http://www.naver.com"

print(url)

# 규칙 1 적용
# url = url[12:]
url = url.replace("http://www.", "")

# 규칙 2 적용
# idx = url.find(".")
# url = url[:idx]

url = url[:url.find(".")]

# 규칙 3 적용
# TypeError: can only concatenate str (not "int") to str int와 str 연결 안됨 str 함수 써야함
password = url[:3] + str(len(url)) + str(url.count("e")) + "!"

print(password)
