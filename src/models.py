import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usersname = Column(String(250), nullable=False)
    name = Column(String(150), nullable=False)
    lastname = Column(String(150), nullable = False)
    email = Column(String(180), nullable = False)
      

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    

class Characters(Base):
    __tablename__ ='characters'   
    id = Column(Integer, primary_key=True)
    Character_name = Column(String(150)) 
     

class Favorite(Base):
    __tablename__ = 'favotrite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    user = relationship(User)
    planet = relationship(Planets)
    character = relationship(Characters)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
