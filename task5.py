# находим максимальное и увеличиваем на 1, чтобы range включал максимальное 
def sum_between(a:int, b:int) -> int:
    return sum(range(min(a, b), max(a, b) + 1))


def sum_between_with_descript(a:int, b:int) -> str:
    sum = sum_between(a, b)
    if a == b:
        return f"{sum} ({sum} числа равны)"
    # если a > b идем по списку до b-1 в обратном порядке 
    elif a > b:
        return f"{sum} ({' + '.join([str(x) for x in range(a, b-1, -1)])} = {sum})"
    # если b > a идем по порядку до b+1 
    else:
        return f"{sum} ({' + '.join([str(x) for x in range(a, b+1)])} = {sum})"

