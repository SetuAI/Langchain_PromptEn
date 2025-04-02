'''
Chat Models : 

Here we are building a chat model using a combination of langchain and open ai 
we are using gpt-4o model from open ai as chat model

All chat models inherit from base chat model

To check which chat models are available : platform.openai.com/docs/models

'''

from langchain_openai import ChatOpenAI # you can press ctrl and click : goes to source code
from dotenv import load_dotenv # .env is where secret keys get stored (API store)
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model='gpt-4o', # model to be communicated with 
                   max_completion_tokens=None, #"None" ensures we explicitly dont put any limit on the output length 
                   openai_api_key=api_key)

result = model.invoke("Can you tell me something about San Francisco ? ")

'''
2 ways to visualize the output:

print(result) : this gives output as well some other metadata like total tokens, input tokens, etc

print(result.content) : this only extracts the content of the output and not the metadata (filtered output)
'''
# print(result)
print(result)


'''
in case you want to export the output to model to a text file, use this after print(result.content)

with open("model_output.txt", "w") as file:
    file.write(result.content)

'''