import requests
from bs4 import BeautifulSoup

''' Адрес страницы кафедры "Технологии программирования" на кафедре ПМ-ПУ СПбГУ '''
url = 'https://pmpu.space/35005692bcff46169bae5932d91b30c5'

''' Получение html-страницы '''
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

''' Очистка html-страницы. Оставляется только информация, которая входит в класс notion-sematic-string '''
result = soup.find_all('span', {'class': 'notion-semantic-string'})

''' Множество для всех уникальных значений страницы '''
set_r = set()

''' Финальная очистка страницы и вывод полезной информации '''
for r in result:
    res_text_in_span = r.find('span').text                          # информация в теге span
    set_r.add(res_text_in_span)                                     # добавление полученной информации в множество
    print(res_text_in_span)                                         # вывод полученной информации
    res_text_in_href = r.find('a', 'notion-link link')              # информация в теге a класса notion-link link
    if res_text_in_href is not None:                                # проверка на None и уникальность полученной информации
        if res_text_in_href.text not in set_r:
            print(res_text_in_href.text)
