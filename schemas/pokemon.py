from pydantic import BaseModel

class Pokemon(BaseModel):
    number : int
    name : str
    name_fr : str
    types : list[str]
    image_url : str
    height : int
    weight : int
    evolves_from_number : int