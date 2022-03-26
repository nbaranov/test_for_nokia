# рекурсивная функция поэтапно делит на длинну части числа и сравнивает равныли ли две части 
def is_part_rec(number:int, part:int) -> bool:
    new_part = number % 10**len(str(part))
    rest = number // 10**len(str(part))
    if rest == 0 and new_part == part:
        return True
    elif part != new_part:
        return False
    else:
        return is_part_rec(rest, part)


# функция подбирает части числа от 2 символов до половины длинны числа
def is_part_of_number(number:int) -> bool:
    max_part = int(len(str(number))/2)
    for i in range(2, max_part+1):
        if is_part_rec(number, number % 10**i):
            return True
    return False

