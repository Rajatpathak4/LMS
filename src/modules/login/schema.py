from pydantic import BaseModel


class LoginUser(BaseModel):
    user_id : str
    password: str
    
