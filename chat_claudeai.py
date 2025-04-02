'''
The below is an example to create a basic chat model using Claude Anthropic
'''

from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model='claude-3-haiku-20240307') #in this code as well you can define temperature, max_tokens, etc.

# you can get the list of model names of Claude here:
# https://docs.anthropic.com/en/docs/about-claude/models/all-models

result = model.invoke('Can you tell me something about EY?')

print(result)
print(result.content)
