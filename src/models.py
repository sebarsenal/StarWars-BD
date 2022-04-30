import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))


class Naves(Base):
    __tablename__ = 'Naves'
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    manufacturer = Column(String(250))


class Planetas(Base):
    __tablename__ = 'Planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    population = Column(Integer)
    gravity = Column(String(250))


class Personajes(Base):
    __tablename__ = 'Personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    estatura = Column(Integer)
    colorOjos = Column(String(250))


class Favoritos_Pj(Base):
    __tablename__ = 'Favoritos_Pj'
    idFav = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('User.id'))
    id_pj = Column(Integer, ForeignKey('Personajes.id'))
    User = relationship(User)
    Personajes = relationship(Personajes)


class Favoritos_PL(Base):
    __tablename__ = 'Favoritos_PL'
    idFav = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('User.id'))
    id_pl = Column(Integer, ForeignKey('Planetas.id'))
    User = relationship(User)
    Planetas = relationship(Planetas)


class Favoritos_Nv(Base):
    __tablename__ = 'Favoritos_Nv'
    idFav = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('User.id'))
    id_nv = Column(Integer, ForeignKey('Naves.id'))
    User = relationship(User)
    Naves = relationship(Naves)


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
