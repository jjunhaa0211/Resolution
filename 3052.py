# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 줄여서 10개 받고 42로 나눈 나머지를 중 서로 다른 값의 개수를 세주는 거구낭
emptyList = []
n = [int(input()) % 42 for _ in range(10)]

for i in n:
    if i not in emptyList:
        emptyList.append(i)

print(len(emptyList))

