from collections import Counter
a = input()
a = list(a)

def most_frequent(data):
    c = Counter(data).most_common()
    if int(c[0][1]) == int(c[1][1]):
        print("?")
    else:
        print(c[0][0].upper())
most_frequent(a)