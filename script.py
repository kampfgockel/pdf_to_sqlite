# This script parses a PDF and saves each page as a row in a sqlite database in the same folder
import PyPDF2	
from sqlalchemy import create_engine
import pandas as pd							
pdfFileObj = open('sample.pdf', 'rb')
engine = create_engine('sqlite:///db.sqlite3')       
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

df = pd.DataFrame(columns=['page','text'],)
for page in range(pdfReader.numPages):
    strPage = pdfReader.getPage(page).extractText()
    df.loc[page] = [page, strPage]

pdfFileObj.close() 
df.to_sql('pages', con=engine)
dfOne = pd.read_sql_table('pages', engine)
print(dfOne.head())

