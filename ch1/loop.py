# 반복문
# while, for

# 1~10 출력

i = 1
while i < 11:
    print(i, end=' ')
    i += 1

print()

# 짝수만 출력 1~100
i = 2
while i < 101:
    print(i, end=' ')
    i += 2
    
print()

# i = i+i == i += 1 == i++(python 불가)
# 3단 출력
i = 1
while i < 10:
    print("{} * {} = {}".format(3, i, 3*i))
    i += 1

# in : 포함 - 연산기호
print("in 기호")
print("y" in "python")
print("k" in "python")
print("k" not in "python")



# range(시작값,종료값(필수),증감값) : 범위 지정 - 시작값,증감값 옵션인데 증감값 옵션 안 주면 1씩 증가
print(range(5))     # range(0, 5) => 0~4 끝나는 값음 포함하지 않음 (0에서:시작값 시작해서 5까지:끝값 범위를 가짐)
print(list(range(1,5))) # [1, 2, 3, 4] 
print(list(range(0,10,2)))  # [0, 2, 4, 6, 8]

# for 
for i in range(10):
    print(i)

for i in range(1,101):
    print(i, end=" ")