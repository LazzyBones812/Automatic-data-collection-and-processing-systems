import os
from pypdf import PdfReader 
import docx
import win32com.client

def pdf_process(fnd: str):
    reader = PdfReader(fnd)
    with open('PDF_page_processing.txt', 'w+', encoding='utf-8') as fout:
        for p in range(len(reader.pages)):
            fout.write(reader.pages[p].extract_text())

def doc_process(fnd: str):
    app = win32com.client.Dispatch('Word.Application') 
    doc = app.Documents.Open(fnd) 
    content=doc.Content.Text
    app.Quit()
    with open('DOC_page_processing.txt', 'w+') as fout:
        fout.write(content)

def docx_process(fnd: str):
    doc = docx.Document(fnd)
    with open('DOCX_page_processing.txt', 'w+') as fout:
        for paragraph in doc.paragraphs:
            fout.write(paragraph.text + '\n')

def djvu_process(fnd: str):
    djvu_str_path = "djvused " + fnd + " -u -e \"print-pure-txt\" > DJVU_page_processing.txt"
    os.system(djvu_str_path)

def main_work(fnd):
    if not os.path.isfile(fnd):
        return 'Такого файла не существует'
    elif fnd.endswith('.pdf'):
        pdf_process(fnd)
        return 'PDF файл успешно создан'
    elif fnd.endswith('.doc'):
        doc_process(fnd)
        return 'DOC файл успешно создан'
    elif fnd.endswith('.docx'):
        docx_process(fnd)
        return 'DOCX файл успешно создан'
    elif fnd.endswith('.djvu'):
        djvu_process(fnd)
        return 'DJVU файл успешно создан'
    else:
        return 'Неверное расширение файла'

# name_doc = input('Введите название документа вместе с расширением: ')
# full_name_doc = os.getcwd() + '\\' + name_doc
# main_work(full_name_doc)
