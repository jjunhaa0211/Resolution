# 문제
# 대한고등학교에 재학 중인 민국이와 만세는 4과목(정보, 수학, 과학, 영어)에 대한 시험을 봤다. 민국이와 만세가 본 4과목의 점수를 입력하면, 민국이의 총점 S와 만세의 총점 T 중에서 큰 점수를 출력하는 프로그램을 작성하시오. 단, 서로 동점일 때는 민국이의 총점 S를 출력한다.

# 입력
# 입력은 2줄로 이루어져 있다.

# 1번째 줄에는 순서대로 민국이의 정보, 수학, 과학, 영어 점수(정수형)가 있으며, 공백으로 구분되어 있다.

# 2번째 줄에는 1번째 줄과 마찬가지로 순서대로 만세의 정보, 수학, 과학, 영어 점수(정수형)가 있고, 공백으로 구분되어 있다.

n1,n2,n3,n4 = map(int, input().split())
b1,b2,b3,b4 = map(int, input().split())

S = n1+n2+n3+n4
T = b1+b2+b3+b4

if S > T:
    print(S)
elif S == T:
    print(S)
else:
    print(T)