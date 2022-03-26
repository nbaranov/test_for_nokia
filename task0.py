
def reverse_words_in_str(string:str) -> str:
    # если слово одно просто разворачиваем его
    if len(string.split()) == 1:
        return string[::-1]
    # если слов больше проходимся посимвольно по строке
    new_string = ''
    start_index = None
    for i in range(len(string)):
        # если символ не пробел и при этом начала слова нет, считаем этот символ началом слова
        if string[i] != ' ' and start_index == None:
            start_index = i
        # если пробел и существует начало, значит это конец слова
        elif string[i] == ' ':
            if start_index != None:
                finish_index = i
                # берем срез от начало до конца слова, а потом этот срез разворачиваем
                new_string += string[start_index : finish_index][::-1] + " "
                start_index = None
            # если начала нет, то это очередной пробел
            else:
                new_string += ' '
            # если строка закончилась без пробела, то добавляем срез от конца до последнего начала слова
        elif i == len(string)-1:
            new_string += string[-1 : start_index-1: -1]
    return new_string


def reverse_words_in_str2(string:str) -> str:
    # дробим на слова и разворачиваем их
    words = string.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    space_count = 0
    # если строка начинается с пробела не добавляем в начало первое слово
    if string[0] == " ":
        words_count = 0
        new_string = ""
    else:
        words_count = 1
        new_string = words[0]
    # проходимся по символам строки считаем пробелы
    for char in string:
        if char == " ":
            space_count += 1
        # если следуюзий сивол не пробел, обнуляем счетчик и добавляем развернутое слово
        elif char != " " and space_count > 0:
            new_string += " " * space_count + words[words_count]
            space_count = 0
            words_count += 1
    # если строка заканчивается пробелами добавим их
    new_string += " " * space_count
    return new_string




