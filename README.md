# Langchain_PromptEn


1. chat models
2. embedding models 
3. prompt templates (start with promptui.py,prompt_generator.py,prompt_reuse.py)
4. messages (chatbot.py,messages.py,chat_prompt_template.py)
5. message placeholder (message_placeholder.py)
6. structured outputs
7. Output Parsers (stroutputparser001.py,stroutputparser_hf.py, stroutputparser1.py,jsonoutputparser1.py,
   structured_output_parser.py, pydantic_output_parser.py)
8. Chains (simple_chain.py,sequential_chain.py, parallel_chain.py,conditional_chain.py)
9. Components in RAG : Document Loaders (text_loader.py,pdf_loader.py)

-----------------------------------------------------------------------------------------------------

repo contains some codes and understanding on Langchain implementation

We have created some chat models using Gemini, Claude and Open AI just to get an understanding.

You can download open source pre trained models as well. (No API dependancy)
You can finetune it , deploy it etc.
You can gte it from : https://huggingface.co/models 
Some Text Generation models : https://huggingface.co/models?pipeline_tag=text-generation&sort=trending
You can use Hugging Face Inference API 

For running open source models : they are compute intensive which can be a drawback


What are Embeddings?

Embeddings are numerical representations of text (or other data types) that capture the semantic meaning of the text. 
In other words, they transform words, phrases, or documents into vectors (lists of numbers) in a high-dimensional space. 
The closer two embeddings are to each other in this space, the more semantically similar the corresponding pieces of text are.

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
Here, you define how will your output dictionary look like. For example, the output should be like {"Name":"ABC" , "age":"twenty-five"}
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

Note : Output Parser can work with LLM that can and cannot generate JSON.

Output parsers in langchain help convert raw LLM responses into structured formats like 
JSON, csv, pydantic models and more. They ensure consistency, validation and ease of use in applications. 

Output parser types : 
stroutput parser
jsonoutput parser
pydantic output parser
csv output parser
etc...

-------------------------------------------------

StrOutputParser :

It's job is simple, It takes the LLM response and converts it into a string.

why and when is it useful ? 

for example ,
talk to your llm twice. 
Give one topic to LLM and we want LLM to give detailed report on that topic. (ex : "detailed report on blackholes")
Once you get the detailed report, resend this report to LLM and ask it to summarize the report in 5 lines .

do compare when you use 1.result.content  and  2.StrOutputParser 
(refer stroutputparser.py file)



-------------------------------------------------

JSONOutputParser:

It forces the LLM to generate the output in JSON format. 

-------------------------------------------------

StructuredOutputParser : 

It is an output parser which helps extract structured JSON data from the LLM responses
based on "predefined field schemas".
The difference between this parser and JSON output parser is that you define the schema here
you tell the LLM that this is particularly how you want to structure of the response to be.

It works by defining a list of fields (ResponseSchema) that the model should return, ensuring
the output follows a structured format. (refer structured_outputparser.py file)


-------------------------------------------------

Pydantic Output Parser : 

Pydantic Output Parser is a structured output parser in langchain 
that use pydantic models to enforce schema validation when processing LLM responses. 

Now here, instead of schema you pass pydantic object
And since it is a pydantic object you can not only enforce schema but also perform data validation.
(Ensures that LLM responses follow a well defined structure.)

-------------------------------------------------

CHAINS : 
With the help of chains we can create a pipeline of Prompt designing, sending it to model 
and getting output etc.

Types of chains :
1. Sequential Chain.
2. Parallel Chain.
3. Conditional Chain.

Before this we will create a simple chain (simple_chain.py)

Sequential Chain : 
Ask for a topic from the user

-----------------------------------------------------------------------------------------------------------

 Document Loaders : https://python.langchain.com/docs/concepts/document_loaders/

 Using langchain building RAG based applications

 RAG is a technique that combines information retrieval with language generation
 where a model retrieves relevant documents from a knowledge base and then uses
 them as context to generate accurate and grounded responses.

Benefits of using RAG : 
Use of up-to data information
Better privacy
No limit of document size.

Important components in a RAG :
Document Loaders
Text Splitters
Vector Databases
Retrievers 
All these 4 components together build a RAG system.
Start with learning Document Loaders -- 

-----------------------------------------------------------------------------
Document Loaders : 
Mostly used ones are Document Loaders : TextLoader, PyPDFLoader, WebBaseLoader, csvLoader

DC are components in Langchain used to load data from various sources into standardized format
usually as document objects, which can be used for chunking, embedding, retrieval and generation.
Data can come from multiple sources from PDFs to s3 to DB.
We need to make sure, when data comes from any source , it should come in common standard format.
This standardised format is called Document or Document object in langchain .

Now, the standard format of a document object is: 

Document(
    page_content = "The actual text content",
    metadata = {"source":"filename.pdf",...}
)


1. Text Loader: simplest document loader.
It reads plain text (.txt files) and converts them into langchain document objects.

Use case : 
For log file processing, or video transcript processing.

Limits : 
Only works with .txt files.
"Now refer text_loader.py file"


2. PyPDF Loader : 
It reads the pdf file and converts them into document object.
It runs on page-by-page basis.
So in short, for 25 pager document it creates 25 pypdf document objects.
So after that, you will have list of 25 document objects.
So now, every Document object will have its own page_content and metadata.

Structure looks something like this : 

[
    Document(page_content = "Text from page 1 of pdf", metadata = {"page": 0,
                                                                    "source":"file.pdf"}),
    Document(page_content = "Text from page 2 of pdf", metadata = {"page": 1,
                                                                    "source":"file.pdf"}),  
    .........                                                             
]

PyPDF loader internally uses PyPDF library.
Not that great for complex pdf structures or scanned ones. 
Better for plain text pdfs. 
"Refer pdf_loader.py".

Which PDF loaders to prefer ? 

Simple, clean PDFs --- > PyPDFLoader
PDFs with tables/columns  ---> PDFPlumberLoader
Scanned/Image PDFs ---> UnstructuredPDFLoader ot AmazonTextractPDFLoader
Need layout and image data --->  PyMuPDFLoader
Want best structure extraction ---> UnstructuredPDFLoader

Refer this link for in depth document loaders :https://python.langchain.com/docs/integrations/document_loaders/