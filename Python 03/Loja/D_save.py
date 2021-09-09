import mysql.connector

db = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = '',
    port = 3306,
    database = 'incount'
)

cursor = db.cursor()

def db_estoque():
    
    comando_mysql = f'SELECT *FROM estoque'
    cursor.execute(comando_mysql)
    dbestoque = cursor.fetchall()

    print('\nProduto em estoque')

    for c in dbestoque:
        print(f'\nID: {c[0]}',
              f'\nNome: {c[1]}',
              f'\nMarca: {c[2]}',
              f'\nTipo: {c[3]}',
              f'\nQuantidade: {c[4]}\n')
