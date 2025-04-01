# create a dict and store student name in it
# it should be in text(str) format only, not any other
# pip install pydantic

from pydantic import BaseModel
# just how in typeddict we inherit TypedDict, in pydantic we inherit BaseModel

class Student(BaseModel):
    
    name: str # as of now defining only one attribute
    
# create a dict called new_student 
new_student = {'name':'Chirantan'}

# create an object of Student class and pass the new_student dict
student = Student(**new_student)

print(student)
# output : name='Chirantan'
# you can also fetch using the dot operator , for example print(student.name) will also give the same output

print(type(student))
# <class '__main__.Student'> : pydantic object

'''
Now do one thing, instead of 'name':'chirantan' , pass 'name':32
you will get an error , which is a validation check 
this was not available in TypedDict
'''

# In the next file pydantic_demo_optional.py, we will learn how to use pydantic with Optional 