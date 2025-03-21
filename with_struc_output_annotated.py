
'''
Annotated : 
Annotated is when you want to guide the llm in short. 
Firstly you import Annotated from typing
Then you create Annotated definition in the class

for example , summary :Annotated[str, "a brief summary of the review"]
you are sharing exactly what you want the llm to do with the summary attribute
'''

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict,Annotated,Optional,Literal


# form a model 
model = ChatOpenAI()


# creating class Review which will inherit from TypedDict
class Review(TypedDict):
    '''
    create 2 attributes in the class : summary : str and sentiment : str
    '''
    summary: Annotated[str , "Return a brief summary of the review"]
    sentiment: Annotated[str , "Return the sentiment of the review either negative or positive or neutral"]
    # we extract key themes as a list of strings
    key_themes: Annotated[list[str] , "Write down all the key themes discussed in the review in a list"]
    # pros are optional, which means they may or may not be present in the review, so we keep them optional
    # we have imported Optional above  you can check
    pros: Annotated[Optional[list[str]] , "Write down all the pros discussed in the review in a list"]
    cons: Annotated[Optional[list[str]] , "Write down all the cons discussed in the review in a list"]
    name : Annotated[Optional[str] , "Name of the reviewer"]

    
    
structured_model = model.with_structured_output(Review)

#  we will pass in a complex review here ..we will also extract key themes, pros , cons ,etc
# also if certain things are not present, for example pros are listed , but cons are not, we keep them optional


result = structured_model.invoke("""The Chrono-Comm, a wristwatch communicator straight out of science fiction, presents a fascinating blend of innovation and frustration. Its sleek, minimalist design is a head-turner, and the holographic interface is incredibly intuitive, offering a seamless experience for calls, messaging, and even video chat. The built-in AI assistant, "Chronos," proves surprisingly helpful with scheduling and information retrieval, though it occasionally exhibits quirky personality traits. However, the device's Achilles' heel is its abysmal battery life, barely lasting a single day with moderate use. While the universal translator function works remarkably well, accurately converting speech in real-time, voice commands are frequently misinterpreted, leading to frustrating errors. Durability is also a concern; the holographic screen scratched easily during testing. The Chrono-Comm offers a tantalizing glimpse into the future of personal communication, but significant improvements are needed, particularly in battery life and robustness, before it can truly live up to its potential. It’s a stylish and innovative device, but its practicality is severely hampered by these significant shortcomings. A promising concept, undoubtedly, but one that needs further refinement before achieving mainstream appeal. Review by Chirantan Lonkar""")

print(result)
print(result['summary'])
print(result['sentiment'])
print(result['key_themes'])
print(result['name'])