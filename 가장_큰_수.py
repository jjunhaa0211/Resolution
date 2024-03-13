# 선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다.
# 여러분이 현수를 도와주세요. (단, 숫자의 순서는 유지해야합니다.)
# 만약 5276823 이 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 숫자가 됩니다.

# 입력
# 첫째 줄에 숫자와 제가 해야할 자릿수의 개수가 주어진다

# 출력
# 가장 큰 수를 출력한다

# 스택을 사용하여야한다
# 먼저 들어온 수가 있다면 

n, m = map(int, input().split())

def result_number(n, m):
    n = list(str(n))
    stack = []
    for num in n:
        while m > 0 and stack and stack[-1] < num:
            stack.pop()
            m = m - 1
        stack.append(num)

    if m > 0:
        stack = stack[:-m]
    return ''.join(stack)


print(result_number(n, m))
