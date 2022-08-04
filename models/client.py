from pydantic import BaseModel

class Client(BaseModel):
   id: int
   name: str
   description: str

   class Config:
     schema_extra = {
        "example": {
            "name": "Recruitement",
            "description": "A recruitement system"
        }
     }


def get_clients():
 pass