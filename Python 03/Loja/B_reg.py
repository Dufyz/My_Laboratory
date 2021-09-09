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

def registrar_cliente():
    
    class cliente():
        __nome = str(input('\nNome do cliente: '))
        __sobrenome = str(input('Sobrenome: '))
        __idade = int(input('Idade: '))
        __compras = int(input('Total compras: '))

        comando_mysql = f'INSERT INTO clientes (nome, sobrenome, idade, compras) VALUES (%s, %s, %s, %s)'
        info = (str(__nome), str(__sobrenome), str(__idade), str(__compras))

        cursor.execute(comando_mysql, info)
        db.commit()

        time.sleep(1)

        print('\n Cliente registrado com sucesso')
        print(f'\nNome: {__nome}',
              f'\nSobrenome: {__sobrenome}',
              f'\nIdade: {__idade}',
              f'\nCompras: {__compras}')
        
        pass