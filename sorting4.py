import random

def CreateRandomList(size):
    a = []
    s = [i for i in range(size)]
    while len(a) < size:
        r = random.randrange(0, len(s))
        a.append(s[r])
        s[r] = s[-1]
        s.pop()
    return a

print(CreateRandomList(10))