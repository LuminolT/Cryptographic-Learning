t = int(input())

res = ""

for _ in range(t):
    n = int(input())
    formt = input().split('W')
    formt = [formt[i] for i in range (len(formt)) if len(formt[i]) > 0]
    # print(formt)
    flag = True
    for it in formt:
        init_char = it[0]
        if len(it) == 1:
            flag = False
            break
        tmp_flag = False
        for idx in range(len(it)):
            if it[idx] != init_char:
                tmp_flag = True
                break
        if tmp_flag is False:
            flag = False
            break
    if flag is True:
        res += "YES\n"
    else:
        res += "NO\n"
        
print(res)
    