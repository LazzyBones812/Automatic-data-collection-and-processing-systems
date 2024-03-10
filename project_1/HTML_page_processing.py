import requests
from bs4 import BeautifulSoup

''' Адрес страницы кафедры "Технологии программирования" на кафедре ПМ-ПУ СПбГУ '''
url = 'https://pmpu.space/35005692bcff46169bae5932d91b30c5'

''' Получение html-страницы '''
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

''' ФИО преподавателей кафедры "Технологии программирования" '''
def parse_full_name_of_teacher():
    all_info = soup.find_all('span', {'class': 'notion-semantic-string'})
    res_fnt = []
    for r in all_info:
        res_text_in_span = r.find('span')
        result = res_text_in_span.find('a', rel=None)
        if result is not None:
            res_fnt.append(result.text)
    return res_fnt

''' Научные работы, которые проводятся на кафедре "Технологии программирования" '''
def parse_scientific_work():
    all_info = soup.find_all('li', {'class': 'notion-list-item'})
    res_sw = []
    for r in all_info:
        res_sw.append(r.text)
    return res_sw

''' Email всех преподавателей кафедры "Технологии программирования" '''
def parse_email_of_teacher():
    all_info = soup.find_all('span', {'class': 'notion-semantic-string'})
    res_et = []
    for r in all_info:
        result = r.find('a', {'rel':'noopener noreferrer'})
        if result is not None:
            if '@spbu.ru' in result.text:
                res_et.append(result.text)
    return res_et


''' Очистка html-страницы. Оставляется только информация, которая входит в класс notion-sematic-string '''
result = soup.find_all('span', {'class': 'notion-semantic-string'})

''' Множество для всех уникальных значений страницы '''
set_r = set()

''' Финальная очистка страницы и запись полезной информации в файл'''
with open('HTML_page_processing.txt', 'w+') as f:
    for r in result:
        res_text_in_span = r.find('span').text                          # информация в теге span
        set_r.add(res_text_in_span)                                     # добавление полученной информации в множество
        f.write(res_text_in_span + '\n')                                # запись полученной информации в файл
        res_text_in_href = r.find('a', 'notion-link link')              # информация в теге a класса notion-link link
        if res_text_in_href is not None:                                # проверка на None и уникальность полученной информации
            if res_text_in_href.text not in set_r:
                f.write(res_text_in_href.text + '\n')                   # запись полученной информации в файл
