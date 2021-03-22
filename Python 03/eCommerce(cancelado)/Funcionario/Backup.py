# from typing import Union

import random


dict_Funcionário = dict() # Contém todas as INFO's dos funcionários
dict_nRegistro = dict() # Adiciona todas as INFO's dos funcionários junto com seu número de registro (por ordem)

list_Funcionário_Total = list() # Lista que contém todos os funcionários já registrados
list_Funcionário_Novos = list() # Lista que adiciona os novos funcionários a lista total de funcionários

def registar_funcionário() -> dict:

    while True:

        try:
            func_quest: int = int(input('\nDeseja registrar quantos funcionário ? '))
            break

        except:
            print('\n!Erro')
            print('Use apenas valores valídos')
            continue

    class RegistrarFuncionário():

        def __init__(self):

            self.__nome: str = str(input('\nNome do Funcionário : '))
            self.__documento: str = input('Documento do Funcionário : ')
            self.salário: int = input('Salário do Funcionário : ')
            self.função: str = input('Função do Funcionário : ')
            self.__nID: int = random.randrange(0, 124897)

            dict_Funcionário['ID']: int = self.__nID
            dict_Funcionário['Nome']: str = self.__nome.title()
            dict_Funcionário['Documento']: str = self.__documento
            dict_Funcionário['Função']: str = self.função
            dict_Funcionário['Salário']: int = self.salário

            list_Funcionário_Novos.append(dict_Funcionário.copy())
                # Adiciona os funcionários a lista de novos funcionários

        def __repr__(self):
            return RegistrarFuncionário()

    for c in range(0, func_quest):
        RegistrarFuncionário()

    print('')
    for Funcionário in list_Funcionário_Novos:
        print(Funcionário, '- Registrado')

    for x in list_Funcionário_Novos:

        dict_nRegistro['nRegistro']: int = len(list_Funcionário_Total) + 1
        dict_nRegistro['INFO']: str = x
        list_Funcionário_Total.append(dict_nRegistro.copy())
            # Adiciona os novos funcionários a lista total de funcionários

    list_Funcionário_Novos.clear()
        # Limpa toda a lista de novos clientes após adicionalos a lista geral de clientes

def atualização_cadastral() -> dict:

    quest: int = int(input('Digite o número de registro do funcionário : '))
    index: int = quest - 1

    class AtualizaFuncionário():

        def __init__(self):

            self.__nome: str = str(input('\nNome do Funcionário : '))
            self.__documento: str = input('Documento do Funcionário : ')
            self.salário: int = input('Salário do Funcionário : ')
            self.função: str = input('Função do Funcionário : ')
            self.__nID: int = list_Funcionário_Total[index]['INFO']['ID']

            list_Funcionário_Total[index]['INFO']['Nome'] = self.__nome.title()
            list_Funcionário_Total[index]['INFO']['Documento'] = self.__documento
            list_Funcionário_Total[index]['INFO']['Salário'] = self.salário
            list_Funcionário_Total[index]['INFO']['Função'] = self.função
            list_Funcionário_Total[index]['INFO']['ID'] = self.__nID

        def __repr__(self):
            return AtualizaFuncionário()

    AtualizaFuncionário()
    print('\n', list_Funcionário_Total[index]['INFO'], '- ATUALIZADO')

def banco_funcionário() -> list:
    for c in list_Funcionário_Total:
        print(c)