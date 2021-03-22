import mysql.connector


banco = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    passwd = '',
    database = 'caser_engenharia'
)

cursor = banco.cursor()


def registrar_despesa():

    class RegistrarDespesa():

        def __init__(self):

            self.descricao = input('Obra/Descrição : ')
            self._tipo_de_conta = input('Tipo de gasto : ')
            self._recebedor = input('Recebedor : ')
            self.modo_de_pagamento = input('Método de pagamento : ')
            self._emissao = input('Emissão : ')
            self.__NF = input('NF : ')
            self._boleto = input('Boleto : ')
            self.__valor_da_nota = input('Valor da nota : R$')
            self.__valor_boleto = input('Valor do boleto : R$')
            self._data_vencimento = input('Data de vencimento : ')
            self.codigo_barras = input('Codigo de barras : ')
            self.data_pagamento = input('Data pagamento : ')

            comando_mysql = f'INSERT INTO despesas_adm (descricao, 	tipo_de_conta, 	recebedor, modo_de_pagamento, emissao' \
                            f',NF, boleto, valor_da_nota, valor_boleto, data_vencimento, codigo_barras,	data_pagamento)' \
                            f' VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

            registrar_despesa = (str(self.descricao), str(self._tipo_de_conta), str(self._recebedor), str(self.modo_de_pagamento)
                                ,str(self._emissao), str(self.__NF), str(self._boleto), str(self.__valor_da_nota)
                                , str(self.__valor_boleto), str(self._data_vencimento), str(self.codigo_barras)
                                , str(self.data_pagamento))

            cursor.execute(comando_mysql, registrar_despesa)
            banco.commit()

            print('')
            print('\n***** --- REGISTRADO --- *****\n')

            print(f"Obra/Descrição : {self.descricao}")
            print(f"Tipo de conta : {self._tipo_de_conta}")
            print(f"Recebedor : {self._recebedor}")
            print(f'Método de pagamento : {self.modo_de_pagamento}')
            print(f"Emissão : {self._emissao}")
            print(f"NF : {self.__NF}")
            print(f"Boleto : {self._boleto}")
            print(f"Valor da nota : R${self.__valor_da_nota}")
            print(f"Valor do boleto : R${self.__valor_boleto}")
            print(f"Data de vencimento : {self._data_vencimento}")
            print(f"Codigo de barras : {self.codigo_barras}")
            print(f"Data de pagamento : {self.data_pagamento}")

            print('\n***** --- REGISTRADO --- *****\n')
            print('')

        def __repr__(self):
                return RegistrarDespesa()

    RegistrarDespesa()

def geral_despesas():
    pass

def ver_despesas():
    comando_mysql = f'SELECT *FROM despesas_adm'
    cursor.execute(comando_mysql)
    banco_de_dados = cursor.fetchall()

    for c in banco_de_dados:
        print(f'\n --- DESCRIÇÃO {c[1]} --- ')
        print(f"\nDescrição : {c[1]}")
        print(f"Tipo de conta : {c[2]}")
        print(f"Recebedor : {c[3]}")
        print(f'Método de pagamento : {c[4]}')
        print(f"Emissão : {c[5]}")
        print(f"NF : {c[6]}")
        print(f"Boleto : {c[7]}")
        print(f"Valor da nota : R${c[8]}")
        print(f"Valor do boleto : R${c[9]}")
        print(f"Data do vencimento : {c[10]}")
        print(f"Código de barras : {c[11]}")
        print(f"Data do pagamento : '{c[12]}'")
        # print(f"'{c[11]}'")
        print('')

def atualizar_despesas():
    pass

def menu_despesas():
    print('')
    print('*' * 40)
    print('              DESPESAS ADM')
    print('*' * 40)

    print('\n[1] REGISTRAR DESPESA'
          '\n[2] VER DESPESAS'
          '\n[3] ATUALIZAR DESPESA'
          '\n[4] BALANÇO GERAL DAS DESPESAS'
          '\n[5] VOLTAR')

    menu_quest = int(input('\nESCOLHA UMA DAS OPÇÕES ACIMA : '))

    if menu_quest == 1:  #
        print('\nVOCÊ ESCOLHEU "REGISTRAR DESPESA"\n')
        registrar_despesa()

    elif menu_quest == 2: #
        print('\nVOCÊ ESCOLHEU "VER DESPESAS"\n')
        ver_despesas()

    elif menu_quest == 3: #
        print('\nVOCÊ ESCOLHEU "ATUALIZAR DESPESA"\n')
        atualizar_despesas()

    elif menu_quest == 4:  #
        print('\nVOCÊ ESCOLHEU "BALANÇO GERAL DAS DESPESAS"\n')
        geral_despesas()

    # elif menu_quest == 5:  #
    #     print('\nVOCÊ ESCOLHEU "VOLTAR"\n')
    #     # Controle_Do_Financeiro.
