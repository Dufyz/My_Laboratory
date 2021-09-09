import mysql.connector

db = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = '',
    port = 3306,
    database = 'incount'
)

cursor = db.cursor()

def registrar_estoque():
    
    class estoque():
        __ID = print('\nID gerado automáticamente')
        __nome = input('Qual o nome do produto ? ')
        __marca = input('Qual a marca do produto ? ')
        __tipo = input('Qual o tipo do produto ? ')
        __quantidade = input('Qual a quantidade disponível do produto ? ')

        comando_mysql = f'INSERT INTO estoque (nome, marca, tipo, quantidade) VALUES (%s, %s, %s, %s)'
        info = (str(__nome), str(__marca), str(__tipo), str(__quantidade)) 
        cursor.execute(comando_mysql, info)
        db.commit()

        print('Produto registrado com sucesso')

        print(f'\nID: {__ID}',
              f'\nNome: {__nome}',
              f'\nMarca: {__marca}',
              f'\nTipo: {__tipo}',
              f'\nQuantidade: {__quantidade}',)
