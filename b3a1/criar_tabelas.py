from sqlalchemy import *

from model.models import Curtida_Comentario, Usuario, Curtida, Comentario, Atividade

engine = create_engine("mysql+pymysql://primeiro_20202017176:cefetMG20202017176@primeiro.cefetvga.pro.br/primeiro_20202017176?charset=utf8mb4",echo=True)

usuario = Usuario.__table__
usuario.create(engine, checkfirst=True)

curtida = Curtida.__table__
curtida.create(engine, checkfirst=True)

curtida_comentario = Curtida_Comentario.__table__
curtida.create(engine, checkfirst=True)

comentario = Comentario.__table__
comentario.create(engine, checkfirst=True)

atividade = Atividade.__table__
atividade.create(engine, checkfirst=True)

