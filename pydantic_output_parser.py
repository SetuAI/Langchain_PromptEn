'''

Pydantic Output Parser : 

Pydantic Output Parser is a structured output parser in langchain 
that use pydantic models to enforce schema validation when processing LLM responses. 

Now here, instead of schema you pass pydantic object
And since it is a pydantic object you can not only enforce schema but also perform data validation.
(Ensures that LLM responses follow a well defined structure.)



write a code :
define name person age and city : we want this in json from llm
constraint is age: int : greater than 18

'''


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    'we are creating pydantic object and hence inheriting from BaseModel'

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person') #gt = greater than 18
    city: str = Field(description='Name of the city the person belongs to')

# creating parser here
parser = PydanticOutputParser(pydantic_object=Person)


template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# defining the chain here
chain = template | model | parser


final_result = chain.invoke({'place':'sri lankan'})

print(final_result)


'''
Output :
name='Ranuka Fernando' age=25 city='Colombo'

you can see because we defined 'place':'sri lankan'}, it gave us
a sri lankan name and city in the output and age gt than 18.

-----------------------------------------------------

if you dont define chain and final_result (remove it)
and insert this code to check how the actual prompt looks in the backend

prompt = template.invoke({'place':'sri lankan'})
result = model.invoke(prompt)
print(prompt)

If you execute it , this is how the prompt looks like in the backend
text='Generate the name, age and city of a fictional sri lankan person \n The output should be formatted as a JSON instance that\
  conforms to the JSON schema below.\n\nAs an example, for the schema \
   {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}},\
    "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema.\
    The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n```\n\
    {"description": "we are creating pydantic object and hence inheriting from BaseModel", \
     "properties": {"name": {"description": "Name of the person", "title": "Name", "type": "string"},\
     "age": {"description": "Age of the person", "exclusiveMinimum": 18, "title": "Age", "type": "integer"},\
     "city": {"description": "Name of the city the person belongs to", "title": "City", "type": "string"}}, "required": ["name", "age", "city"]}\n```'

'''