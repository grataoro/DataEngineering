#from models import Jogo

class GameDao:
    def __init__(self,db):
        self.__db = db 

    def save(self, game):
        cursor = self.__db.connection.cursor()    

        SQL_CREATE_GAME = """INSERT INTO game (name, category,console) 
                             VALUES (%s,%s,%s)"""

        cursor.execute(SQL_CREATE_GAME,(game.name,game.category,game.console))
        self.__db.connection.commit()
        return game

    def retirn_games():

        SQL_GET_GAMES = """
        
        SELECT * FROM GAMES;
        
        """
        

        pass    
