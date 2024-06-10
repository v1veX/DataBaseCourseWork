def reform_name(s):
    s = s.replace(' ', '')
    s = s.lower()

    # Все лишние символы и слова, которые надо убрать из названия
    check_list = ['шир.', '_', '(', ')', 'линолеум', 'бытовой', 'коммерческий', 'полукоммерческий', 'усиленный', 'дляж/дтранспорта']
    for item in check_list:
        if item in s:
            s = s.replace(item, '')

    # Специфический случай для сайта Залог
    if '/' in s:
        s_split = s.split('/')
        s = s_split[0]

    return s
