'''
Here we learn to interact with Embedding models using langchain
Embedding is the process of convert tokens to vectors
you can go to open ai and see the full list of embedding models

The principle is simple :
Bigger the vector size, higher contextual information is captured
Smaller the vector size, lower contextual information is captured
'''

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', 
                             dimensions=32) # number of dimensions in the output vector 
# bigger dimensions are used in capturing more information about the token
# small dimensions are used in capturing less information about the token and cost effective

result = embedding.embed_query("EY is a global professional services organization") # embed a single query
# for multiple queries we use another syntax

print(str(result))

# you can check the ouput which generates a list of vectors in 32 dimensions. (32-D vectors)
# this 32-D vector represents the contextual meaning of the input text we provided
# you can also change the dimensions and check the output

# by default, the length of embedding vector you can take for small embedding is 1536 (text-embedding-3-small)
# and 3072 for larger embedding models (text-embedding-3-large)

