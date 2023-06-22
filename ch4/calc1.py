class Calc:
    """
    생성자 작성 - 멤버 변수 result 
    메소드 작성 - adder(숫자) result += 숫자, result 리턴
    """
    def __init__(self,result) -> None:
        self.result = result

    def adder(self, num):
        self.result += num
        return self.result
