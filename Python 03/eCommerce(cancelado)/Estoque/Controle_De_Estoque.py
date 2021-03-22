from Estoque import Estoque_Menu

import mysql.connector


banco = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    passwd = "",
    database = "caser_engenharia"
)

cursor = banco.cursor()

def registrar_produto_novo(): # Registra produtos ainda não existentes no estoque

    class Produto():

        def __init__(self):
            self.__nome:str = input('Nome do produto : ')
            self.__quantidade:int = int(input('Quantidade : '))
            self.tamanho = input('Tamanho do produto : ')
            self.cor:str = input('Cor do Produto : ')
            self.__data = input('Data de entrada do produto : ')
            self.__Codigo: int = input('Codigo do Produto : ')

            comando_mysql = f'INSERT INTO estoque (nome, quantidade, tamanho, cor, data, codigo) VALUES (%s, %s, %s, %s, %s, %s)'
            registra_produto = (str(self.__nome),str(self.__quantidade),str(self.tamanho),str(self.cor),str(self.__data), str(self.__Codigo))
            cursor.execute(comando_mysql, registra_produto)
            banco.commit()

            print('')
            print(f"Código : {self.__Codigo}", end='')
            print(f" / Nome : {self.__nome}", end='')
            print(f" / Quantidade : {self.__quantidade}", end='')
            print(f" / Tamanho : {self.tamanho}", end='')
            print(f" / Cor : {self.cor}", end='')
            print(f" / Data : {self.__data}", end='')
            print(' // --- REGISTRADO')

        def __repr__(self):
            Produto()

    Produto()

def controle(): # Registra toda a entrada e saída de produtos para controlar o estoque

    def registrar_entrada():

        while True:

            try:
                id_quest: int = int(input('\nDigite o ID do produto ao qual deseja registrar entrada : '))

                comando_mysql = "SELECT ID FROM estoque"
                cursor.execute(comando_mysql)
                resultado = cursor.fetchall()

                if id_quest not in resultado:
                    print('Digite um ID já registrado ')
                    continue

                else: break

            except:
                print('\n!Erro')
                print('Use apenas valores valídos')
                continue

        comando_mysql = f'SELECT nome from estoque WHERE ID = {id_quest}'
        cursor.execute(comando_mysql)
        nome_produto = cursor.fetchall()

        print('\nProduto', f'"{nome_produto}"', ' - SELECIONADO')

        quantidade_add = int(input(f'\nQuantidade a ser adicionada ao estoque do "{nome_produto}"  : '))

        comando_mysql = f'SELECT quantidade from estoque WHERE ID = {id_quest}'
        cursor.execute(comando_mysql)
        quantidade_produto = int(cursor.fetchall())
        quantidade_atualizada = quantidade_produto + quantidade_add

        comando_mysql = f'UPDATE produto SET quantidade = "{quantidade_atualizada}" WHERE ID = {id_quest}'
        cursor.execute(comando_mysql)
        banco.commit()

        print(f'\nQuantidade do produto {nome_produto} atualizada : "{quantidade_atualizada}"')

    def registrar_saida():
        pass

    def ver_entrada():
        pass

    def ver_saida():
        pass

    print('*' * 40)
    print('         CONTROLE DE ESTOQUE')
    print('*' * 40)

    print('\n[1] REGISTRAR ENTRADA'
          '\n[2] REGISTRAR SAÍDA'
          '\n[3] VER ENTRADA'
          '\n[4] VER SAÍDA'
          '\n[5] VOLTAR')

    while True:

        try:
            menu_quest: int = int(input('\nESCOLHA UMA DAS OPÇÕES ACIMA : \n'))

            if menu_quest == 1:
                registrar_entrada()
                break

            elif menu_quest == 2:
                registrar_saida()
                break

            elif menu_quest == 3:
                ver_entrada()
                break

            elif menu_quest == 4:
                ver_saida()
                break

            elif menu_quest == 5:
                Estoque_Menu.menu_estoque()

            else:
                print('\n!Erro')
                print('!Digite uma opção valída')

        except:
            print('\n!Erro')
            print('!Digite uma opção valída')

def estoque() -> list: # Imprime todo o estoque disponível
    comando_mysql = f'SELECT *FROM estoque'
    cursor.execute(comando_mysql)
    estoque = cursor.fetchall()

    for c in estoque:
        print('')
        print(f"ID : {c[0]}", end='')
        print(f" / Nome : {c[1]}", end='')
        print(f" / Quantidade : {c[2]}", end='')
        print(f" / Tamanho : {c[3]}", end='')
        print(f" / Cor : {c[4]}", end='')
        print(f" / Data : {c[5]}", end='')
        print(f" / Código : {c[6]}", end='')
        print(' // --- PRODUTO')
