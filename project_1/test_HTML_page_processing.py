import HTML_page_processing

fnt_true = ['Блеканов Иван Станиславович', 'Максимов Алексей Юрьевич', 'Малинина Мария Анатольевна', 'Митрофанов Евгений Павлович', 'Митрофанова Ольга Александровна', 'Мишенин Алексей Николаевич', 'Овсянников Александр Дмитриевич', 'Орехов Михаил Юрьевич', 'Охотников Антон Юрьевич', 'Печников Андрей Анатольевич', 'Попова Светлана Владимировна', 'Сергеев Сергей Львович', 'Стученков Александр Борисович', 'Уланов Александр Владимирович']
sw_true = ['Информационный поиск; теория информации', 'Интеллектуальный анализ данных', 'Вебометрика', 'Компьютерное моделирование сложных объектов', 'Системы управления базами данных, сверхбольшие базы данных', 'Компьютерная криминалистика', 'Распознавание и обработка изображений', 'Прогнозирования временных рядов в прикладных задачах анализа данных']
et_true = [' I.blekanov@spbu.ru', 'm.malinina@spbu.ru', 'e.mitrofanov@spbu.ru', 'o.a.mitrofanova@spbu.ru', 'a.mishenin@spbu.ru', 'a.ovsyannikov@spbu.ru', 'm.orekhov@spbu.ru', 'a.okhotnikov@spbu.ru', 'a.pechnikov@spbu.ru', 's.popova@spbu.ru', 's.l.sergeev@spbu.ru', 'a.stuchenkov@spbu.ru', 'a.ulanov@spbu.ru']

uni_soup = HTML_page_processing.get_soup('https://pmpu.space/35005692bcff46169bae5932d91b30c5')

def test_parse_full_name_of_teacher():
    assert HTML_page_processing.parse_full_name_of_teacher(uni_soup) == fnt_true

def test_parse_scientific_work():
    assert HTML_page_processing.parse_scientific_work(uni_soup) == sw_true

def test_parse_email_of_teacher():
    assert HTML_page_processing.parse_email_of_teacher(uni_soup) == et_true

test_parse_scientific_work()
test_parse_email_of_teacher()
test_parse_full_name_of_teacher()

def new_link(url: str):
    assert HTML_page_processing.main_HTML_work(url) == 'HTML страница обработана', 'Не получилось'

#Рандомная ссылка, не имеющая ничего общего с собираемыми данными
new_link('https://filesamples.com/')

#Рандомная ссылка, не имеющая ничего общего с собираемыми данными
new_link('https://www.jefkine.com/general/2018/05/21/2018-05-21-vanishing-and-exploding-gradient-problems/')

#Ссылка, не рабочая в России
new_link('https://www.spotify.com/')

#Ссылка, не рабочая в России
new_link('https://open.spotify.com/artist/7dGJo4pcD2V6oG8kP0tJRR')

#Кафедра Теории Управления
new_link('https://pmpu.space/45f602328e4f40d1a91eaf66b4dd79f0')

#Кафедра Компьютерных технологий и систем
new_link('https://pmpu.space/461432d0373649ab90e84dfd34d10cff')

#Список преподавателей в Стэнфорде
new_link('https://ed.stanford.edu/faculty/profiles?group=active&affiliation=All&title=')

#конкретный преподаватель в Стэнфорде
new_link('https://ed.stanford.edu/faculty/subini')


'''
Не работает:

#Кафедра Математической теории игр и статистических решений
new_link('https://pmpu.space/56207e07591e4a629cadaee8e36052c8')

#Кафедра Механики управляемого движения
new_link('https://pmpu.space/d2c48a2773e348919506b1cae922c255')

#Рандомная ссылка, не имеющая ничего общего с собираемыми данными
#new_link('https://towardsdatascience.com/intuitively-understanding-convolutions-for-deep-learning-1f6f42faee1')

'''
