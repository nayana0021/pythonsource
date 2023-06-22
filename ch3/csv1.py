# csv 읽기
import csv  #python 에서 제공하는 csv 모듈

# with open("resource/sample1.csv", "r", encoding="ms949") as f:
#     content = csv.reader(f)
#     print(content)
#     print(dir(content))
#     print(type(content))

#     for c in content:
#         print(c)

    # next(content)   # 헤더명 제거
    # for c in content:
    #     print(c)

# with open("resource/sample2.csv", "r", encoding="ms949") as f:  
#     content = csv.reader(f, delimiter="|")

#     next(content)   # 헤더명 제거
#     for c in content:
#         print(c)


# with open("resource/sample2.csv", "r", encoding="ms949") as f:
#     content = csv.DictReader(f, delimiter="|")  #dict 구조

#     next(content)   # 헤더명 제거
#     for c in content:
#         print(c)
#         for k,v in c.items():
#             print(k,":",v)
#         print()

# sample3.csv 읽기
# with open("resource/sample3.csv", "r") as f:
#     content = csv.reader(f)
#     for row in content:
#         #print(c)
#         for i in row:
#             print(i, end=" ")
#         print()


# csv 쓰기
data = [[1,2,3],[4,5,6,],[7,8,9,],[10,11,12],[13,14,15]]

with open("resource/sample4.csv","w") as f: # newline="" 엔터 부분 제거하는 옵션
    wt = csv.writer(f)

    for v in data:
        wt.writerow(v)
    # wt.writerows(data)