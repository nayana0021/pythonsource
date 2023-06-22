class UserInfo:
    #     """
    #     Author : Hong
    #     Date : 2023.06.22
    #     Description : 클래스 작성법 - 인자 있는 생성자(오버로딩 유사한 개념)
    #     """

    def __init__(self,name,age,email=None) -> None: # init 은 하나만 만들수있기 때문에 기본값을 줌으로 오버로딩과 유사한 개념으로 생성자를 사용한다
        self.name = name
        self.age = age
        self.email = email

    def user_info(self):
        return "name : {}, age : {}, email : {}".format(self.name, self.age, self.email)
    
# 두 명의 객체 생성
user1 = UserInfo("박재범",37,"jay87@gmail.com")
user2 = UserInfo("윤성빈",30)

# user_info 호출
print(user1.user_info())
print(user2.user_info())


