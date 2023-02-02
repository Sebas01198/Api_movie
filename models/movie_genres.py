from sqlalchemy import Column, ForeignKey ,Integer
#from sqlalchemy.orm import relationship

from config.database import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MovieGenres(Base):

    __tablename__ = "movie_genres"

    id =  Column(Integer, primary_key = True)
    mov_id = Column(Integer, ForeignKey('move.id'))
    gen_id = Column(Integer, ForeignKey('genres.id'))
