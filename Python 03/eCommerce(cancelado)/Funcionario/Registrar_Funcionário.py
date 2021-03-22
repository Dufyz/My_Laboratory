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

def registar_funcionário() -> dict:

    while True:

        try:
            func_quest: int = int(input('\nDeseja registrar quantos funcionário ? '))
            break

        except:
            print('\n!Erro')
            print('Use apenas valores valídos')
            continue

    class RegistrarFuncionário():

        def __init__(self):
            self.__name: str = str(input('\nNome do Funcionário : '))
            self.__CPF: str = input('CPF : ')
            self.__RG: str = input('RG : ')
            self._birthday: int = input('Data de nascimento : ')
            self.address: str = input('Endereço : ')
            self.phone: str = input('Número de telefone : ')
            self.function: str = input('Função do Funcionário : ')
            self.salario: str = input('Salário do Funcionário : ')
            self.__nCod: int = random.randrange(0, 124897)

            comando_mysql = f'INSERT INTO funcionario (name, CPF, RG, birthday, address, phone, function, salario, COD) VALUES (%s, %s, %s, %s, %s, ' \
                f'%s, %s, %s, %s)'
            registra_funcionario = (str(self.__name), str(self.__CPF), str(self.__RG), str(self._birthday),
                                    str(self.address), str(self.phone), str(self.function),
                                    str(self.salario), str(self.__nCod))

            cursor.execute(comando_mysql, registra_funcionario)
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
            print(f"Função : {self.function}")
            print(f"Salário : {self.salario}")
            print('\n***** --- REGISTRADO --- *****')
            print('')

        def __repr__(self):
            return RegistrarFuncionário()

    for c in range(0, func_quest):
        RegistrarFuncionário()

def atualização_cadastral() -> dict:

    quest: int = int(input('Digite o número de registro do funcionário : '))

    class AtualizaFuncionário():

        def __init__(self):

            self.__name: str = str(input('\nNome do Funcionário : '))
            self.__CPF: str = input('CPF : ')
            self.__RG: str = input('RG : ')
            self._birthday: int = input('Data de nascimento : ')
            self.address: str = input('Endereço : ')
            self.phone: str = input('Número de telefone : ')
            self.function: str = input('Função do Funcionário : ')
            self.salario: str = input('Salário do Funcionário : ')

            comando_mysql = f'UPDATE funcionario SET name = "{self.__name}", CPF = "{self.__CPF}", RG = "{self.__RG}"' \
                f', birthday = "{self._birthday}", address = "{self.address}", phone = "{self.phone}", function = "{self.function}"' \
                f', salario = "{self.salario}"' \
                f'WHERE ID = {quest}'
            cursor.execute(comando_mysql)
            banco.commit()

        def __repr__(self):
            return AtualizaFuncionário()

    AtualizaFuncionário()

def banco_funcionário() -> list:
    comando_mysql = f'SELECT *FROM funcionario'
    cursor.execute(comando_mysql)
    banco_de_dados = cursor.fetchall()

    for c in banco_de_dados:
        print(f' --- FUNCIONÁRIO {c[0]} --- ')
        print(f"\nID : {c[0]}")
        print(f"Nome : {c[1]}")
        print(f"CPF : {c[2]}")
        print(f"RG : {c[3]}")
        print(f"Data de nascimento : {c[4]}")
        print(f"Endereço : {c[5]}")
        print(f"Telefone : {c[6]}")
        print(f"Função : {c[7]}")
        print(f"Salário : {c[8]}")
        print(f"Código : {c[9]}")
        print('')

