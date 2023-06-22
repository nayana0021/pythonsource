# class UserInfo:
#     """
#     Author : Hong
#     Date : 2023.06.21
#     Description : 클래스 작성법
#     """

#     def user_info(self):
#         print("메소드 실행")

# user1 = UserInfo()
# print(user1)    # <__main__.UserInfo object at 0x102460dd0> UserInfo 객체의 주소
# user1.user_info()   # 메소드 호출방법 자바랑 같음


# class UserInfo:
#     #     """
#     #     Author : Hong
#     #     Date : 2023.06.21
#     #     Description : 클래스 작성법 - 인자 있는 생성자
#     #     """

#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age

#     def user_info(self):
#         return "name : {}, age : {}".format(self.name, self.age)
    
# # 두 명의 객체 생성
# user1 = UserInfo("박재범",37)
# user2 = UserInfo("윤성빈",30)

# # user_info 호출
# print(user1.user_info())
# print(user2.user_info())


class UserInfo:
    #     """
    #     Author : Hong
    #     Date : 2023.06.22
    #     Description : 클래스 작성법 - 클래스 변수
    #     """

    # 클래스 변수
    user_count = 0

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

        UserInfo.user_count += 1    #생성자를 사용해서 user가 만들어질때 +1이 된다

    def user_info(self):
        return "name : {}, age : {}".format(self.name, self.age)
    
    def __del__(self):
        UserInfo.user_count -= 1

    @classmethod    # 어노테이션을 붙여서 클래스 메소드인 것을 명확하게 해줌
    def function1(cls): # 인자로 cls 를 쓴다 - 클래스변수에 접근할 수 있다
        """
        클래스 메소드 : self 를 붙이지 않으면
        """
        print("function1 호출",cls.user_count)

    def function2(self):
        print("function2 호출")

user1 = UserInfo("홍길동",30)
user2 = UserInfo("김유신",20)

# 메소드 호출
print(user1.user_info())
print(user2.user_info())

# 클래스 변수 확인
print("생성된 user {} 명".format(UserInfo.user_count))
print("생성된 user {} 명".format(user1.user_count))

# user 삭제
del user1   # __del__ 메소드 자동으로 실행
print("생성된 user {} 명".format(UserInfo.user_count))

# function1(), function2() 호출
# user2.function1()   # TypeError: UserInfo.function1() takes 0 positional arguments but 1 was given : self 를 안 넣었음
UserInfo.function1()    
user2.function2()   #  : self 넣었음

