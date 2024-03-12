# T = int(input())

# Aarr = []
# Barr = []
# result = []

# for i in range(T):
#     A,B = map(int, input().split())
#     for j in range(1, A+1):
#         if A % j == 0:
#             Aarr.append(j)
#     for k in range(1, B+1):
#         if B % k == 0:
#             Barr.append(k)

# length = len(Aarr)

# for i in range(0, length):
#     for j in range(0, length):
#         if i != j:
#             result.append(Aarr[i]+Aarr[j])

# exist = False
# for i in result:
#     for j in Barr:
#         if i == j:
#             exist = True
#             break
# if exist:
#     print("yes")
# else:
#     print("no")

T = int(input())

for i in range(T):
    A,B = map(int, input().split())
    print("yes")