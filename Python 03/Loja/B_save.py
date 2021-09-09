import mysql.connector
import time

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '',
    database = 'incount'
    )

cursor = db.cursor()

def db_cliente():
    
    comando_mysql = f'SELECT *from clientes'
    cursor.execute(comando_mysql)
    dbcliente = cursor.fetchall()

    print('\n CLIENTES REGISTRADOS: ')

    time.sleep(1)

    for c in dbcliente:
        print(f'\nNome: {c[0]}')
        print(f'Sobrenome: {c[1]}')
        print(f'Idade: {c[2]}')
        print(f'Compras: {c[3]}') 
    pass
