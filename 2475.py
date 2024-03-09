a = map(int, input().split())

result = 0

for i in a:
    result = result + i ** 2
print(result%10)