# in the chains module this is the first file
# we start with implementing a simple chain

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 10 interesting facts about this {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

# StrOutputParser gives output in string format 
parser = StrOutputParser()

# create a chain
chain = prompt | model | parser # parser will parse the metadata and only show us result.content

result = chain.invoke({'topic':'cricket'})

print(result)

# visualize the chain using get_graph function
chain.get_graph().print_ascii()