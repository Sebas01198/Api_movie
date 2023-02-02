from sqlalchemy import Column, ForeignKey ,Integer, String, Float,Date
from sqlalchemy.orm import relationship

from models.moviecast import MovieCast
from config.database import Base


class Reviewer(Base):

    __tablename__ = "reviewer"
    
    id = Column(Integer, primary_key=True, index=True)
    rev_name =  Column(String)
    

 
