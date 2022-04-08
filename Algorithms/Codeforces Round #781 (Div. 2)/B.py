'''
source: https://codeforces.com/contest/1665/problem/B
AC
'''

import math

t = int(input())

for i in range(t):
    n = int(input())
    a = input().split()
    dic = {}
    for item in a:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    m = max(dic.values())
    ops = math.ceil(math.log2(n/m)) + n - m
    print(ops)