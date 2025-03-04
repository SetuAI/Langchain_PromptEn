from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

'''

'''
load_dotenv()

model = ChatOpenAI()

# list of messages : Chat history 
messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me  something about LangChain framework in LLMs.')
]

# invoking the model and sending the messages we defined above
result = model.invoke(messages)

# extracting and appending the result content to the messages list and make that an AI message
messages.append(AIMessage(content=result.content))

# printing the entire Chat History
print(messages)

'''
We now integrate this in chatbot.py

'''