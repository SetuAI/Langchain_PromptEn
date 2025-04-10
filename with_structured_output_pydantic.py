
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field


# form a model  
model = ChatOpenAI(model="gpt-4o-2024-08-06")


# creating class Review which will inherit from BaseModel as this is pydantic
class Review(BaseModel):
    '''
    create attibutes 
    '''
    
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="Return a brief summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(description="Return the sentiment of the review either negative or positive or neutral")
    
   
    # we have imported Optional above  you can check
    pros: list[str] = Field(default=None, description="Write down all the pros discussed in the review in a list")
    cons : list[str] = Field(default=None,description="Write down all the pros discussed in the review in a list")
    name : Optional[str] = Field(default=None,description="Name of the reviewer")

    
    
structured_model = model.with_structured_output(Review)

#  we will pass in a complex review here ..we will also extract key themes, pros , cons ,etc
# also if certain things are not present, for example pros are listed , but cons are not, we keep them optional


result = structured_model.invoke("""The new Nova X Pro boasts stunning camera quality, capturing vibrant and detailed photos even in low light.\
                                   Battery life is exceptional, easily lasting a full day of heavy use.\
                                   While the phone's design is sleek, it feels a bit slippery in hand. \
                                   The user interface is intuitive and responsive, making navigation a breeze. \
                                   Overall, a solid flagship phone with a few minor drawbacks. Reviewed by Alex Thompson""")

print(result)
print(result.name)

# after this we will see how to work with json schema , go to json_schema.json
# there we will understand how to create json schema 