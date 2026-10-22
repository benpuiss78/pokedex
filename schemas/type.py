from pydantic import BaseModel

class Type(BaseModel):
    id : int
    name : str
    name_fr : str