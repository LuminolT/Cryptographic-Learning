from collections import Counter


t = int(input())

res = ""

for _ in range(t):
    n = int(input())
    raw_list = input().split()
    raw_list = [int(raw_list[i]) for i in range(n)]
    ctr = Counter(raw_list)
    res += (str(ctr.most_common(1)[0][0] if ctr.most_common(1)[0][1] >= 3 else -1)) + '\n'
    
print(res)