'''
source: https://codeforces.com/contest/1665/problem/C
WA
'''
from math import ceil, floor

def binary_search(c1, c2):
    m = (c1 + c2 + 1) // 2
    while abs(c1 - c2) > 1:
        m = (c1 + c2 + 1) // 2
        if ok(m):
            c2 = m
        else:
            c1 = m
    m = max(m - 2, 0)
    while not ok(m):
        m += 1
    return m

def ok(m):
    c = 0
    for i in range(len(l)):
        c += max(0, l[i] - m - i - 1)
    return True if c <= m else False


t = int(input())

res = []

for _ in range(t):
    n = int(input())
    a = input().split()
    a = [int(x) for x in a] + [0]
    dic = {}
    for item in a:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    l = list(dic.values())
    l = sorted(l, reverse=True)
    # for idx in range(len(l)):
    #     round_cnt += floor((l[idx] - round_cnt)/2) if l[idx] - (round_cnt - 1) > 0 else 0
    # for idx in range(len(l)):
    #     round_cnt += 1 if (l[idx] - round_cnt > 0) else 0
    res.append(binary_search(0, n) + len(l))

for item in res:
    print(item)