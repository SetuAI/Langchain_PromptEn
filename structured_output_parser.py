'''
StructuredOutputParser : 

It is an output parser which helps extract structured JSON data from the LLM responses
based on "predefined field schemas".
The difference between this parser and JSON output parser is that you define the schema here
you tell the LLM that this is particularly how you want to structure of the response to be.

It works by defining a list of fields (ResponseSchema) 
that the model should return, ensuring
the output follows a structured format. 
'''

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# create a schema using ResponseSchema class objects
# 
schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

# define the parser
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)


'''
Output :

{'fact_1': 'Black holes are regions of spacetime where gravity is so strong that nothing, not even light, can escape.', 
'fact_2': 'They form when massive stars collapse at the end of their lifespans.', 
'fact_3': 'Black holes can have different sizes, from tiny stellar-mass black holes to supermassive black holes at the centre of galaxies.'}

So , what is the disadvantage ?

You cannot do data validation here in structured output parser.

This can enforce schema , which is great , but no data validation .

And that is where Pydantic Output Parser comes into play . 

you can go to pydantic_output_parser.py
'''