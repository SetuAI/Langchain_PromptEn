
'''
Creating a chat model using Google Gemini
You can get the API key from aistudio.google.com

'''

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

result = model.invoke('Can you tell me something about EY?')

print(result.content)