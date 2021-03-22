'''
# from typing import Union
import random

dict_Cliente = dict() # Contém todas as INFO's do cliente
dict_nRegistro = dict() # Adiciona todas as INFO's do cliente junto com seu número de registro (por ordem)

list_Cliente_Total = list() # Lista que contém todos os clientes já registrados
list_Novos_Clientes = list() # Lista que adiciona os novos clientes a lista total de clientes

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

            self.__nome: str = str(input('\nNome do Cliente : '))
            self.__documento: str = input('Documento do Cliente : ')
            self._nota: int = input('Nota do Cliente : ')
            self.__nID: int = random.randrange(0, 124897)

            dict_Cliente['ID']: int = self.__nID
            dict_Cliente['Nome']: str = self.__nome.title()
            dict_Cliente['Documento']: str = self.__documento
            dict_Cliente['Nota']: int = self._nota

            list_Novos_Clientes.append(dict_Cliente.copy())
                # Adiciona os clientes a lista de novos clientes

        def __repr__(self):
            return RegistrarCliente()

    for c in range(0, func_quest):
        RegistrarCliente()

    print('')
    for Funcionário in list_Novos_Clientes:
        print(Funcionário, '- Registrado')

    for x in list_Novos_Clientes:

        dict_nRegistro['nRegistro'] = len(list_Cliente_Total) + 1
        dict_nRegistro['INFO'] = x
        list_Cliente_Total.append(dict_nRegistro.copy())
            # Adiciona os novos cliente a lista total de clientes

    list_Novos_Clientes.clear()
        # Limpa toda a lista de novos clientes após adicionalos a lista geral de clientes

def atualização_cadastral() -> dict:


    quest: int = int(input('Digite o número de registro do funcionário : '))
    index: int = quest - 1

    class AtualizaCliente():

        def __init__(self):

            self.__nome: str = str(input('\nNome do Cliente : '))
            self.__documento: str = input('Documento do Cliente : ')
            self._nota: int = input('Nota do Cliente : ')
            self.__nID: int = list_Cliente_Total[index]['INFO']['ID']

            list_Cliente_Total[index]['INFO']['Nome'] = self.__nome.title()
            list_Cliente_Total[index]['INFO']['Documento'] = self.__documento
            list_Cliente_Total[index]['INFO']['Nota'] = self._nota
            list_Cliente_Total[index]['INFO']['ID'] = self.__nID

        def __repr__(self):
            return AtualizaCliente()

    AtualizaCliente()
    print('\n', list_Cliente_Total[index]['INFO'], '- ATUALIZADO')

def banco_cliente() -> list:
    for c in list_Cliente_Total:
        print(c)

''' # registrar_cliente / etc - ANTES DO BANCO DE DADOS / 1.0

"""# from typing import Union
import mysql.connector
import random

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

            self.__nome: str = str(input('\nNome do Cliente : '))
            self.__documento: str = input('Documento do Cliente : ')
            self._nota: int = input('Nota do Cliente : ')
            self.__nCodigo: int = random.randrange(0, 124897)

            comando_mysql = f'INSERT INTO cliente (nome, documento, codigo, nota) VALUES (%s, %s, %s, %s)'
            registra_cliente = (str(self.__nome), str(self.__documento), str(self.__nCodigo), str(self._nota))
            cursor.execute(comando_mysql, registra_cliente)
            banco.commit()

            print('')
            print(f"Código : {self.__nCodigo}", end='')
            print(f" / Nome : {self.__nome}", end='')
            print(f" / Documento : {self.__documento}", end='')
            print(f" / Nota : {self._nota}", end='')
            print(' // --- REGISTRADO')

        def __repr__(self):
            return RegistrarCliente()

    for c in range(0, func_quest):
        RegistrarCliente()

def atualização_cadastral() -> dict:


    quest: int = int(input('Digite o ID do Cliente : '))

    comando_mysql = f'SELECT ID, codigo FROM cliente WHERE ID = {quest}'
    cursor.execute(comando_mysql)
    codigo = cursor.fetchall()
    for c in codigo:
        codigo = c[1]

    class AtualizaCliente():

        def __init__(self):

            self.__nome: str = str(input('\nNome do Cliente : '))
            self.__documento: str = input('Documento do Cliente : ')
            self._nota: int = input('Nota do Cliente : ')
            self.__nCodigo: int = codigo

            comando_mysql = f'UPDATE cliente SET nome = "{self.__nome}", documento = "{self.__documento}", ' \
                f'nota = "{self._nota}", codigo = "{self.__nCodigo}" WHERE ID = {quest}'
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
        print('')
        print(f"ID : {c[0]}", end='')
        print(f" / Nome : {c[1]}", end='')
        print(f" / Documento : {c[2]}", end='')
        print(f" / Código : {c[3]}")""" # registrar_cliente / etc - DEPOIS DO BANCO DE DADOS / 2.0
