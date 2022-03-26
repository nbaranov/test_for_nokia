import unittest

from task0 import reverse_words_in_str, reverse_words_in_str2
from task1 import count_alfabet_index
from task2 import count_words
from task3 import get_top
from task4 import get_links
from task5 import sum_between, sum_between_with_descript
from task6 import is_mirror
from task7 import is_part_of_number
from task8 import chees_board
from task9 import gen_lottery_tiket


class NokiaTasks(unittest.TestCase):
    msg = "Huston we have a problem!!!"

    def test_task0(self):
        self.assertEqual(reverse_words_in_str("This is an example!  "), 
                                              "sihT si na !elpmaxe  ", self.msg)
        self.assertEqual(reverse_words_in_str("double  spaces"), 
                                              "elbuod  secaps", self.msg)
        self.assertEqual(reverse_words_in_str(" OnE MoRe       sPuPid     StRiNg  !!!!!?????  "),
                                              " EnO eRoM       diPuPs     gNiRtS  ?????!!!!!  ", self.msg)
        self.assertEqual(reverse_words_in_str(" level radar rotor madam "), 
                                              " level radar rotor madam ", self.msg)
        self.assertEqual(reverse_words_in_str("???FTW"), 
                                              "WTF???", self.msg)
        self.assertEqual(reverse_words_in_str2("This is an example!"), 
                                               "sihT si na !elpmaxe", self.msg)
        self.assertEqual(reverse_words_in_str2("double  spaces"), 
                                               "elbuod  secaps", self.msg)
        self.assertEqual(reverse_words_in_str2("   OnE MoRe       sPuPid     StRiNg  !!!!!?????  "),
                                               "   EnO eRoM       diPuPs     gNiRtS  ?????!!!!!  ", self.msg)
        self.assertEqual(reverse_words_in_str2("level radar rotor madam"), 
                                               "level radar rotor madam", self.msg)
        self.assertEqual(reverse_words_in_str2("???FTW  "), 
                                               "WTF???  ", self.msg)


    def test_task1(self):
        self.assertEqual(count_alfabet_index("abode"), 4, self.msg)
        self.assertEqual(count_alfabet_index("ABc"), 3, self.msg)
        self.assertEqual(count_alfabet_index("xyzD"), 1, self.msg)
        self.assertEqual(count_alfabet_index("abcdefghijklmnopqrstuvwxyz"), 26, self.msg)
        self.assertEqual(count_alfabet_index("asdfefghijklmnopqrstuvwxyzjksdjksdjkd"), 23, self.msg)


    def test_task2(self):
        self.assertEqual(count_words("тест, такой тест"), {'тест': 2, 'такой': 1}, self.msg)
        self.assertEqual(count_words("  тест, тест... тест!!! 123 тест654"), {'тест': 3}, self.msg)
        self.assertEqual(count_words("123 1 2 3 !!! ... ,,, "), {}, self.msg)


    def test_task4(self):
        self.assertEqual(get_top({'тест': 2, 'такой': 1}, 1),
                                 {'тест': 2,}, self.msg)
        self.assertEqual(get_top({'тест': 2, 'такой': 1}, 2),
                                 {'тест': 2, 'такой': 1}, self.msg)
        self.assertEqual(get_top({'тест': 2, 'такой': 1, "текст" : 3}, 2),
                                 {'текст': 3, 'тест': 2}, self.msg)
        

    def test_task4(self):
        text = """Адрес https://my-site.ru/test больше не доступен. 
Но если обратиться к www.my-test.com:8080 всё работает хорошо. 
Напиши мне на test@test.ru"""
        result = ['https://my-site.ru/test', 'www.my-test.com:8080']
        self.assertEqual(get_links(text), result, self.msg)


    def test_task5(self):
        self.assertEqual(sum_between(1, 0), 1, self.msg)
        self.assertEqual(sum_between(1, 2), 3, self.msg)
        self.assertEqual(sum_between(0, 1), 1, self.msg)
        self.assertEqual(sum_between(1, 1), 1, self.msg)
        self.assertEqual(sum_between(-1, 0), -1, self.msg)
        self.assertEqual(sum_between(-1, 2), 2, self.msg)

        self.assertEqual(sum_between_with_descript(1, 0), "1 (1 + 0 = 1)", self.msg)
        self.assertEqual(sum_between_with_descript(1, 2), "3 (1 + 2 = 3)", self.msg)
        self.assertEqual(sum_between_with_descript(0, 1), "1 (0 + 1 = 1)", self.msg)
        self.assertEqual(sum_between_with_descript(1, 1), "1 (1 числа равны)", self.msg)
        self.assertEqual(sum_between_with_descript(-1, 0), "-1 (-1 + 0 = -1)", self.msg)
        self.assertEqual(sum_between_with_descript(-1, 2), "2 (-1 + 0 + 1 + 2 = 2)", self.msg)
    

    def test_task6(self):
        self.assertEqual(is_mirror(3456), False, self.msg)
        self.assertEqual(is_mirror(5234234), False, self.msg)
        self.assertEqual(is_mirror(435534), True, self.msg)
        self.assertEqual(is_mirror(9887889), True, self.msg)


    def test_task7(self):
        self.assertEqual(is_part_of_number(525252), True, self.msg)
        self.assertEqual(is_part_of_number(123123123), True, self.msg)
        self.assertEqual(is_part_of_number(43434), False, self.msg)
        self.assertEqual(is_part_of_number(10110), False, self.msg)


    def test_task8(self):
        result = """8 # # # #
7# # # # 
6 # # # #
5# # # # 
4 # # # #
3# # # # 
2 # # # #
1# # # # 
 abcdefgh""" 
        self.assertEqual(chees_board('#', 8), result, self.msg )


    def test_task9(self):
        tiket = gen_lottery_tiket()
        # проверяем что строк 9
        self.assertEqual(len(tiket), 9, self.msg)
        istart = 1
        for i in range(len(tiket)):
            ifinish = (i+1)*10
            # проверяем что в строке 3 числа
            self.assertEqual(len(tiket[i]), 3, self.msg)
            for number in tiket[i]:
                # проверяем что числа в диапазоне строке
                self.assertEqual(istart <= number <= ifinish, True, self.msg)
            istart = ifinish + 1


if __name__ == "__main__":
    runner = unittest.main()
