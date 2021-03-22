# from typing import Union

from Estoque import Controle_De_Estoque


def menu_estoque() -> str:

    while True:

        print('')
        print('*' * 40)
        print('    BEM-VINDO AO MENU DO ESTOQUE')
        print('*' * 40)

        print('\n[1] REGISTRAR NOVO PRODUTO'
              '\n[2] CONTROLE DO ESTOQUE'
              '\n[3] ESTOQUE'
              '\n[4] ATUALIZA PRODUTO'
              '\n[5] VOLTAR AO MENU PRINCIPAL')

        menu_quest: int = int(input('\nESCOLHA UMA DAS OPÇÕES ACIMA : '))

        if menu_quest == 1:  # Registrar entrada de produto
            print('\nVOCÊ ESCOLHEU "ENTRADA DE PRODUTOS"\n')
            Controle_De_Estoque.registrar_produto_novo()

        elif menu_quest == 2: # Registrar entrada de produto
            print('\nVOCÊ ESCOLHEU "CONTROLE DO ESTOQUE"\n')
            Controle_De_Estoque.controle()

        elif menu_quest == 3: # Abre o estoque disponível no momento
            print('\nVOCÊ ESCOLHEU "ESTOQUE"\n')
            Controle_De_Estoque.estoque()

        elif menu_quest == 4: # Abre a atualização cadastral do produto
            print('\nVOCÊ ESCOLHEU "ATUALIZAÇÃO CADASTRAL"')
            Controle_De_Estoque.atualização_cadastral()

        elif menu_quest == 5: # Volta ao menu principal
            print('\nVOCÊ ESCOLHEU "VOLTAR AO MENU PRINCIPAL"\n')
            break

        else:
            print('\n!ERROR')
            print('DIGITE APENAS OPÇÕES VALÍDAS')
            continue

# menu_estoque() #ATEEEEEEEEEENÇÃOOOOOOOOO GUILHERME