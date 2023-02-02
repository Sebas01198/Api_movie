from sqlalchemy import Column, ForeignKey ,Integer
from sqlalchemy.orm import relationship

from config.database import Base


class Genres(Base):

    __tablename__ = "movie_direction"
    
    dir_id = Column(Integer,ForeignKey('director.id'))
    mov_id = Column(Integer, ForeignKey('movie.id'))
    
