# %%
import PyPDF2								 # Importing required modules
# %%
pdfFileObj = open('sample.pdf', 'rb')       # creating a pdf file object
# %%
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # creating a pdf reader object
# %%
print(pdfReader.numPages)                    # printing number of pages in pdf file
# %%
pageObj = pdfReader.getPage(0)               # creating a page object
# %%
print(pageObj.extractText())                 # extracting text from page
# %%
pdfFileObj.close()                           # closing the pdf file object