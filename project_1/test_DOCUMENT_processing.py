import DOCUMENT_processing
import os

'''НАБОР PDF ТЕСТОВ'''

def test_1():
    # Пустой файл
    assert DOCUMENT_processing.main_work('PDF/Empty.pdf') != 'Такого файла не существует', 'Файл существует, но пустой'

def test_2():
    # Отсутствующий документ
    assert DOCUMENT_processing.main_work('PDF/1.pdf') == 'Такого файла не существует', 'Несуществующий файл выполнен'

def test_4():
    # Достаточно большой файл
    assert DOCUMENT_processing.main_work('PDF/LargePDF.pdf') == 'Файл PDF обработан', 'Не обработан большой PDF файл'

def test_5():
    # Файл-презентация
    assert DOCUMENT_processing.main_work('PDF/Presentation.pdf') == 'Файл PDF обработан', 'Не обработана PDF-презентация'

def test_6():
    # Файл только с картинкой
    assert DOCUMENT_processing.main_work('PDF/Image.pdf') == 'Файл PDF обработан', 'Не обработан PDF-файл с картинкой'

def test_7():
    # Русский и английский тексты
    assert DOCUMENT_processing.main_work('PDF/Russian_And_English.pdf') == 'Файл PDF обработан', 'Не обработан комбинированный русский, и английский текст'

def test_8():
    # Текст и картинки
    assert DOCUMENT_processing.main_work('PDF/Text_And_Images.pdf') == 'Файл PDF обработан', 'Не обработан комбинированный файл - картинки + текст'

'''
PDF PART ENDED
'''

def test_3():
    # Неправильное расширение файла
    assert DOCUMENT_processing.main_work('1.pptx') == 'Неверное расширение файла', 'Неподходящее расширение файла'



'''
DOCX PART
'''
def test_9():
    # Отсутствующий файл
    assert DOCUMENT_processing.main_work('DOCX/2.docx') == 'Такого файла не существует', 'Нет ошибки несуществующего файла'

def test_10():
    # Пустой документ
    assert DOCUMENT_processing.main_work('DOCX/Empty.docx') == 'Файл Docx обработан', 'Не обработан пустой документ'
def test_11():
    # Файл с изображением
    assert DOCUMENT_processing.main_work('DOCX/Image.docx') == 'Файл Docx обработан', 'Не обработан файл с картинкой'

def test_12():
    # Англ-Рус документ
    assert DOCUMENT_processing.main_work('DOCX/Russian_And_English.docx') == 'Файл Docx обработан', 'Не обработан комбинированный документ - русский и английский'

def test_13():
    # Текст + картинки
    assert DOCUMENT_processing.main_work('DOCX/Text_And_Images.docx') == 'Файл Docx обработан', 'Не обработан комбинированный документ - текст + картинки'

def test_14():
    # Большой документ
    assert DOCUMENT_processing.main_work('DOCX/LargeDocx.docx') == 'Файл Docx обработан', 'Не обработан большой документ'

def test_15():
    # Обыкновенный документ
    assert DOCUMENT_processing.main_work('DOCX/1.docx') == "Файл Docx обработан", "Не обработан обыкновенный документ"

'''
DOC Part
'''
def test_16():
    # Отсутствующий файл
    assert DOCUMENT_processing.main_work('DOC/2.doc') == 'Такого файла не существует', 'Нет ошибки несуществующего файла'
def test_17():
    # Пустой документ
    assert DOCUMENT_processing.main_work(os.getcwd() + '\\' + 'DOC/Empty.doc') == 'Файл Doc обработан', 'Не обработан пустой документ'
def test_18():
    # Файл с изображением
    assert DOCUMENT_processing.main_work(os.getcwd() + '\\' + 'DOC/Image.doc') == 'Файл Doc обработан', 'Не обработан файл с картинкой'

def test_19():
    # Англ-Рус документ
    assert DOCUMENT_processing.main_work(os.getcwd() + '\\' + 'DOC/Russian_And_English.doc') == 'Файл Doc обработан', 'Не обработан комбинированный документ - русский и английский'

def test_20():
    # Текст + картинки
    assert DOCUMENT_processing.main_work(os.getcwd() + '\\' + 'DOC/Text_And_Images.doc') == 'Файл Doc обработан', 'Не обработан комбинированный документ - текст + картинки'

def test_21():
    # Большой документ
    assert DOCUMENT_processing.main_work(os.getcwd() + '\\' + 'DOC/LargeDoc.doc') == 'Файл Doc обработан', 'Не обработан большой документ'

def test_22():
    #обычный документ
    assert DOCUMENT_processing.main_work(os.getcwd() + '\\' + 'Doc/1.doc') == 'Файл Doc обработан', 'Не обработан обычный документ'


'''
DJVU part
'''

def test_23():
    # Отсутствующий файл
    assert DOCUMENT_processing.main_work('DJVU/1.djvu') == 'Такого файла не существует', 'Нет ошибки несуществующего файла'

def test_24():
    # Sample1
    assert DOCUMENT_processing.main_work('DJVU/Sample1.djvu') == 'Файл DJVU обработан', 'Не обработан Sample1 файл'

def test_25():
    # Sample2
    assert DOCUMENT_processing.main_work('DJVU/Sample2.djvu') == 'Файл DJVU обработан', 'Не обработан Sample2 файл'

def test_26():
    # DJVU2
    assert DOCUMENT_processing.main_work('DJVU/DJVU2.djvu') == 'Файл DJVU обработан', 'Не обработан DJVU2 файл'

def test_27():
    # DJVU3
    assert DOCUMENT_processing.main_work('DJVU/DJVU3.djvu') == 'Файл DJVU обработан', 'Не обработан DJVU3 файл'
