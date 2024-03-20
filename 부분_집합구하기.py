# 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램을 작성하세요

# 입력
# 첫번째 줄에 자연수 N(1<=N<=10)이 주어집니다.

# 출력
# 첫번째 줄부터 각 줄에 하나씩 부분집합을 아래와 출력예제 순으로 출력하시고 단 공집합은 출력하지 않습ㄴ디ㅏ.
n1 = int(input())
arr = []
brr = []

for i in range(1, n1+1):
    arr.append(i)
    brr.append(0)

def f(k, n):
    if n==k:
        for i in range(n):
            if brr[i] == 1:
                print(arr[i], end=' ')
        print()
    else:
        brr[k]=1
        f(k+1, n)
        brr[k]=0
        f(k+1, n)

f(0, n1)