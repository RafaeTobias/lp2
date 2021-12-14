from re import S
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import user

from model.models import *

engine = create_engine("mysql+pymysql://primeiro_20202017176:cefetMG20202017176@primeiro.cefetvga.pro.br/primeiro_20202017176?charset=utf8mb4",echo=True)

Session = sessionmaker(bind=engine)
session = Session()

#clientes
cliente1 = Cliente(id=1, endereco_cliente = "Varginha", CPF = '37002400', telefone_cliente = '922552022')
session.add(cliente1)

cliente2 = Cliente(id=2, endereco_cliente = "Tres Pontas", CPF = '7006240', telefone_cliente = '955552022')
session.add(cliente2)

cliente3 = Cliente(id=3, endereco_cliente = "Santana", CPF = '3706240', telefone_cliente = '900552022')
session.add(cliente3)

#editoras
editora1 = Editora(id=1, codigo = "123", endereco_editora = "Varginha", telefone_editora = "23232333", gerente = "Carlos")
session.add(editora1)

editora2 = Editora(id=2, codigo = "321", endereco_editora = "Passos", telefone_editora = "523232333", gerente = "Pedro")
session.add(editora2)

editora3 = Editora(id=3, codigo = "213", endereco_editora = "Curvelo", telefone_editora = "123232333", gerente = "Lucas")
session.add(editora3)

#livros
livro1 = Livro(id=1, editora=editora1, autor="Machado", assunto="Brasil", ISBN='Isbn', quantidade=30)
session.add(livro1)

livro2 = Livro(id=2, editora=editora1, autor="Drummond", assunto="Tecnologia", ISBN='Isbn2', quantidade=50)
session.add(livro2)

livro3 = Livro(id=3, editora=editora1, autor="José de Alencar", assunto="Regionalismo", ISBN='Isbn3', quantidade=70)
session.add(livro3)

#compras
compra1 = Compra(id=1, cliente=cliente1, livro=livro3, data_compra='2022-05-08 11:35:29')
session.add(compra1)

compra2 = Compra(id=2, cliente=cliente3, livro=livro2, data_compra='2016-05-08 08:35:29')
session.add(compra2)

compra3 = Compra(id=3, cliente=cliente2, livro=livro1, data_compra='2012-05-08 17:35:29')
session.add(compra3)

session.commit()


