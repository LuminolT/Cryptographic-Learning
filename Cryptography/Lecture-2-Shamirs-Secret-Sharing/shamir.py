import random
import math
import utils
from decimal import Decimal
from Crypto.Util.number import bytes_to_long, long_to_bytes


def enc(secret, min_num, share_num, prime):
    """
    :param s: 原始秘密
    :param min_num: 最小秘密数量
    :param share_num: 共享秘密数量
    :param prime: 共享秘密素数
    :return: 共享秘密列表
    """
    if min_num > share_num:
        print('Error: min_num > share_num')
        return
    poly_coef = [secret]
    shares = []
    for i in range(1, min_num):
        # poly_coef.append(random.randint(0, prime))
        poly_coef.append(1)
    for i in range(1, share_num):
        # x = random.randint(0, prime)
        x = i
        y = utils.calc_poly(poly_coef, x, prime)
        shares.append((x, y))
    return shares

def dec(shares, min_num, prime):
    """
    :param shares: 共享秘密列表
    :param min_num: 最小秘密数量
    :param prime: 共享秘密素数
    :return: 原始秘密
    """
    sums = 0
    prod_arr = []
    for j, share_j in enumerate(shares):
        xj, yj = share_j
        prod = Decimal(1)
        for i, share_i in enumerate(shares):
            xi, _ = share_i
            if i != j:
                prod *= Decimal(Decimal(xi)/(xi-xj))
        prod *= yj
        sums += Decimal(prod)
    return int(round(Decimal(sums), 0))

def main():
    k, n = 3, 5
    p = 1e9 + 7
    l = enc(123455, k, n, p)
    print(f'my shares: {l}')
    print(dec(l, k, p))

if __name__ == '__main__':
    main()