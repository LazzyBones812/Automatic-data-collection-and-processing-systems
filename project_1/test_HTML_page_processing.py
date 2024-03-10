import HTML_page_processing

fnt_true = ['Блеканов Иван Станиславович', 'Максимов Алексей Юрьевич', 'Малинина Мария Анатольевна', 'Митрофанов Евгений Павлович', 'Митрофанова Ольга Александровна', 'Мишенин Алексей Николаевич', 'Овсянников Александр Дмитриевич', 'Орехов Михаил Юрьевич', 'Охотников Антон Юрьевич', 'Печников Андрей Анатольевич', 'Попова Светлана Владимировна', 'Сергеев Сергей Львович', 'Стученков Александр Борисович', 'Уланов Александр Владимирович']
sw_true = ['Информационный поиск; теория информации', 'Интеллектуальный анализ данных', 'Вебометрика', 'Компьютерное моделирование сложных объектов', 'Системы управления базами данных, сверхбольшие базы данных', 'Компьютерная криминалистика', 'Распознавание и обработка изображений', 'Прогнозирования временных рядов в прикладных задачах анализа данных']
et_true = [' I.blekanov@spbu.ru', 'm.malinina@spbu.ru', 'e.mitrofanov@spbu.ru', 'o.a.mitrofanova@spbu.ru', 'a.mishenin@spbu.ru', 'a.ovsyannikov@spbu.ru', 'm.orekhov@spbu.ru', 'a.okhotnikov@spbu.ru', 'a.pechnikov@spbu.ru', 's.popova@spbu.ru', 's.l.sergeev@spbu.ru', 'a.stuchenkov@spbu.ru', 'a.ulanov@spbu.ru']

def test_parse_full_name_of_teacher():
    assert HTML_page_processing.parse_full_name_of_teacher() ==  fnt_true

def test_parse_scientific_work():
    assert HTML_page_processing.parse_scientific_work() == sw_true

def test_parse_email_of_teacher():
    assert HTML_page_processing.parse_email_of_teacher() == et_true
