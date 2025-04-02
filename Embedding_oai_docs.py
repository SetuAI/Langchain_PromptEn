'''
Here was pass in multiple statements for embedding purposes.
'''

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

'''
embed_documents : this function is used to embed multiple documents at once

'''

print(str(result))

'''
Look at the output closely. 
We have a 2d list inside which we have 3 lists. Each list represents list of vectors of the respective document.
After this,
If you want to understand how to perform "Document search with embeddings using Gemini"
Refer this colab link : https://colab.research.google.com/drive/1kXsyRhaUr2MPrV3mh7jIuT6jTypYfkUN?usp=sharing

'''