import math

class Test:
    def solv(self, r):
        return math.pi * (r**2)
    
    def add(self, a, b):
        return a + b

if __name__ == "__main__":
    test = Test()
    print(test.solv(2))
    print(test.add(6,7))
