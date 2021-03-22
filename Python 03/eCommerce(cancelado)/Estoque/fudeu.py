    def menu_registrar_entrada_saida():

        def registra_entrada_de_produto(): # Registra toda a entrada de produtos

            while True:

                try:
                    id_quest: int = int(input('\nDigite o ID do produto ao qual deseja registrar entrada : '))
                    # if id_quest not in list_verifica_id:
                    #     print(f'O ID digitado ({id_quest}) não existe no estoque')
                    #
                    # else:
                    break

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

        def registrar_saída_de_produto(): # Registra toda a saída de produtos

            while True:

                try:
                    id_quest: int = int(input('\nDigite o ID do produto ao qual deseja registrar saída : '))
                    # if id_quest not in list_verifica_id:
                    #     print(f'O ID digitado ({id_quest}) não existe no estoque')
                    #
                    # else:break

                except:
                    print('\n!Erro')
                    print('Use apenas valores valídos')
                    continue

            comando_mysql = f'SELECT nome from estoque WHERE ID = {id_quest}'
            cursor.execute(comando_mysql)
            nome_produto = cursor.fetchall()

            print('\nProduto', f'"{nome_produto}"', ' - SELECIONADO')

            quantidade_sub: str = int(input(f'\nQuantidade a ser adicionada ao estoque do "{nome_produto}"  : '))

            comando_mysql = f'SELECT quantidade from estoque WHERE ID = {id_quest}'
            cursor.execute(comando_mysql)
            quantidade_produto = int(cursor.fetchall())
            quantidade_atualizada = quantidade_produto - quantidade_sub

            comando_mysql = f'UPDATE produto SET quantidade = "{quantidade_atualizada}" WHERE ID = {id_quest}'
            cursor.execute(comando_mysql)
            banco.commit()

            print(f'\nQuantidade do produto {nome_produto} atualizada : "{quantidade_atualizada}"')

        print('*' * 40)
        print('         ENTRADA/SAÍDA')
        print('*' * 40)

        print('\n[1] REGISTRAR ENTRADA'
              '\n[2] REGISTRAR SAÍDA'
              '\n[3] VOLTAR')

        while True:

            try:
                menu_quest: int = int(input('\nESCOLHA UMA DAS OPÇÕES ACIMA : \n'))

                if menu_quest == 1:
                    registra_entrada_de_produto()
                    break

                elif menu_quest == 2:
                    registrar_saída_de_produto()
                    break

                elif menu_quest == 3:
                    Estoque_Menu.menu_estoque()
                    break

                else:
                    print('\n!Erro')
                    print('!Digite uma opção valída')

            except:
                print('\n!Erro')
                print('!Digite uma opção valída')


    print('*'  * 40)
    print('         CONTROLE DE ESTOQUE')
    print('*' * 40)

    print('\n[1] REGISTRAR ENTRADA/SAÍDA DE PRODUTO'
          '\n[2] VER ENTRADA/SAÍDA DE PRODUTOS'
          '\n[3] VOLTAR')

    while True:

        try:
            menu_quest: int = int(input('\nESCOLHA UMA DAS OPÇÕES ACIMA : \n'))

            if menu_quest == 1:
                menu_registrar_entrada_saida()
                break

            # elif menu_quest == 2:
                #
                #

            elif menu_quest == 3:
                Estoque_Menu.menu_estoque()
                break

            else:
                print('\n!Erro')
                print('!Digite uma opção valída')

        except:
            print('\n!Erro')
            print('!Digite uma opção valída')

# def atualização_cadastral() -> dict : # Atualiza o armazenamento de informações de um produto mal registrado
#
#     while True:
#
#         quest: int = int(input('\nDigite o número de id do produto : '))
#
#         if quest in list_verifica_id:
#             break
#
#         elif quest != int:
#             print('\n!Erro')
#             print('Use apenas valores valídos')
#             continue
#
#         else: print('\n!Erro'), print('!Não encotrado')
#
#     index:int = list_verifica_id.index(quest) # Acessa o index do produto selecionado
#
#     class AtualizaProduto(): # Coleta e altera as informações do produto selecionado
#
#         def __init__(self):
#             self.__nome:str = input('Nome do produto : ')
#             self.__quantidade:int = int(input('Quantidade : '))
#             self.tamanho = input('Tamanho do produto : ')
#             self.cor:str = input('Cor do Produto : ')
#             self.__data = input('Data de entrada do produto : ')
#             self.__nRegistro:int = list_estoque[index]['INFO']['nRegistro']
#
#             list_estoque[index]['INFO']['nRegistro']:int = self.__nRegistro
#             list_estoque[index]['INFO']['Nome']:str  = self.__nome.title()
#             list_estoque[index]['INFO']['Quantidade']:int = self.__quantidade
#             list_estoque[index]['INFO']['Tamanho'] = self.tamanho
#             list_estoque[index]['INFO']['Cor']:str = self.cor
#             list_estoque[index]['INFO']['Data'] = self.__data
#
#         def __repr__(self):
#             AtualizaProduto()
#
#     AtualizaProduto()
#     print('\n', list_estoque[index]['INFO'], '- ATUALIZADO')
#