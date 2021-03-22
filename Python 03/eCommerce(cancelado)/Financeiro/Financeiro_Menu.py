# from typing import Union

from Financeiro import despesas_adm
from Financeiro import receitas_adm


def menu_financeiro() -> str:

    while True:

        print('')
        print('*' * 40)
        print('    BEM-VINDO AO MENU DO FINANCEIRO')
        print('*' * 40)

        print('\n[1] RECEITA ADM'
              '\n[2] DESPESAS ADM'
              # '\n[3] BALANÇO GERAL'
              '\n[3] SAIR')

        menu_quest: int = int(input('\nESCOLHA UMA DAS OPÇÕES ACIMA : '))

        if menu_quest == 1:  #
            print('\nVOCÊ ESCOLHEU "RECEITA ADM"')
            receitas_adm.menu_receita()

        elif menu_quest == 2: #
            print('\nVOCÊ ESCOLHEU "DESPESAS ADM"')
            despesas_adm.menu_despesas()

        elif menu_quest == 3: #
            print('\nVOCÊ ESCOLHEU "SAIR"\n')
            break

        else:
            print('\n!ERROR')
            print('DIGITE APENAS OPÇÕES VALÍDAS')
            continue

menu_financeiro() #AQUIII ÓOOO