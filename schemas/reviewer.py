from typing import Optional
from pydantic import BaseModel, Field


class Reviewer(BaseModel):
        rev_id: int
        rev_name: str

        class Config:
            schema_extra = {
                "example":{
                    "rev_id": 1,
                    "rev_name":"alec show",
                    
                }
            }
