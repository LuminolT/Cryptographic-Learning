from Crypto.Util import number
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.py3compat import is_native_int

def calc_poly(poly_coef, x):
    idx = x
    share = element(0)
    for val in poly_coef:
        share = idx * share + val
    return share.encode()

class element(object):
    """GF(2^128)域元素"""

    # GF(2^128)域中的不可约多项式
    irre_poly = 1 + 2 + 4 + 128 + 2 ** 128
    
    def __init__(self, encoded_value):
        if is_native_int(encoded_value):
            self._value = encoded_value
        elif len(encoded_value) == 16:
            self._value = bytes_to_long(encoded_value)
        else:
            raise ValueError("被分享的数据必须是一个整数或者16字节的字符串")

    def __eq__(self, other):
        return self._value == other._value

    def __int__(self):
        """返回域元素，以整数表示"""
        return self._value

    def encode(self):
        """返回域元素，以16字节的字符串表示"""
        return long_to_bytes(self._value, 16)

    def __mul__(self, factor):

        f1 = self._value
        f2 = factor._value

        # 运算加速
        if f2 > f1:
            f1, f2 = f2, f1

        if self.irre_poly in (f1, f2):
            return element(0)

        mask1 = 2 ** 128
        v, z = f1, 0
        while f2:
            # if f2 ^ 1: z ^= v
            mask2 = int(bin(f2 & 1)[2:] * 128, base=2)
            z = (mask2 & (z ^ v)) | ((mask1 - mask2 - 1) & z)
            v <<= 1
            # if v & mask1: v ^= self.irre_poly
            mask3 = int(bin((v >> 128) & 1)[2:] * 128, base=2)
            v = (mask3 & (v ^ self.irre_poly)) | ((mask1 - mask3 - 1) & v)
            f2 >>= 1
        return element(z)

    def __add__(self, term):
        return element(self._value ^ term._value)

    def inverse(self):
        """Return the inverse of this element in GF(2^128)."""

        # We use the Extended GCD algorithm
        # http://en.wikipedia.org/wiki/Polynomial_greatest_common_divisor

        if self._value == 0:
            raise ValueError("Inversion of zero")

        r0, r1 = self._value, self.irre_poly
        s0, s1 = 1, 0
        while r1 > 0:
            q = _div_gf2(r0, r1)[0]
            r0, r1 = r1, r0 ^ _mult_gf2(q, r1)
            s0, s1 = s1, s0 ^ _mult_gf2(q, s1)
        return element(s0)

    def __pow__(self, exponent):
        result = element(self._value)
        for _ in range(exponent - 1):
            result = result * self
        return result


def _mult_gf2(f1, f2):
    """GF(2)多项式乘法"""

    # Ensure f2 is the smallest
    if f2 > f1:
        f1, f2 = f2, f1
    z = 0
    while f2:
        if f2 & 1:
            z ^= f1
        f1 <<= 1
        f2 >>= 1
    return z


def _div_gf2(a, b):
    """
    GF(2)多项式除法（用于exgcd）
    a = b * q + r，且 deg(r)<deg(b)
    """

    if (a < b):
        return 0, a

    deg = number.size
    q = 0
    r = a
    d = deg(b)
    while deg(r) >= d:
        s = 1 << (deg(r) - d)
        q ^= s
        r ^= _mult_gf2(b, s)
    return (q, r)