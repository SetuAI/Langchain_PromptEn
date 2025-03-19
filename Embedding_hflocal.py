'''
Using hugging face open source model to generate embeddings
'''

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

vector = embedding.embed_documents(documents)

# Check the size (number of dimensions) of the vector
vector_size = len(vector[0])  # Get the length of the first vector

print(f"Number of documents: {len(vector)}")
print(f"Embedding vector size (dimensions): {vector_size}") # you can check the output is a 384 D vector

# Print a snippet of the first embedding vector (optional)
print(f"First 10 elements of the first embedding vector: {vector[0][:10]}")
# if you want for the 2nd document : vector[1][:10]