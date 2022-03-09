def calc_poly(poly_coef, x, prime):
    y = 0
    tmp = 1
    for i in range(len(poly_coef)):
        y += (poly_coef[i] * tmp) % prime
        tmp *= x
    return int(y)