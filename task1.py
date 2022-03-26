def count_alfabet_index(string: str) -> int:
    ALFABET = "abcdefghijklmnopqrstuvwxyz"
    # устанавиливаем длинну цикла, по длинне алфавита или строки 
    finish_for = 26 if len(string) > 26 else len(string)
    count = 0
    # посимвольно проверяем равны ли элементы с одинаковыми индексами.
    for i in range(finish_for):
        if string[i].lower() == ALFABET[i]:
            count += 1
    return count


