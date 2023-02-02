from typing import Optional
from pydantic import BaseModel, Field


class Actor(BaseModel):
        gen_id:int
        gen_title:str

        class Config:
            schema_extra = {
                "example":{
                    "gen_id": 1245,
                    "gen_title":"Comedy",
                    
                }
            }
