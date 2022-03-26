from unittest import result


def chees_board(symbol:str, size:int) ->str:
    ALFABET = "abcdefghijklmnopqrstuvwxyz"
    # огрничиваем размер доски длинной алфавита 26
    size = 26 if size > 26 else size
    result_str = ''
    for i in range(size, 0, -1):
        # собираем строки начиная с пробела или символа в записимости от четности строки
        result_str += f"{i}{''.join([' ' if x%2 == i%2 else symbol for x in range(size)])}\n"
    result_str += ' ' + ALFABET[:size]
    return result_str
