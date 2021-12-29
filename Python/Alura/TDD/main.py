class Name:
    
    def __init__(self, name):
        self.__name = name

    @property
    def user_name(self):
        return self.__name

class Bet:

    def __init__(self, bet):
        self.__bet = bet
    
    @property
    def user_bet(self):
        return self.__bet

class DataBase:

    def __init__(self, desc):
        self.db = (desc)
        self.__db = []
    
    @property
    def users(self):
        return self.__db