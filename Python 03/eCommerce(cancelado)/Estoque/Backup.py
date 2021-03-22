from Estoque import Estoque_Menu


list_estoque = list() # Contém todas as produtos registrados e seu disponibilidade
list_verifica_id = list() # Contém todos os ids já registrados para tratamento de erro
list_entrada_de_produto = list() # Registra toda a entrada de produto
list_saída_de_produto = list() # Registra toda a saída de produto

dict_produto = dict() # Armazena todas as informações do produto
dict_nRegistro = dict() # Reúne as informações do produto e seu ID de reconhecimento


def registrar_produto_novo(): # Registra produtos ainda não existentes no estoque

    class Produto():

        def __init__(self):
            self.__produto_id:int = int(input('ID do Produto : '))
            self.__nome:str = input('Nome do produto : ')
            self.__quantidade:int = int(input('Quantidade : '))
            self.tamanho = input('Tamanho do produto : ')
            self.cor:str = input('Cor do Produto : ')
            self.__data = input('Data de entrada do produto : ')
            self.__nRegistro:int = len(list_estoque) + 1

            dict_produto['nRegistro']:int = self.__nRegistro
            dict_produto['Nome']:str = self.__nome.title()
            dict_produto['Quantidade']:int = self.__quantidade
            dict_produto['Tamanho'] = self.tamanho
            dict_produto['Cor']:str = self.cor
            dict_produto['Data'] = self.__data

            dict_nRegistro['ID DO PRODUTO']:int = self.__produto_id
            dict_nRegistro['INFO']:str = dict_produto.copy()

        def __repr__(self):
            Produto()

    Produto()

    if dict_nRegistro['ID DO PRODUTO'] not in list_verifica_id:
        list_entrada_de_produto.append(dict_produto.copy())
        list_estoque.append(dict_nRegistro.copy())

        print('\n', dict_produto, '- REGISTRADO')
            # Adiciona o produto ao estoque e controle de entrada

    else:
        print('TÁ ERRADO ISSO AI IRMÃO')

    list_verifica_id.append(dict_nRegistro.copy()['ID DO PRODUTO'])
        # list_verifica_registro.append(dict_produto.copy()['nRegistro'])

def controle(): # Registra toda a entrada e saída de produtos para controlar o estoque

    def menu_registrar_entrada_saida():

        def registra_entrada_de_produto(): # Registra toda a entrada de produtos

            while True:

                try:
                    id_quest: int = int(input('\nDigite o ID do produto ao qual deseja registrar entrada : '))

                    if id_quest not in list_verifica_id:
                        print(f'O ID digitado ({id_quest}) não existe no estoque')

                    else:
                        break

                except:
                    print('\n!Erro')
                    print('Use apenas valores valídos')
                    continue

            nome_produto: dict = list_estoque[list_verifica_id.index(id_quest)]['INFO']['Nome'] # Acessa o nome do produto
            print('\nProduto', f'"{nome_produto}"', ' - SELECIONADO')

            quantidade:str = int(input(f'\nQuantidade a ser adicionada ao estoque do "{nome_produto}"  : '))

            list_estoque[list_verifica_id.index(id_quest)]['INFO']['Quantidade'] += quantidade
                # Soma a quantia solicitada ao estoque
            x: dict = list_estoque[list_verifica_id.index(id_quest)]['INFO']['Quantidade']

            print(f'\nQuantidade do produto {nome_produto} atualiza : "{x}"')

        def registrar_saída_de_produto(): # Registra toda a saída de produtos

            while True:

                try:
                    id_quest: int = int(input('\nDigite o ID do produto ao qual deseja registrar saída : '))
                    if id_quest not in list_verifica_id:
                        print(f'O ID digitado ({id_quest}) não existe no estoque')

                    else:break

                except:
                    print('\n!Erro')
                    print('Use apenas valores valídos')
                    continue

            nome_produto:str = list_estoque[list_verifica_id.index(id_quest)]['INFO']['Nome'] # Acessa o nome do produto
            print('\nProduto', f'"{nome_produto}"', ' - SELECIONADO')

            quantidade:int = int(input(f'\nQuantidade a ser removida do estoque do "{nome_produto}"  : '))
            quantidade_nova = list_estoque[list_verifica_id.index(id_quest)]['INFO']['Quantidade'] - quantidade
                # Subtrai a quantia solicitada do estoque
            print(f'\n Quantidade do produto "{nome_produto}" atualiza : "Quantidade : {quantidade_nova}"')

    def menu_entrada_saida():

        def entrada_de_entrada():
            for produto in list_entrada_de_produto:
                print(produto)

        def saida_de_saida():
            for produto in list_saída_de_produto:
                print(produto)

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

            elif menu_quest == 2:
                menu_entrada_saida()
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

def atualização_cadastral() -> dict : # Atualiza o armazenamento de informações de um produto mal registrado

    while True:

        quest: int = int(input('\nDigite o número de id do produto : '))

        if quest in list_verifica_id:
            break

        elif quest != int:
            print('\n!Erro')
            print('Use apenas valores valídos')
            continue

        else: print('\n!Erro'), print('!Não encotrado')

    index:int = list_verifica_id.index(quest) # Acessa o index do produto selecionado

    class AtualizaProduto(): # Coleta e altera as informações do produto selecionado

        def __init__(self):
            self.__nome:str = input('Nome do produto : ')
            self.__quantidade:int = int(input('Quantidade : '))
            self.tamanho = input('Tamanho do produto : ')
            self.cor:str = input('Cor do Produto : ')
            self.__data = input('Data de entrada do produto : ')
            self.__nRegistro:int = list_estoque[index]['INFO']['nRegistro']

            list_estoque[index]['INFO']['nRegistro']:int = self.__nRegistro
            list_estoque[index]['INFO']['Nome']:str  = self.__nome.title()
            list_estoque[index]['INFO']['Quantidade']:int = self.__quantidade
            list_estoque[index]['INFO']['Tamanho'] = self.tamanho
            list_estoque[index]['INFO']['Cor']:str = self.cor
            list_estoque[index]['INFO']['Data'] = self.__data

        def __repr__(self):
            AtualizaProduto()

    AtualizaProduto()
    print('\n', list_estoque[index]['INFO'], '- ATUALIZADO')

def estoque() -> list: # Imprime todo o estoque disponível
    for c in list_estoque:
        print(c)