res = 0b0000

while True:
    n = input()
    if n == '0':
        break
    res ^= int(n, 2)

print(bin(res))
