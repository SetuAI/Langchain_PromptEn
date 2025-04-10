'''
Sequential Chain : 
Ask for a topic from the user. 
User will provide a topic.
Then we will send the topic to the LLM with prompt asking for detailed report.
Then the LLM generated detailed report output will be sent back to the LLM 
and we will create 2nd prompt "to extract 5 most important points from this report".

You can see we are forming a sequential chain of prompts.

'''

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# creating prompt 1
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

# creating prompt 2 which will take the output of prompt 1 and generate a summary
prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

# choosing string ouptput parser
parser = StrOutputParser()

# creating a chain
chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Influencer led brands and their adoption.'})

print(result)

chain.get_graph().print_ascii()

'''
After this we will learn how to work with parallel chains
where you can connect multiple chains in parallel instead of sequential pattern. Refer parallel_chain.py
'''