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
    
class Result:

    def __init__(self, db):
        global users

        index = 0
        self.__users = []
        users_indexs = []
        bets = [c[1].user_bet for c in db.users]

        for bet in bets:
            if bet == max(bets):
                users_indexs.append(index)
            index += 1

        for index in users_indexs:
            user = db.users[index]
            name, bet = user[0].user_name, user[1].user_bet
            user = (name, bet, index)
            self.__users.append(user)

    @property
    def result(self):
        name = self.__users[0][0]
        bet = self.__users[0][1]
        index = self.__users[0][2]
        return f'O usuário {name}({index}) fez o maior bet de {bet}'