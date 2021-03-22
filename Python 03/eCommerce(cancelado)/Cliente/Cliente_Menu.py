# from typing import Union

from Cliente import Registrar_Cliente


def menu_cliente() -> str:

    while True:

        print('')
        print('*' * 40)
        print('    BEM-VINDO AO MENU DOS CLIENTES')
        print('*' * 40)

        print('\n[1] CADASTRAR CLIENTE'
              '\n[2] ATUALIZAÇÃO CADASTRAL'
              '\n[3] BANCO DE DADOS DOS CLIENTES'
              '\n[4] VOLTAR AO MENU PRINCIPAL')

        menu_quest: int = int(input('\nESCOLHA UMA DAS OPÇÕES ACIMA : '))

        if menu_quest == 1: # Abre o registro de novos clientes
            print('\nVOCÊ ESCOLHEU "CADASTRAR CLIENTE"\n')
            Registrar_Cliente.registrar_cliente()

        elif menu_quest == 2: # Abre a atualização cadastral de clientes já registrados
            print('')
            Registrar_Cliente.atualização_cadastral()

        elif menu_quest == 3: # Abre o banco de dados dos clientes
            print('\nVOCÊ ESCOLHEU "BANCO DE DADOS DOS CLIENTES"')
            Registrar_Cliente.banco_cliente()

        elif menu_quest == 4: # Volta ao menu principal
            print('\nVOCÊ ESCOLHEU "VOLTAR AO MENU PRINCIPAL"\n')
            break

        else:
            print('\n!ERROR')
            print('DIGITE APENAS OPÇÕES VALÍDAS')
            continue

# menu_cliente()