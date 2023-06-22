class FourCal:
    """
    사칙연산 메소드를 가지고 있는 클래스 작성
    """

    def __init__(self,num1,num2) -> None:
        """
        두 개의 변수를 받아서 멤버 변수(num1, num2) 초기화
        """
        self.num1 = num1
        self.num2 = num2
        

    def add(self):
        """
        두 개의 멤버 변수 더하기 후 리턴
        """
        return self.num1 + self.num2
        

    def sub(self):
        """
        두 개의 멤버 변수 빼기 후 리턴
        """
        return self.num1 - self.num2
        

    def mul(self):
        """
        두 개의 멤버 변수 곱하기 후 리턴
        """
        return self.num1 * self.num2


    def div(self):
        """
        두 개의 멤버 변수 나누기 후 리턴
        """
        return self.num1 / self.num2
    
num1, num2 = 10,5
cal = FourCal(num1, num2)

print("{} + {} = {}".format(num1,num2,cal.add()))
print("{} - {} = {}".format(num1,num2,cal.sub()))
print("{} * {} = {}".format(num1,num2,cal.mul()))
print("{} / {} = {}".format(num1,num2,cal.div()))
