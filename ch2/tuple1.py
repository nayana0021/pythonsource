# 파이썬 자료형
# 3. 튜플 (리스트와 거의 유사함)
#       ()사용 / 수정(삭제) 불가 - 값 변화 X / 읽기만 가능

t1 = 1,2,3
print(t1)   # (1, 2, 3)

# 원소 개수가 하나라면 반드시 , (콤마)가 필요함
t2 = (1,)   # 콤마가 없다면 변수 하나 선언한것임..
print(t2)

t3 = (1, 2, ("Life","is"))
print(t3)   # (1, 2, ('Life', 'is'))

# 요소 삭제
# del t1[0]   # TypeError: 'tuple' object doesn't support item deletion - 튜플은 삭제 안됨
# 요소 변경
# t1[0] = 5   # TypeError: 'tuple' object does not support item assignment - 튜플은 변경 안됨

# 인덱싱 / 슬라이싱
print(t1[0])    # 1
print(t1[0:2])  # (1, 2)

# 함수 리턴 값 ==> 여러 개의 값이 가능함 ==> 튜플로 리턴

# 튜플 ==> 리스트
print(list(t1)) # 튜플을 리스트로 바꿔주는 것 - list 함수 [1, 2, 3]

# 리스트 => 튜플
list1 = [5,6,7]
print(tuple(list1)) # (5, 6, 7)
