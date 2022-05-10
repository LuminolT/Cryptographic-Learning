for i in range(15):
    round = 1
    iter = (i + i) % 15
    while iter != i:
        iter += i
        iter %= 15
        round += 1
    print(f'{i}\'s order: {round}')
