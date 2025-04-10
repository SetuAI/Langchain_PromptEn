'''
Create an application : 

User gives us a feedback .
Take this feedback and analyse the sentiment of the feedback.
If the sentiment is positive, then we will say "Thank you for the kind words".
If the sentiment is negative, then we will say "Sorry to hear that. We will try to improve".

Now this is not a fresh application . 

But it will be great, if it will be agentic.
For ex, if the sentiment is positive, the agent will give feedback form to the user and ask
for rating them 5 stars .

If negative, then the agent will send an email to customer support executive and then he/she
will connect with the customer to discuss the issue.

We will learn agentic stuff soon .

As of now we will focus on creating conditional chain .

User gives feedback : we will send this to the model .
The job of the model is to analyse the sentiment of the feedback : psitive or negative ? 
Based on whether the feedback is positive or negative, we will take action.
Means, we will ask the model only to generate response as per the feedback.

Now here only one part is executed in conditional chain , unlike parallel chains.

'''

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

# creating 2nd parser
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# creating prompt 1 
prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

# we are classifying here : 
classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a quite an amazing smart phone'}))

chain.get_graph().print_ascii()