n = int(input())

for _ in range(n):
    cnt, word = map(str, input().split())
    for x in word:
        print(x*int(cnt), end='')
    print()

# int를 받고 몇번 돌려줄지를 결정한다
# cnt와 word를 받는다
# x를 cnt만큼 볼려준다