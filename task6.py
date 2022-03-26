# конвептируем в строку и сравниваем с обратной
def is_mirror(number:int) -> bool:
    return str(number) == str(number)[::-1]

