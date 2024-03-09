n = int(input())
result = [sum(map(int, input().split())) for _ in range(n)]
for r in result:
    print(r)