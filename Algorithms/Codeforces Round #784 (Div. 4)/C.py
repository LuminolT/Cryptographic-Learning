t = int(input())

for _ in range(t):
    n = int(input())
    raw_list = input().split()
    raw_list = [int(raw_list[i]) for i in range(n)]
    if n == 2:
        print("YES")
        continue
    num_1 = raw_list[0] % 2
    num_2 = raw_list[1] % 2
    flag = False
    for i in range(0, n, 2):
        if raw_list[i] % 2 != num_1:
            print("NO")
            flag = True
            break
    if flag is True:
        continue
    for i in range(1, n, 2):
        if raw_list[i] % 2 != num_2:
            print("No")
            flag = True
            break
    if flag is True:
        continue
    print("YES")