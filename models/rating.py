from sqlalchemy import Column, ForeignKey ,Integer, String, Float,Date
from sqlalchemy.orm import relationship

from models.moviecast import MovieCast
from config.database import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Rating(Base):

    __tablename__ = "rating"
    id = Column(Integer, primary_key= True)
    mov_id = Column(Integer, ForeignKey('movie.id'))
    rev_id = Column(Integer, ForeignKey('reviewer.id'))
    rev_stars = (Integer)
    num_o_ratings = (Integer)
    
    
    
    