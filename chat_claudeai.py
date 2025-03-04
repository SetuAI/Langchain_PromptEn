

from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model='claude-3-7-sonnet-20250219')

# you can get the list of model names of Claude here:
# https://docs.anthropic.com/en/docs/about-claude/models/all-models

result = model.invoke('Can you tell me something about EY?')


print(result.content)
