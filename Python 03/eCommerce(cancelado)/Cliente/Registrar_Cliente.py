# from typing import Union
import random
import mysql.connector

banco = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    passwd = '',
    database = 'caser_engenharia'
)

cursor = banco.cursor()

def registrar_cliente() -> dict:

    while True:

        try:
            func_quest: int = int(input('Deseja registrar quantos clientes ? '))
            break

        except:
            print('\n!Erro')
            print('Use apenas valores valídos')
            continue

    class RegistrarCliente():

        def __init__(self):

            self.__name: str = str(input('\nNome do Cliente : '))
            self.__CPF: str = input('CPF : ')
            self.__RG: str = input('RG : ')
            self._birthday: int = input('Data de nascimento : ')
            self.address: str = input('Endereço : ')
            self.phone: str = input('Número de telefone : ')
            self.__nCod: int = random.randrange(0, 124897)

            comando_mysql = f'INSERT INTO cliente (name, CPF, RG, birthday, address, phone, COD) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            registra_cliente = (str(self.__name), str(self.__CPF), str(self.__RG), str(self._birthday),
                                str(self.address), str(self.phone), str(self.__nCod))

            cursor.execute(comando_mysql, registra_cliente)
            banco.commit()

            print('')
            print('\n***** --- REGISTRADO --- *****\n')
            print(f"Código : {self.__nCod}")
            print(f"Nome : {self.__name}")
            print(f"CPF : {self.__CPF}")
            print(f"RG : {self.__RG}")
            print(f"Data de nascimento : {self._birthday}")
            print(f"Endereço : {self.address}")
            print(f"Telefone : {self.phone}")
            print('\n***** --- REGISTRADO --- *****\n')
            print('')

        def __repr__(self):
            return RegistrarCliente()

    for c in range(0, func_quest):
        RegistrarCliente()

def atualização_cadastral() -> dict:


    quest: int = int(input('Digite o ID do Cliente : '))

    class AtualizaCliente():

        def __init__(self):
            self.__name: str = str(input('\nNome do Cliente : '))
            self.__CPF: str = input('CPF : ')
            self.__RG: str = input('RG : ')
            self._birthday: int = input('Data de nascimento : ')
            self.address: str = input('Endereço : ')
            self.phone: str = input('Número de telefone : ')

            comando_mysql = f'UPDATE cliente SET name = "{self.__name}", CPF = "{self.__CPF}", RG = "{self.__RG}"' \
                f', birthday = "{self._birthday}", address = "{self.address}", phone = "{self.phone}"' \
                f' WHERE ID = {quest}'
            cursor.execute(comando_mysql)
            banco.commit()

        def __repr__(self):
            return AtualizaCliente()

    AtualizaCliente()

def banco_cliente() -> list:
    comando_mysql = f'SELECT *FROM cliente'
    cursor.execute(comando_mysql)
    banco_de_dados = cursor.fetchall()

    for c in banco_de_dados:
        print(f'\n --- Cliente {c[0]} --- ')
        print(f"\nID : {c[0]}")
        print(f"Nome : {c[1]}")
        print(f"CPF : {c[2]}")
        print(f"RG : {c[3]}")
        print(f"Data de nascimento : {c[4]}")
        print(f"Endereço : {c[5]}")
        print(f"Telefone : {c[6]}")
        print(f"Código : {c[7]}")
        print('')