import mysql.connector


banco = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    passwd = '',
    database = 'caser_engenharia'
)

cursor = banco.cursor()

def registrar_receita():

    class RegistrarReceita():

        def __init__(self):

            self.__contrato = input('Contrato :')
            self.emissao = input('Emissão : ')
            self.__NF = input('NF : ')
            self.banco = input('Banco : ')
            self.__valor_da_nota = float(input('Valor da nota : \033[32mR$\033[0;0m'))
            self.data_recebimento = input('Data de recebimento : ')
            self.material = float(input('Material : \033[32mR$\033[0;0m'))
            self.mao_de_obra = float(input('Mão de obra : \033[32mR$\033[0;0m'))
            self._IMP_FED  = float(input('IMP.FED : \033[32mR$\033[0;0m'))
            self._ISS = float(input('ISS : \033[32mR$\033[0;0m'))
            self.INSS = float(input('INSS : \033[32mR$\033[0;0m'))
            self.glosa = float(input('Glosa : \033[32mR$\033[0;0m'))
            self._data = input('Data : ')
            self.total_desconto = float(self._IMP_FED + self._ISS + self.INSS + self.glosa
                                   + self.material + self.mao_de_obra)
            self.__valor_creditado = (self.__valor_da_nota - self.total_desconto)

            comando_mysql = f'INSERT INTO receitas_adm (contrato, emissao, NF, banco, valor_da_nota' \
                            f', valor_creditado, data_recebimento, material, mao_de_obra, IMP_FED, ISS' \
                            f', INSS, glosa, total_descontos, data) ' \
                            f'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

            registra_receita = (str(self.__contrato), str(self.emissao), str(self.__NF), str(self.banco)
                                , str(self.__valor_da_nota), str(self.__valor_creditado), str(self.data_recebimento)
                                , str(self.material), str(self.mao_de_obra), str(self._IMP_FED), str(self._ISS)
                                , str(self.INSS), str(self.glosa), str(self.total_desconto), str(self._data))

            cursor.execute(comando_mysql, registra_receita)
            banco.commit()

            print('')
            print('\n***** --- REGISTRADO --- *****\n')

            print(f"Contrato : {self.__contrato}")
            print(f"Emissão : {self.emissao}")
            print(f"NF: {self.__NF}")
            print(f"Banco : {self.banco}")
            print(f"Valor da nota : R${self.__valor_da_nota}")
            print(f"Data recebimento : {self.data_recebimento}")
            print(f"Material : R${self.material}")
            print(f"Mão de obra : R${self.mao_de_obra}")
            print(f"IMP.FED : R${self._IMP_FED}")
            print(f"ISS : R${self._ISS}")
            print(f"Glosa : R${self.glosa}")
            print(f"Data : {self._data}")
            print(f"Total de descontos : R${self.total_desconto}")
            print(f"Valor creditado : R${self.__valor_creditado}")

            print('\n***** --- REGISTRADO --- *****\n')
            print('')

        def __repr__(self):
            return RegistrarReceita()

    RegistrarReceita()

def geral_receitas():

    valor_liquido = 0
    valor_bruto = 0

    comando_mysql = f'SELECT VALOR_CREDITADO FROM receitas_adm'
    cursor.execute(comando_mysql)
    resultado = cursor.fetchall()

    for c in resultado:
        c = float(c[0])
        valor_liquido += c

    comando_mysql = f'SELECT valor_da_nota FROM receitas_adm'
    cursor.execute(comando_mysql)
    resultado = cursor.fetchall()

    for c in resultado:
        c = float(c[0])
        valor_bruto += c

    print(f'	\033[1;31mValor bruto : R$ {valor_bruto}\033[0;0m')
    print('')
    print(f'	\033[1;31mValor líquido : R$ {valor_liquido}\033[0;0m')

def atualizar_receita():
    pass

def ver_receita():
    comando_mysql = f'SELECT *FROM receitas_adm'
    cursor.execute(comando_mysql)
    banco_de_dados = cursor.fetchall()

    for c in banco_de_dados:
        print(f'\n --- Crontato "{c[1]}"" --- ')
        print('')
        print(f"\nContrato : {c[1]}")
        print(f"Emissão : {c[2]}")
        print(f"NF : {c[3]}")
        print(f"Banco : {c[4]}")
        print(f"Valor da nota : R${c[5]}")
        print(f"Valor creditado : R${c[6]}")
        print(f"Data de recebimento : {c[7]}")
        print(f"Material : {c[8]}")
        print(f"Mão de obra : {c[9]}")
        print(f"IMP. FED. : R${c[10]}")
        print(f"ISS : R${c[11]}")
        print(f"Glosa : R${c[12]}")
        print(f"Total de descontos : R${c[13]}")
        print(f"Data : {c[14]}")
        print('')

def menu_receita():

    print('')
    print('*' * 40)
    print('              RECEITA ADM')
    print('*' * 40)

    print('\n[1] REGISTRAR RECEITA'
          '\n[2] VER RECEITA'
          '\n[3] ATUALIZAR RECEITA'
          '\n[4] BALANÇO GERAL DAS RECEITAS'
          '\n[5] VOLTAR')

    menu_quest = int(input('ESCOLHA UMA DAS OPÇÕES ACIMA : '))

    if menu_quest == 1:  #
        print('\nVOCÊ ESCOLHEU "REGISTRAR RECEITA"\n')
        registrar_receita()

    elif menu_quest == 2: #
        print('\nVOCÊ ESCOLHEU "VER RECEITA"\n')
        ver_receita()

    elif menu_quest == 3: #
        print('\nVOCÊ ESCOLHEU "ATUALIZAR RECEITA"\n')
        atualizar_receita()

    elif menu_quest == 4:  #
        print('\nVOCÊ ESCOLHEU "BALANÇO GERAL DAS RECEITAS"\n')
        geral_receitas()

    # elif menu_quest == 5:  #
    #     print('\nVOCÊ ESCOLHEU ""\n')
    #     # Controle_Do_Financeiro.
