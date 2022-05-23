from math import floor


def find_minimun_distance(C: list[int]) -> int:
    res = bin(C[0] ^ C[1]).count("1")
    for i in range(len(C)):
        for j in range(i+1, len(C)):
            print(f'd_{i+1}_{j+1} := {bin(C[i] ^ C[j])}')
            res = min(res, bin(C[i] ^ C[j]).count("1"))
    return(res)


def main():
    # C = [0b10010, 0b01001, 0b10101, 0b01110]
    # C = [0b101010, 0b101101, 0b011011, 0b001110]
    C = [0b10100, 0b01010, 0b01101, 0b10011]
    min_dis = find_minimun_distance(C)
    print(
        f"min_dis: {min_dis}, detect: {min_dis - 1}, correct: {floor((min_dis - 1)/2)}")


if __name__ == "__main__":
    main()
