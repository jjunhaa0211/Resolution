numbers = [int(input()) for _ in range(3)]

result = list(str(numbers[0] * numbers[1] * numbers[2]))

for i in range(10):
    print(result.count(str(i)))