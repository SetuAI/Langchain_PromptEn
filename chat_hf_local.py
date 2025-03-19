'''
We download the model from hugging face here locally
and then we interact with the model 
The speed is dependant on the hardware and the model size
'''

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

# be default , all the files are downloaded in C drive
# and hence we need to change the path to D drive

os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0', # repo id : you can copy paste from huggingface models page
    task='text-generation',
    pipeline_kwargs=dict( 
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)