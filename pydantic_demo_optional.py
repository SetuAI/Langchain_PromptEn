# just how we saw in typeddict , we can also use it with pydantic.
# it I want to extract some info and you dont know if that is present or not, you use optional

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    
    org:str = 'ABCDEF' # default value
    years_of_exp : Optional[int] = None
    # the above means if there is no years_of_exp info explicitly mentioned , it will be None by default
    
new_user = {'years_of_exp': 5}

user_1 = User(**new_user)

print(user_1)

'''
Now the output will be: 

org='ABCDEF' years_of_exp=None

Alternatively, you can also pass in the years_of_exp info and then check, 
pas sit in new_user = {'years_of_exp': 5} and then check 

'''