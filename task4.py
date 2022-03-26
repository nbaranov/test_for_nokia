def get_links(text:str) -> list:
    # константа с признаками ссылки, т.е. доменами
    LINK_REFERENCE = ['.ru', '.com', '.ua', '.by', '.kz']
    links = []
    words = text.split()
    # для каждого слова проверяем есть ли в домен и отсутствует ли в нем @ - email-признак 
    for word in words:
        for domen in LINK_REFERENCE:
            if domen in word and '@' not in word:
                links.append(word)

    return links

