'''
This explains how to define a dynamic chat prompt template in lagnchain.
Where in you dont define a single prompt, but a series of prompts which are dynamic in nature.
'''

from langchain_core.prompts import ChatPromptTemplate


# forming chat template by creating object of ChatPromptTemplate
chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'), # system message - dynamic 
    ('human','Explain in simple terms, what is {topic}')  # human message  - dynamic
])

prompt = chat_template.invoke({'domain':'Cricket',
                               'topic':'Dusra'})

print(prompt)