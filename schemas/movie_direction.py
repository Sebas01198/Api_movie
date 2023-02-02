from typing import Optional
from pydantic import BaseModel, Field


class Movie_direction(BaseModel):
        dir_id: int
        mov_id: int
        
        class Config:
            schema_extra = {
                "example":{
                    "dir_id": 123,
                    "mov_id": 1234,
                    
                }
            }
