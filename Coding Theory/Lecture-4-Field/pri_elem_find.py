modulus = 7

for i in range(1, modulus):
    print(f"{i}:", end=' ')
    tmp = i
    order = modulus
    for j in range(1, modulus):
        order = j if tmp == 1 and j < order else order 
        print(f"{tmp}, ", end='')
        tmp = tmp * i % modulus
    print(f' order = {order}')