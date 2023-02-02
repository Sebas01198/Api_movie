from sqlalchemy import Column, ForeignKey ,Integer, String, Float,Date
from sqlalchemy.orm import relationship

from models.moviecast import MovieCast
from config.database import Base


class Genres(Base):

    __tablename__ = "genres"
    
    id = Column(Integer, primary_key = True)
    gen_title = Column(String)

    