from langchain_community.document_loaders import PyPDFLoader

# create a loader object
loader = PyPDFLoader('AI_TrainingPLan.pdf')

# this will create out set of document objects
docs = loader.load()

print("list of document objects........\n",docs) # list of document objects

print("length of the list.......\n",len(docs))

print("Extracting first document object.....\n",docs[0].page_content) # content of the 1st page

print("Printing metadata.......\n",docs[1].metadata) # when you scroll towards the end in output, what you see is metadata

'''
After this we learn about directory loader directory_loader.py
'''