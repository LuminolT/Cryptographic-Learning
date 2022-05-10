m = {-1: 0b0000}

m[0] = 0b0001
m[1] = 0b0010
m[2] = 0b0100
m[3] = 0b1000
m[4] = 0b1001
m[5] = 0b1011
m[6] = 0b1111
m[7] = 0b0111
m[8] = 0b1110
m[9] = 0b0101
m[10] = 0b1010
m[11] = 0b1101
m[12] = 0b0011
m[13] = 0b0110
m[14] = 0b1100


# arr = '3 12 5 9 6 10'
# arr = '7 11 13 14'

arr = '3 6 9 12'
arr = '9 6 12 3'
arr = '9 12 3 6'
arr = '5 10'

arr = '7 11 13 14'
# arr = '3 12 5 6 9 10'
# arr = '4 8 1 2'
l = arr.split()
l = [int(i) for i in l]

res = 0b0000

for i in range(len(l)):
    print(f'{i}: {bin(m[l[i]])}')
    res ^= m[l[i]]

print(f'result: {bin(res)}')
