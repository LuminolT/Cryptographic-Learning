from pydoc import plain
import numpy as np

MATRIX_SIZE = 3

def get_random_key(m_size):
    A = np.random.randint(10, size = (m_size, m_size))
    b = np.random.randint(10, size = (m_size, 1))
    assert np.linalg.det(A)
    return A, b

def enc(s, A, b, n):
    l = []
    for i in s:
        l.append(ord(i) - ord('a'))
    M = np.array(l)
    C = A * M + b 
    res = ''
    for idx in range(np.shape(A)[0]):
        C[0][idx] = C[0][idx] % n
        res += chr(C[0][idx] + ord('a'))
    return res

def dec(s, A, b, n):
    l = []
    for i in s:
        l.append(ord(i) - ord('a'))
    M = np.array(l)
    C = np.linalg.inv(A) * (M - b) 
    res = ''
    for idx in range(np.shape(A)[0]):
        C[0][idx] = C[0][idx] % n
        res += chr(int(C[0][idx] + ord('a')))
    return res

def main():
    plain_text = 'abc'
    m_size = len(plain_text)
    A, b = get_random_key(m_size)
    cypher_text = enc(plain_text, A, b, 26)
    print('Cypher Text: {}'.format(cypher_text))
    plain_text = dec(cypher_text, A, b, 26)
    print('Plain Text: {}'.format(plain_text))

if __name__ == '__main__':
    main()