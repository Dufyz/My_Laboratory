import mysql.connector


banco = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    passwd = '',
    database = 'caser_engenharia'
)

cursor = banco.cursor()


print('[1] BALANÇO GERAL DAS RECEITAS'
      '[2] REGISTRAR RECEITA'
      '[3] VER RECEITA'
      '[4] ATUALIZAR RECEITA'
      '[5] VOLTAR')

menu_quest = int(input('ESCOLHA UMA DAS OPÇÕES ACIMA : '))

if menu_quest == 1:  #
    print('\nVOCÊ ESCOLHEU "BALANÇO GERAL DAS RECEITAS"\n')
    # registrar_receita()

elif menu_quest == 2:  #
    print('\nVOCÊ ESCOLHEU "REGISTRAR RECEITA"\n')
    # geral_receitas()

elif menu_quest == 3: #
    print('\nVOCÊ ESCOLHEU "VER RECEITA"\n')
    # ver_receitas()

elif menu_quest == 4: #
    print('\nVOCÊ ESCOLHEU "ATUALIZAR RECEITA"\n')
    # atualizar_receita()

# elif menu_quest == 5:  #
#     print('\nVOCÊ ESCOLHEU ""\n')
#     # Controle_Do_Financeiro.


