# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

n = int(input())

if n >= 90:
    print("A")
elif 80 <= n:
    print("B")
elif 70 <= n:
    print("C")
elif 60 <= n:
    print("D")
else:
    print("F")