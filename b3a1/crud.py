from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

from model.models import *

engine = create_engine("mysql+pymysql://primeiro_20202017176:cefetMG20202017176@primeiro.cefetvga.pro.br/primeiro_20202017176?charset=utf8mb4",echo=True)

Session = sessionmaker(bind=engine)
session = Session()

#adicionando usuarios
usuario1 = Usuario(id=1, login='user1', senha='batatinha1', email='user1@gmail.com')
usuario2 = Usuario(id=2, login='user2', senha='batatinha2', email='user2@gmail.com')
usuario3 = Usuario(id=3, login='user3', senha='batatinha3', email='user3@gmail.com')

session.add(usuario1)
session.add(usuario2)
session.add(usuario3)

#adicionando atividades
atividade1 = Atividade(id=1, id_usuario=1, data='2021-11-07', inicio='08:51:26', final='09:50:32', local='CEFET', tipo='Aeróbica', quilometragem=25.6)
atividade2 = Atividade(id=2, id_usuario=2, data='2021-11-17', inicio='09:51:26', final='10:50:32', local='CEFET', tipo='Aeróbica', quilometragem=26.6)
atividade3 = Atividade(id=3, id_usuario=3, data='2021-11-27', inicio='10:51:26', final='11:50:32', local='CEFET', tipo='Aeróbica', quilometragem=27.6)

session.add(atividade1)
session.add(atividade2)
session.add(atividade3)

#adicionando curtidas
curtida1 = Curtida(id_usuario=1, id_atividade=1)
curtida2 = Curtida(id_usuario=2, id_atividade=2)
curtida3 = Curtida(id_usuario=3, id_atividade=3)

session.add(curtida1)
session.add(curtida2)
session.add(curtida3)

#adicionando comentarios
comentario1 = Comentario(id=1, id_usuario=1, id_atividade=1, texto_comentario='Muito bom!')
comentario2 = Comentario(id=2, id_usuario=2, id_atividade=2, texto_comentario='Interessante!')
comentario3 = Comentario(id=3, id_usuario=3, id_atividade=3, texto_comentario='Não gostei!')

session.add(comentario1)
session.add(comentario2)
session.add(comentario3)

#adicionando Curtida_Comentario
cutida_comentario1 = Curtida_Comentario(id=1, id_usuario=1, id_atividade=1)
cutida_comentario2 = Curtida_Comentario(id=2, id_usuario=2, id_atividade=2)
cutida_comentario3 = Curtida_Comentario(id=3, id_usuario=3, id_atividade=3)

session.add(curtida1)
session.add(curtida2)
session.add(curtida3)

session.commit()