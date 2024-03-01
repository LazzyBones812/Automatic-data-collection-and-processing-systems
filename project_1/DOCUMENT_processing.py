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
    pass

name_doc = input('Введите название документа вместе с расширением: ')
full_name_doc = os.getcwd() + '\\' + name_doc

if not os.path.isfile(full_name_doc):
    print('Такого файла не существует')
elif name_doc.endswith('.pdf'):
    pdf_process(full_name_doc)
elif name_doc.endswith('.doc'):
    doc_process(full_name_doc)
elif name_doc.endswith('.docx'):
    docx_process(full_name_doc)
elif name_doc.endswith('.djvu'):
    djvu_process(full_name_doc)
else:
    print('Неверное расширение файла ')
