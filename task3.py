
def get_top(unsorted_dict, limit):
    sorted_dict = {}
    # сортируем ключи по значению, от максимального к минимальному, делаем срез по ограничителю 
    sorted_keys = sorted(unsorted_dict, key=unsorted_dict.get, reverse=True)[:limit]
    # проходим по списку ключей, достаем их значения их оригинального словаря 
    for key in sorted_keys:
        sorted_dict.update({key : unsorted_dict.get(key)})
    return sorted_dict
    

