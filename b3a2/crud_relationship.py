from re import S
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import user

from model.models import *

engine = create_engine("mysql+pymysql://primeiro_20202017176:cefetMG20202017176@primeiro.cefetvga.pro.br/primeiro_20202017176?charset=utf8mb4",echo=True)

Session = sessionmaker(bind=engine)
session = Session()

#adicionando usuario 1 e atividades
usuario1 = Usuario(id=1, senha='batatinha1', email='usu1@usu.com')

atividade1 = Atividade(id=1, usuario=usuario1, data='2021-11-07', inicio='08:51:26', fim='09:50:32', local='VGA', tipo_atividade='Aeróbica', quilometragem=25.6)
session.add(atividade1)

atividade2 = Atividade(id=2, usuario=usuario1, data='2021-11-17', inicio='09:51:26', fim='10:50:32', local='VGA', tipo_atividade='Aeróbica', quilometragem=26.6)
session.add(atividade2)

atividade3 = Atividade(id=3, usuario=usuario1, data='2021-11-27', inicio='10:51:26', fim='11:50:32', local='VGA', tipo_atividade='Aeróbica', quilometragem=27.6)
session.add(atividade3)

#adicionando usuario 2 e atividades
usuario2 = Usuario(id=2, senha='batatinha1', email='usu2@usu.com')

atividade4 = Atividade(id=4, usuario=usuario1, data='2021-11-07', inicio='08:51:26', fim='09:50:32', local='VGA', tipo_atividade='Aeróbica', quilometragem=25.6)
session.add(atividade4)

atividade5 = Atividade(id=5, usuario=usuario1, data='2021-11-17', inicio='09:51:26', fim='10:50:32', local='VGA', tipo_atividade='Aeróbica', quilometragem=26.6)
session.add(atividade5)

atividade6 = Atividade(id=6, usuario=usuario1, data='2021-11-27', inicio='10:51:26', fim='11:50:32', local='VGA', tipo_atividade='Aeróbica', quilometragem=27.6)
session.add(atividade6)

#adicionando usuario 3 e atividades
usuario3 = Usuario(id=3, senha='batatinha1', email='usu3@usu.com')

atividade7 = Atividade(id=7, usuario=usuario1, data='2021-11-07', inicio='08:51:26', fim='09:50:32', local='VGA', tipo_atividade='Aeróbica', quilometragem=25.6)
session.add(atividade7)

atividade8 = Atividade(id=8, usuario=usuario1, data='2021-11-17', inicio='09:51:26', fim='10:50:32', local='VGA', tipo_atividade='Aeróbica', quilometragem=26.6)
session.add(atividade8)

atividade9 = Atividade(id=9, usuario=usuario1, data='2021-11-27', inicio='10:51:26', fim='11:50:32', local='VGA', tipo_atividade='Aeróbica', quilometragem=27.6)
session.add(atividade9)

#adicionando comentarios
comentario1 = Comentario(id=1, usuario=usuario1, atividade=atividade2, texto_comentario="Muito bom!")
session.add(comentario1)

comentario2 = Comentario(id=2, usuario=usuario1, atividade=atividade3, texto_comentario="Bacana!")
session.add(comentario1)

comentario3 = Comentario(id=3, usuario=usuario3, atividade=atividade4, texto_comentario="Legal!")
session.add(comentario1)

comentario4 = Comentario(id=4, usuario=usuario2, atividade=atividade7, texto_comentario="Não gostei!")
session.add(comentario1)

#adicionando curtida
curitda1 = Curtida(usuario=usuario1, atividade=atividade1)
session.add(curitda1)

curitda2 = Curtida(usuario=usuario1, atividade=atividade2)
session.add(curitda2)

session.commit()

tuplas = session.query(Atividade).order_by(Atividade.quilometragem) 

def select():
    for tuplas in session.query(Atividade).filter(Atividade.local=='VGA'):
        print(tuplas.usuario_id, "-" , tuplas.quilometragem, "-", tuplas.inicio, "-", tuplas.fim)

def update():
    Usuario.senha = "senhausu1"

def delete():
    for tuplas in session.query(Atividade).filter(Atividade.local=='VGA'):
        print("ENTREI")
        if tuplas.usuario_id == 'usu2@usu.com':
            print("deletei")
            var = tuplas.usuario_id
            session.delete(var)




