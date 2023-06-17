# 주차장 프로그램

# 메뉴 제공
# [1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 :

# 주차장 리스트 생성
parking_lot = []
# 주차위치, 자동차명 변수 생성
top, car_name = 0, "A"

# print(ord("A")) # 65 ord() : 아스키 코드 값으로 반환
# print(chr(65))  # chr() : 숫자를 문자로 반환(아스키)

while True :
    no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 :"))

    if no <= 3:
        if no == 1:
            # print("{} 자동차 들어감. 주차장 상태 ==> ['{}']".format(car_name, car_name))
            # list.append(car_name)
            if top >= 5:
                print("주차장 꽉 찼음")
            else:
                parking_lot.append(car_name)
                print("{} 자동차 들어감. 주차장 상태 ==> {}".format(car_name, parking_lot))

                top += 1
                car_name = chr(ord(car_name) + 1)
        elif no == 2:
            if top > 0:
                out_car = parking_lot.pop()
                print("{} 자동차 나감. 주차장 상태 ==> {}".format(out_car, parking_lot))

                top -= 1
                car_name = chr(ord(car_name) - 1)
            else:
                print("빠져나갈 자동차 없음")
        else:
            print("프로그램 종료")
            break
    else:
        print("번호를 확인해 주세요")

# pass : 코드 완성하기 전 문법 적인 오류를 넘어가게 해준다 - 내용을 나중에 넣을 경우

