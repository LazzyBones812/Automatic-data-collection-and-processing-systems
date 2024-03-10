import DOCUMENT_processing
import os

def test_1():
    assert DOCUMENT_processing.main_work('3.pdf') == 'PDF файл успешно создан'

def test_2():
    assert DOCUMENT_processing.main_work(os.getcwd() + '\\' + '1.doc') == 'DOC файл успешно создан'

def test_3():
    assert DOCUMENT_processing.main_work('1.docx') == 'DOCX файл успешно создан'

def test_4():
    assert DOCUMENT_processing.main_work('1.djvu') == 'DJVU файл успешно создан'

def test_5():
    assert DOCUMENT_processing.main_work('404.djvu') == 'Такого файла не существует'

def test_6():
    assert DOCUMENT_processing.main_work('1.pdq') == 'Такого файла не существует'
