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


class UserInfo:
    #     """
    #     Author : Hong
    #     Date : 2023.06.21
    #     Description : 클래스 작성법 - 인자 있는 생성자
    #     """

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def user_info(self):
        return "name : {}, age : {}".format(self.name, self.age)
    
# 두 명의 객체 생성
user1 = UserInfo("박재범",37)
user2 = UserInfo("윤성빈",30)

# user_info 호출
print(user1.user_info())
print(user2.user_info())


