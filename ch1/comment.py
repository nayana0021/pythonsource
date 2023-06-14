# 주석
"""
여러 줄 주석 처리 (쌍따옴표)
"""

'''
여러 줄 주서 처리 (홑따옴표)
'''

# 화면출력 - print() / 변수타입 확인 - type() 
print("Hello Python!!!")
print("100")
print(21.9)
print(type(100))    # <class 'int'>
print(type("100"))  # <class 'str'>
print(type(100.15)) # <class 'float'>
print(type(True))   # <class 'bool'> 대문자임!! False도 대문자

# sep : 문자열 사이 구분자(기본값 spacebar) seperator
print('t','e','s','t')  # t e s t 사이띄기 해서 출력됨
print('t','e','s','t', sep='')  # test 사이띄기를 없앤것
print('t','e','s','t', sep='-') # t-e-s-t

# end : 기본값은 엔터, 
print("Welcome To", end=' ') # 끝나고 한 칸 띄워주고 밑에거 출력해줘(줄바꿈 안함)
print("the black prade")

# format : %s(문자열,정수,실수), %d(정수), %f(실수), %c(문자열 하나)   (%를 사용하려면 콤마가 아닌 %를 써줘야한다)
print("%d" % 100)   # 정수출력
print("%5d" % 100)  # 5자리 맞춰서 출력
print("%05d" % 100) # 5자리 맞춰서 출력(자릿수 없는 것은 0으로 채우기)
print()
print("%s" % "hi")
print("%5s" % "hi")
print()
print("%-8.2f" % 123.21)    #왼쪽정렬 (숫자는 기본적으로 오른쪽정렬) 전체8자리 소수점은 두자리까지
print("%8.2f" % 123.21)
print("%8.2f" % 123.213456)

# 변수 선언(타입 선언 안함 - 값에 따라 타입이 결정)
number = 3
print("I eat %d apples" % number)
print("I eat", number, "apples")
print("%d : %s" % (1,"홍길동")) # 여러개가 대입되는 경우는 괄호를 사용한다 - 사용 안하면 TypeError

print("I eat %s apples" % 2)
print("I eat %s apples" % 3.156)    # 소숫점, 자릿수 옵션을 주려면 %d, %f 사용
print("I eat %s apples" % "two")

# 98% %를 출력하려면 한 번 더 쓴다
#print("Error is %d%" % 98) # ValueError
print("Error is %d%%" % 98)

# format() 함수
print("\nformat 함수 : {}")
print("{} and {}".format("You","Me"))
print("I eat {} apples".format(3))
print("I eat {0} apples".format(3)) # 인덱스 사용 가능
print("{0} and {1} and {0}".format("You","Me"))
print("{var1} and {var2}".format(var1="You", var2="Me"))
print("{0} and {var2}".format("You", var2="Me")) # 혼합으로도 사용 가능(인덱스와 변수) 근데 순서 지켜서해야함

# 이스케이프 문자 : \n, \t
print("\n줄바꿈\n연습")
print("\\ 역슬래쉬")
print(r"\n \t \\ 그대로 출력") # 그 화면 그대로 출력 (r은 정규식과 관련이 있다)
print("글자가 '강조'되는 효과") # 문자 표현 시 "", ''허용
print('글자가 "강조"되는 효과') # 문자 표현 시 "", ''허용
