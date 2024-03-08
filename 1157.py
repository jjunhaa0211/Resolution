from collections import Counter

def most_frequent(data):
    data = data.upper()
    c = Counter(data).most_common(2)
    if len(c) > 1 and c[0][1] == c[1][1]:
        return "?"
    else:
        return c[0][0]

word = input()
print(most_frequent(word))