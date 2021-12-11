import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://root@127.0.0.1:3306/phpmyadmin?charset=utf8mb4")
connection = engine.connect()

sql_query = db.text("SELECT * FROM pf_produtos")
result = connection.execute(sql_query)
result_as_list = result.fetchall()

for row in result_as_list:
    print(row)


#metada = db.MetaData()