import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    port = 3306,
    database = 'incount'
)

cursor = db.cursor()

def registrar_funcionario():
    
    class funcionario():
        __nome = input('Nome do funcionário: ')
        __documento = input('Documento do funcionário: ')
        __salario = input('Salário do funcionário: ')

        comando_mysql = f'INSERT INTO funcionario (nome, documento, salario) VALUES (%s, %s, %s)'
        info = (__nome, __documento, __salario)

        cursor.execute(comando_mysql, info)
        db.commit()

        print('Funcionário registrado com sucesso')
        print(f'\nID: gerado automáticamente',
              f'\nNome: {__nome}',
              f'\nDocumento: {__documento}',
              f'\nSalário: R${__salario}\n')

registrar_funcionario()