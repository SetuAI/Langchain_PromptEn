# Langchain_PromptEn


1. chat models
2. embedding models 
3. prompt templates (start with promptui.py,prompt_generator.py,prompt_reuse.py )
4. structured outputs

repo contains some codes and understanding on Langchain implementation

We have created some chat models using Gemini, Claude and Open AI just to get an understanding.

You can download open source pre trained models as well. (No API dependancy)
You can finetune it , deploy it etc.
You can gte it from : https://huggingface.co/models 
Some Text Generation models : https://huggingface.co/models?pipeline_tag=text-generation&sort=trending
You can use Hugging Face Inference API 

For running open source models : they are compute intensive which can be a drawback


What are Embeddings?

Embeddings are numerical representations of text (or other data types) that capture the semantic meaning of the text. In other words, they transform words, phrases, or documents into vectors (lists of numbers) in a high-dimensional space. The closer two embeddings are to each other in this space, the more semantically similar the corresponding pieces of text are.

Some Links : 
https://python.langchain.com/docs/integrations/chat/openai/

https://www.youtube.com/watch?v=HdcLE8JuMrA


Message Placeholder : 
A Message Placeholder in Langchain is a dynamic placeholder which is used inside a ChatPromptTemplate to 
dynamically insert a chat history or a list of messages at runtime.

---------------------------------------------------------------------------------------------------------------------
### What is unstructured output ? 

When we converse with an LLM, we get textual output - that is an unstructured output. (Free-form text)
For example, you ask chatgpt : what is the capital of India ? Output : New Delhi. (Text output : Unstructured - plain and simple)



### What is structured output ? 

Json output format, instead of plain text. 
For example, imagine a dictionary . 
When the output response from the LLM, follows a structure , it will be termed as Structured output.

For example, you ask chatgpt : Can you create a one-day travel itenerary to Eiffel Tower ?

Json enforced output : 

[
 {"time": "Morning" , "activity":"Visting Eiffel Tower"},
 {"time": "Afternoon" , "activity":"Lunch at a nearby restaurant"},
 {"time": "Evening" , "activity":"Watching the sunset"},
]

This is an example of Structured output , if you see time and activity is categorized neatly. 

Advantage of Strucutured output : you can easeily integrate this with other LLM systems.


Use case for Structured output : 

Data Extraction : Let's say you want to store the response extracted from LLMs in a db.
For example, you are creating a job portal. And you want to extract certain key attributes
like "Previous Work-Ex" , "Year of Graduation" , etc in a seperate db.
This is where you can use Structured output. (json info ---> db)

API building : For example, you work for BookMyShow.
Customers often write movie reviews , which are "Textual" , which means "Unstructured".
You can write code to extract key information from the review like : "Actor" , "Movie" , "Sentiment", etc 
and store them efficiently. And then you create an endpoint for people to use it.

-------------------------------------------------------------------------------------------------------------

Now be default, some LLMs can generate structured outputs (ex :ChatGPT, Gemini,Claude, etc) and some cannot.

If we consider the LLMs which can generate the structured ones , we can use a function 
called with_structured_output to extract it.

If we take LLMs which cannot generate structured output , then we can use something called
Output Parsers.

------------------------------------------------------------------------------------
Now before doing model.invoke() in langchain , we need to specify the datat_format to be used with with_structured_output.

There are 3 types of data_format options : TypedDict, json_schema, Pydantic.

1. TypedDict :
Here, you define how will your output dictionary look like. For example, the output should be like {"Name":"ABC" , "age":"25}
Here, you ensure dictionary follows a specific structure. What keys and values should go in there.
The only loophole here, is that there is no validation.
Which means if I want age:int , which means I expect the output of age in int format
but if another developer defines age:str , when there will be no hardblock and TypeDict will let it execute without error.
So please note, TypeDict, only helps you define the output format without any guardrails.

2. Pydantic :
Pydantic is data validation and data parsing library for python. It ensures that the data you work with is
correct, structured and type-safe.
If you want to put a check on your data if it is matching certain criteria or not, in that case, you can use Pydantic.
For example, while building APIs.(it should be right type, right format, etc.)

-----------------------------------------------------------------------------------------------------------

When working with_structured_output , then you can tell by which method you want the structured output
you have "method" parameter .
In this , you can set 2 values : json mode and function calling.

json mode to be used when you want the structured output in json format only.
function calling to be used when you want to call a particular function.

If working with open ai models, you use function calling.
when working with claude gemini , prefer json mode.
Many hugging face models dont support json mode and function calling, and that is when we use "Output Parsers".

-------------------------------------------------------------------------------------------------------------------

Output Parsers : 

Certain LLMs are fine tuned in such a way, they will give structured output in response. 
In langchain we use with_structured_output function here. 

Certain LLMs can't. 
This is where we prefer using output parsers.

Output parsers in langchain help convert raw LLM responses into structured formats like 
JSON, csv, pydantic models and more. They ensure consistency, validation and ease of use in applications. 

Output parser types : 
stroutput parser
jsonoutput parser
structured output parser
pydantic output parser
csv output parser
etc...

-------------------------------------------------
StrOutputParser : 
It takes the LLM response and converts it into a plain string.
