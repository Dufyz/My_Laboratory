# from typing import Union

from Funcionario import Registrar_Funcionário


def menu_funcionário() -> str:

    while True:

        print('')
        print('*' * 40)
        print('  BEM-VINDO AO MENU DOS FUNCIONÁRIOS')
        print('*' * 40)

        print('\n[1] REGISTRAR FUNCIONÁRIO'
              '\n[2] ATUALIZAÇÃO CADASTRAL'
              '\n[3] BANCO DE DADOS DOS FUNCIONÁRIOS'
              '\n[4] VOLTAR AO MENU PRINCIPAL')

        menu_quest: int = int(input('\nESCOLHA UMA DAS OPÇÕES ACIMA : '))

        if menu_quest == 1: # Abre o registro de novos funcionários
            print('\nVOCÊ ESCOLHEU "REGISTRAR UM FUNCIONÁRIO')
            Registrar_Funcionário.registar_funcionário()

        elif menu_quest == 2: # Abre a atualização cadastral dos funcionários já registrados
            print('\nVOCÊ ESCOLHEU "ATUALIZAÇÃO CADASTRAL\n')
            Registrar_Funcionário.atualização_cadastral()

        elif menu_quest == 3: # Abre o banco de dados dos funcionários
            print('\nVOCÊ ESCOLHEU "BANCO DE DADOS DOS FUNCIONÁRIOS\n')
            Registrar_Funcionário.banco_funcionário()

        elif menu_quest == 4: # Volta ao menu principal
            print('\nVOCÊ ESCOLHEU "VOLTAR AO MENU PRINCIPAL\n')
            break

        else:
            print('\n!ERROR')
            print('DIGITE APENAS OPÇÕES VALÍDAS')
            continue

# menu_funcionário()