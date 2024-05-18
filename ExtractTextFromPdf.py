from pypdf import PdfReader
reader=PdfReader('DW.pdf')
print(len(reader.pages))
page=reader.pages[46]
text=page.extract_text()
print(text)
