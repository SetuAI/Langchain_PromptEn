# Email str
# there are certain things in pydantic with which we can perform validation 
# popular : email validation 

from pydantic import BaseModel,EmailStr
from typing import Optional

class User(BaseModel):
    
    org:str = 'ABCDEF' # default value
    years_of_exp : Optional[int] = None
    # the above means if there is no years_of_exp info explicitly mentioned , it will be None by default
    email : EmailStr # this will validate if the email is in correct format or not
    # EmailStr is a pydantic data type which will validate the email format
    
new_user = {'years_of_exp': 5 , 'email' : 'abc@gmail.com'}
# value is not a valid email address: for 'email':'abc'
# give correct email format : 'abc@gmail.com'

user_1 = User(**new_user)

print(user_1)
print(user_1.email)


# in the next file pydantic_FieldFunction.py, we will learn about Field function