from D_reg import  registrar_estoque
from D_save import db_estoque

def menu_estoque():
    
    print('\n', '-' * 50)   
    print('                 Menu Estoque')
    print('\n', '-' * 50)

    print('\n[1] Registrar produto',
        '\n[2] Banco de dados dos produtos'
        '\n[3] Voltar')

    section = int(input('\nFaça sua escolha: '))

    if section == 1:
        registrar_estoque()
        return(menu_estoque())

    elif section == 2:
        db_estoque()
        return(menu_estoque())

    elif section == 3:
        pass

    else:
        print('Parece que você não escolheu nenhuma opção válida')
