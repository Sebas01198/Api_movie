from typing import Optional
from pydantic import BaseModel, Field


class Director(BaseModel):
       id: int
       dir_fname: str = Field(max_length=15,min_length=3)
       dir_lname: str = Field(max_length=15,min_length=3)
        
        
       class Config:
           schema_extra = {
               "example":{
                   "id": 1,
                   "dir_fname":"Alfred",
                   "dir_lname":"Hitchcock"    
               }
           }