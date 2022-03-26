# делим на слова, очищаем их от знаков препинания, если  словао не цифра и не "а" "и"
# считаем и обновляем словарь
from unittest import result


def count_words(text:str) -> dict: 
    BAD_WORDS = ["а", "и", "у", "в", "но", "на", "с", "за", "от", "по"]
    words = text.split()
    counted_words = {}
    for word in words:
        cleared_word = word.strip(".,()!?:;—").lower()
        if cleared_word.isalpha() and cleared_word not in BAD_WORDS:
            counter = counted_words.get(cleared_word, 0)
            counted_words.update({cleared_word: counter + 1})
    return counted_words

