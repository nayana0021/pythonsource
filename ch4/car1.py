# class Car:
#     color = ""
#     speed = 0

#     def upSpeed(self, value):
#         self.speed += value

#     def downSpeed(self, value):
#         self.speed -= value

class Car:
    def __init__(self) -> None:
        self.color = "" # 멤버변수로 만듬
        self.speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value


# Red, Blue, Yellow 자동차 객체 생성
car1 = Car()
car1.color = "Red"

car2 = Car()
car2.color = "Blue"

car3 = Car()
car3.color = "Yellow"

# 첫번째 자동차 색상은 Red 이며, 현재 속도는 50km 입니다
car1.upSpeed(100)
print("첫번째 자동차 색상은 {} 이며, 현재 속도는 {}km 입니다".format(car1.color,car1.speed))

car2.upSpeed(60)
car2.downSpeed(20)
print("두번째 자동차 색상은 {} 이며, 현재 속도는 {}km 입니다".format(car2.color,car2.speed))

car3.upSpeed(150)
car3.downSpeed(50)
print("세번째 자동차 색상은 {} 이며, 현재 속도는 {}km 입니다".format(car3.color,car3.speed))
