import pyttsx3
import pdfplumber
import PyPDF2

file_path = 'D:/DATA SCIENCE AND MACHINE LEARNING/ISLR.pdf'

pdfFileObj = open(file_path, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pages = pdfReader.numPages

with pdfplumber.open(file_path) as pdf:

    for i in range(pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
