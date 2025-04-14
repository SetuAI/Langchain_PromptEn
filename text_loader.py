'''
first code in document loaders section
all document loaders are found in langchain_community package
text loaders .
'''

from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)


# deine a parser object : str output parser
parser = StrOutputParser()

# define a document loader object ,here text loader object
# encoding for special characters in the text file.
loader = TextLoader('cricket.txt', encoding='utf-8')

# loader object has load function, it will load the text file as a document in the memory
docs = loader.load()

print(docs)

print(type(docs)) # list

print(len(docs)) # as of now 1 document is loaded

print(type(docs[0])) # it is document data type

# document loaders have 2 components : page content and metedata , so printing page_content now
# this is the main text
print("Printing page content......\n ", docs[0].page_content)

# extracting metadata 
print("Printing metadata............\n ",docs[0].metadata)

# define a chain 
chain = prompt | model | parser

# instead of "poem", we send docs[0].page_content
print(chain.invoke({'poem':docs[0].page_content}))


'''
When the loadeer , loads the document, it is loaded as a list of documents.

After this we will learn pdf_loader.py
'''