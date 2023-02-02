from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship

from config.database import Base


class Director(Base):

    __tablename__ = "director"
    
    id = Column(Integer, primary_key = True)
    act_fname = Column(String)
    act_lname = Column(String)
