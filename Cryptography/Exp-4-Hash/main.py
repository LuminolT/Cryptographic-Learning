import os
from Crypto.Hash import SHA256

BLOCK_SIZE = 1024


def get_file_block(file_name):
    with open(file_name, 'rb') as f:
        for idx in reversed(range(0, os.path.getsize(file_name), BLOCK_SIZE)):
            f.seek(idx)
            yield f.read(BLOCK_SIZE)


def stream_hash(file_name):
    hash_result = b''
    for block in get_file_block(file_name):
        h = SHA256.new(block + hash_result)
        hash_result = h.digest()
    return h.hexdigest()


def main() -> None:
    file_name = '6.1.intro.mp4'
    # file_name = '6.2.birthday.mp4'
    print(stream_hash(file_name.encode()))


if __name__ == '__main__':
    main()
