# Уникальных сочетаний символов строки длиной n = n!
# У строки длиной 3 = 6 (1*2*3)
# 3 symbols  2 1 0


import itertools

def permutations(s):
    perm = itertools.permutations(list(s))
    result = []
    for i in perm:
        result.append(''.join(i))
    return set(result)

print(permutations('abc'))