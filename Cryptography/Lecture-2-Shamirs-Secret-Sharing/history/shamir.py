import random
import math
from utils import *
from decimal import Decimal
from Crypto.Util.number import bytes_to_long, long_to_bytes

class shamir:
    """
        GF(2^128)下的Shamir(k,n)秘密共享
    """

    def enc(secret, min_num, share_num):
        """
        :param s: 原始秘密
        :param min_num: 最小秘密数量
        :param share_num: 共享秘密数量
        :return: 共享秘密列表
        """
        if min_num > share_num:
            raise ValueError("min_num > share_num")
        poly_coef = [element(secret)]
        shares = []
        for i in range(1, min_num):
            poly_coef.append(element(random.randint(0, 2**128)))
            # poly_coef.append(1)
        for i in range(0, share_num):
            x = element(i)
            y = calc_poly(poly_coef, x)
            shares.append((x, y))
        return shares

    def dec(shares, min_num):
        """
        :param shares: 共享秘密列表
        :param min_num: 最小秘密数量
        :param prime: 共享秘密素数
        :return: 原始秘密
        """
        k = len(shares)

        gf_shares = []
        for x in shares:
            idx = x[0]
            value = x[1]
            if any(y[0] == idx for y in gf_shares):
                raise ValueError("Duplicate share")
            gf_shares.append((idx, value))

        result = element(0)
        for j in range(k):
            x_j, y_j = gf_shares[j]

            numerator = element(1)
            denominator = element(1)

            for m in range(k):
                x_m = gf_shares[m][0]
                if m != j:
                    numerator *= x_m
                    denominator *= x_j + x_m
            result += y_j * numerator * denominator.inverse()
        return result