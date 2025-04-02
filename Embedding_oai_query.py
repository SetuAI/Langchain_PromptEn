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
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
embedding = OpenAIEmbeddings(model='text-embedding-3-small', 
                             dimensions=32,api_key= api_key) # number of dimensions in the output vector 
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


'''
Output : 
[-0.043329671025276184, -0.06875734776258469, 0.2922092080116272, 0.4001533091068268, 0.007820245809853077, 
0.20904666185379028, -0.15857139229774475, 0.3965044915676117, -0.13067317008972168, 0.04808073118329048, 
0.08483493328094482, -0.10414324700832367, 0.0894719660282135, -0.23686887323856354, 0.16419664025306702,
0.23686887323856354, -0.04435589909553528, 0.08620323985815048, -0.1714942753314972, -0.0015678498893976212, 
0.08605120331048965, 0.13827486336231232, -0.10657578706741333, 0.2149759829044342, 0.203269362449646,
-0.1725585162639618, -0.08817967772483826, 0.04960107058286667, -0.06446238607168198, -0.12101901322603226, 
0.29555395245552063, -0.1635885089635849] 


After this,
If you want to understand how to perform "Document search with embeddings using Gemini"
Refer this colab link : https://colab.research.google.com/drive/1kXsyRhaUr2MPrV3mh7jIuT6jTypYfkUN?usp=sharing
'''