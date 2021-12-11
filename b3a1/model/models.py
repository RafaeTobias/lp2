from enum import unique
from typing import Text
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Float, Time

Base = declarative_base()

class Usuario(Base):

    __tablename__ = 'b3a1_usuario'

    id = Column(Integer, primary_key=True)
    login = Column(String(64), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)
    
    def _repr_(self):
        return f'Usuario {self.login}'

class Atividade(Base):

    __tablename__ = 'b3a1_atividade'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    data = Column(Date, nullable=False)
    inicio = Column(Time, nullable=False)
    final = Column(Time, nullable=False)
    local = Column(String(45), nullable=False)
    tipo = Column(String(45), nullable=False)
    quilometragem = Column(Float, nullable=False)
    
    def _repr_(self):
        return f'Atividade {self.inicio}'

class Curtida(Base):
    
    __tablename__ = 'b3a1_curtida'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    id_atividade = Column(Integer, nullable=False)

    def _repr_(self):
        return f'Curtida {self.id_usuario}'   


class Comentario(Base):

    __tablename__ = 'b3a1_comentario'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    id_atividade = Column(Integer, nullable=False)
    texto_comentario = Column(String(555), nullable = False)

    def _repr_(self):
        return f'Usuario {self.texto_comentario}'

class Curtida_Comentario(Base):

    __tablename__ = 'b3a1_curtida_comentario'
    
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    id_atividade = Column(Integer, nullable=False)
    
    def _repr_(self):
        return f'Usuario {self.id_usuario}'    
