    # from typing import Union

from Funcionario import Funcionário_Menu
from Cliente import Cliente_Menu
from Estoque import Estoque_Menu


while True:

    print('*' * 45)
    print('        BEM-VINDO AO MENU PRINCIPAL')
    print('*' * 45)

    print('\n[1] MENU DO CLIENTE'
          '\n[2] MENU DO FUNCIONÁRIO'
          # '\n[3] MENU DO ESTOQUE'
          '\n[4] MENU DO FINANCEIRO'
          '\n[5] SAIR')

    menu_quest: int = int(input('\nESCOLHA UMA DAS OPÇÕES ACIMA : '))

    if menu_quest == 1:
        Cliente_Menu.menu_cliente() # Abre o menu dos clientes

    elif menu_quest == 2:
        Funcionário_Menu.menu_funcionário() # Abre o menu dos funcionários
        print('')

    elif menu_quest == 3: # Abre o menu do estoque
        Estoque_Menu.menu_estoque() #Abre o menu do estoque

    #elif menu_quest == 4: # Abre o menu do financeiro
     #   Financeiro_Menu.menu_financeiro()

    elif menu_quest == 5: # Finaliza o aplicativo
        exit()