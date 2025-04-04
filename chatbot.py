from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

'''
Langchain has 3 types of messsages :  (They are also called Static Messages. For dynamic messages we use ChatPromptTemplate)

System Message : a system level message you send to AI at the start of conversation.
(For ex, You are a helpful AI Assistant. You ask the user relevant questions and provide them with the information they need.)

Human Message : message that human sends to the system (For ex, "What is the capital of India?")
 
AI Message : message that AI replies to the human message (For ex, "The capital of India is New Delhi")

you can know more about them in the file messages.py

'''

load_dotenv()

model = ChatOpenAI()

# 1st message to Chat History , storing chat history
# chat history is a list of messages exchanged between human and AI
# each time user inputs a message, it is appended to the chat history

chat_history = [
    SystemMessage(content='You are a helpful AI Assistant. \
        You ask the user relevant questions and provide them with the information they need.')
]

while True:
    user_input = input('You: ')      # user input given
    chat_history.append(HumanMessage(content=user_input))  # user input converted to Human Message    
    if user_input == 'exit':       # to exit the chatbot, print "exit" and leave the chatbot env
        break
    result = model.invoke(chat_history)  
    chat_history.append(AIMessage(content=result.content)) # result converted to an AI Message
    print("AI: ",result.content)

print(chat_history)

'''
After exiting , you can check. Now our every interaction is labelled. If it is a system message, human message or AI message.
[SystemMessage(content='You are a helpful AI Assistant. You ask the user relevant questions and provide them with the information they need.', additional_kwargs={}, response_metadata={}), 
HumanMessage(content='hi ', additional_kwargs={}, response_metadata={}), 
AIMessage(content='Hello! How can I assist you today?', additional_kwargs={}, response_metadata={}), 
HumanMessage(content='what is your birth date? ', additional_kwargs={}, response_metadata={}),
AIMessage(content='I am an artificial intelligence and do not have a physical form or a birth date. I exist to assist you with information and tasks. How can I help you today?', additional_kwargs={}, response_metadata={}), HumanMessage(content='exit', additional_kwargs={}, response_metadata={})]
(base) 

'''

# After this you can visit chat_prompt_template.py to understand the concept of ChatPromptTemplate (dynamic messages) in Langchain.