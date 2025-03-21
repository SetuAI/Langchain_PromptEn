from typing import TypedDict

# we will create  a class Person : will inherit from TypedDict


class Person(TypedDict):
    
    name : str
    age : int
    
# create a new dictionary new_person on the above format

new_person : Person = {'name':'John',
                       'age': 25}

print(new_person) # {'name': 'John', 'age': 25}

'''
output: 
$ python typedict_demo.py                                                                                                                                                                                                           
{'name': 'John', 'age': 25}
'''

##################################################################################

# how to create data_format with TypedDict and create structured output
# Lets take some reviews, push it to LLM and output should be in dict format
# {summary: str, sentiment: str} , and then extarct summary and sentiment from the dict

# you can find this code in with_structured_output_typeddict.py