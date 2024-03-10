import main_2
import os

def test_1():
    assert main_2.main_work('3.pdf') == 'Файл PDF обработан'

def test_2():
    assert main_2.main_work(os.getcwd() + '\\' + '1.doc') == 'Файл DOC обработан'

def test_3():
    assert main_2.main_work('1.docx') == 'Файл DOCX обработан'

def test_4():
    assert main_2.main_work('1.djvu') == 'Файл DJVU обработан'

def test_5():
    assert main_2.main_work('404.djvu') == 'Такого файла не существует'

def test_6():
    assert main_2.main_work('1.pdq') == 'Такого файла не существует'
