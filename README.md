# Langchain_PromptEn
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