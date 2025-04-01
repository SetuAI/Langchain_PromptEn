# Field function 
# With Field function we can set default values, contstraints, and metadata for the fields in the model.
# with this we also define description constraint which suggests what is the field about
# Description is same as Annotated we used in TypeDict which use to do hinting, tell what is the attribute about

# add one more attribute employee_rating and put a constraint on it that the value should be between 0 and 10
from pydantic import BaseModel,EmailStr, Field
from typing import Optional

class User(BaseModel):
    
    org:str = 'ABCDEF' # default value
    years_of_exp : Optional[int] = None
    # the above means if there is no years_of_exp info explicitly mentioned , it will be None by default
    email : EmailStr 
    # this will validate if the email is in correct format or not
    employee_rating : float = Field(gt=0, le=10,description="Represents employee annual rating from Jan to Dec") 
    # empoyee_rating is float type and set to Field function and in field set constraint
    # gt = greater than 0, le = less than equal to 10
    # this will validate if the employee_rating is between 0 and 10
    
    
new_user = {'years_of_exp': 5, 
            'email' : 'abc@gmail.com', 
            'employee_rating' : 8.5}
# set the employee_rating out of range and check , it will throw error.

user_1 = User(**new_user)

print(user_1.employee_rating)

"""
to convert to dictionary or json format

print(dict(user_1))

or 

user_dict = dict(user_1)
print(user_dict['employee_rating'])

for json :

user_json = user_1.model_dump_json()
print(user_json)
"""

# in the next file with_structured_output_pydantic.py, we will learn how to generate structured output using pydantic