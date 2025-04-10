from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict


# form a model 
model = ChatOpenAI(model="gpt-4o-2024-08-06")

# now first we create a schema which shows the structure of the output format

# creating class Review which will inherit from TypedDict
class Review(TypedDict):
    '''
    create 2 attributes in the class : summary : str and sentiment : str
    '''
    summary: str
    sentiment: str
    name: str
    
structured_model = model.with_structured_output(Review)

# invoke the strucutred_model to extract structured output : json 

result = structured_model.invoke("""Music and cinematography are the two biggest highlights of Gowri. The medley song, and a touching tribute to Gowri Lankesh in the first half are memorable. Muddada and Time Barrutte in the second half are refreshing. The film’s cinematography is at its finest as it offers a visual feast, showcasing some of the best locations, in various seasons, throughout Karnataka and a bit of Mumbai.Review given by author Chirantan""")

print(result)

'''
output is a dictionary
{'summary': 'Music and cinematography are the biggest highlights of Gowri', 'sentiment': 'positive'}
'''

# for open you can check which models support structured output
# link : https://platform.openai.com/docs/guides/structured-outputs?api-mode=chat

# since this is dictionary, you can also individually access the values
print(result['summary'])
print(result['sentiment'])
print(result['name'])

'''
In the next file " with_struc_output_annotated : we will learn how Annotated works in Typeddict
'''