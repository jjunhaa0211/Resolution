bracket = input()
arr = []
stack = []
count = 0

for i in bracket:
    arr.append(str(i))

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')
    elif arr[i-1] == '(':
        stack.pop()
        count = count + len(stack)
    else:
        stack.pop()
        count = count + 1

print(count)