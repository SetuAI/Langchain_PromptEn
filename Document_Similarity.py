'''
Document Similarity Search :

Say we have 5 documents. 
User asks a question and that question will be related to one of the documents we have.
We need to find, which document does the question belong to .

To tackle this, we generate embeddings for all the documents and store it. [5 documents : 5 embedding vectors]
After that, we generate embedding vectors for the question as well. [1 question : 1 embedding vector]
As of now imagine 5 documents are of 300 D vectors

And now you have new question vector. 
Now we need to find : How close is this newly added vector to the existing 5 document vectors ? 
So we take Cosine Similarity , which gives a score between 0 and 1.
Higher the score, more similar the vectors are.
This principle is the same as what is used in RAG based applications.


Cosine similarity measures the angle between two vectors; a value of 1 means the vectors are perfectly aligned (very similar), 
and a value of -1 means they are perfectly opposite (very dissimilar). A value of 0 indicates orthogonality (no similarity).
 
 
'''


from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', 
                             dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'Tell me somthing about Bumrah.' 

# we extract document embeddings
doc_embeddings = embedding.embed_documents(documents)

# then we extract query embeddings
query_embedding = embedding.embed_query(query)

# we calculate cosine similarity between query vector and document vectors
# first sent a query embedding vector as a 2D list and then document embeddings as a 2D list
scores = cosine_similarity([query_embedding], doc_embeddings)[0] #[0] extracts the first row of the result.
print("Similarity scores obtained: ", scores)


# enumerrate will give an index position to every score obtained and then we sort the scores
index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]


'''
Info : 
If scores is [0.8, 0.2, 0.5], enumerate(scores) will generate (0, 0.8), (1, 0.2), (2, 0.5), and so on.
Which means : Document 0 has a score of 0.8 etc.. 

list(enumerate(scores)): This converts the iterator into a list of (index, score) tuples. For example: [(0, 0.8), (1, 0.2), (2, 0.5)]

key=lambda x: x[1] tells sorted() how to sort the tuples. lambda x: x[1] is a small, anonymous function (a "lambda function") 
that takes a tuple x as input and returns its second element (the element at index 1), which is the score.

In other words, the sorted() function will look at the second element of each tuple (the score) to determine the sorting order.
It sorts the list from lowest score to highest score.

For example, if we sort [(0, 0.8), (1, 0.2), (2, 0.5), (3, 0.9)] using key=lambda x: x[1], the result will be:
[(1, 0.2), (2, 0.5), (0, 0.8), (3, 0.9)] (The tuples are now ordered by score from lowest to highest)

[-1]: This accesses the last element of the sorted list, which will be the (index, score) tuple with the highest score (the most similar document).
Since the list is sorted from lowest to highest score, the last element will be the tuple with the highest score (the most similar document).

In our example, [(1, 0.2), (2, 0.5), (0, 0.8), (3, 0.9)][-1] will give us (3, 0.9)

'''

print("Query given was:", query)
print("Content which was most similar to the query:", documents[index])
print("Similarity score is:", score)