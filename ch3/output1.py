# 파일 입출력

# 파일 입출력
# f = open("파일경로","모드")
# 파일 관련 작업
# .......
# 종료
# f.close()

# resource 폴더에 test1.txt 파일 생성
# w : write 기존 내용 다 지우고 새로 작성해줌
# f = open("resource/test1.txt", "w")
# f.write("Hello Python")
# f.close()

# close() 명시하지 않아도 됨 - with 구문 사용시 열고, 닫고를 자동으로 처리해준다
with open("resource/test1/txt","w") as f:
    f.write("Hello Python")


# f = open("resource/test1.txt", "w", encoding="utf-8")   # 한글이 들어가는 경우 인코딩 해줘야 함
# f.write("안녕하세요\n반갑습니다")
# f.close()

# 1~10 파일에 작성
# f = open("resource/test1.txt", "w", encoding="utf-8")
# for i in range(1,11):
#     data = "%d 번\n" % i
#     f.write(data)
# f.close()

# a (append) 앞에 내용이 있다면 뒤에 덧붙여지는 개념
# 안녕하세요
# f = open("resource/test1.txt", "a", encoding="utf-8")
# for i in range(1,11):
#     data = "안녕하세요\n"
#     f.write(data)
# f.close()

# list1 = ["홍길동","김길동","최길동"]
# # test2.txt 에 리스트 안의 문자 작성
# f = open("resource/test2.txt", "w", encoding="utf-8")
# for name in list1:
#     f.write(name+"\n")
# f.close()

# list1 = ["홍길동\n","김길동\n","최길동\n"]
# # test2.txt 에 리스트 안의 문자 작성
# f = open("resource/test2.txt", "w", encoding="utf-8")
# f.writelines(list1) # 엔터가 요소에 들어가있기 때문에 라인별로 써달라고 할수있음
# # f.write(list1) 에러남 리스트 요소에 엔터가 들어가있으면 안됨
# f.close()

# write append 둘 중에 하나 골라서 사용하면 됨~

# dict1 = {"name":"홍길동","age":25,"addr":"서울"}
# # test3.txt
# # name : 홍길동
# # age : 25
# # addr : 서울
# f = open("resource/test3.txt", "w", encoding="utf-8")
# for k,v in dict1.items():
#     f.write("{} : {}\n".format(k,v))
# f.close()

import random

hanguls = list("가나다라마바사아자차카타파하")
# print(hanguls)
# print(random.choice(hanguls))
f = open("resource/info.txt","w",encoding="utf-8")
for i in range(1000):
    name = random.choice(hanguls) + random.choice(hanguls)
    weight = random.randrange(40,100)
    height = random.randrange(140,190)
    f.write("{}, {}, {}\n".format(name,weight,height))
f.close()
