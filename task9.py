import random


def gen_lottery_tiket() -> list:
    tiket = []
    istart = 1
    # девять строк
    for i in range(0, 9):
        line = []
        # цикл пока не добавим 3 числа в строку
        while len(line) < 3:
            ifinish = (i+1)*10
            item = random.randint(istart, ifinish)
            if item not in line:
                line.append(item)
        istart = ifinish + 1
        tiket.append(sorted(line))
    return tiket
