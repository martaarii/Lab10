from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.state import State
class Contiguity_dao():
    def __init__(self):

        pass

    def get_connesioni(self, anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore nella ricerca del database")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct state1no,state2no,year from contiguity
                    where year <= %s 
                    and conttype = 1"""
            cursor.execute(query, (anno, ))
            for row in cursor:
                result.append(Contiguity(row["state1no"], row["state2no"], row["year"]))
            cursor.close()
            cnx.close()
        return result


class State_dao():
    def get_stati(self, anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore nella ricerca del database")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * from country where CCode in
                    (select state1no from contiguity c where year <= %s )"""
            cursor.execute(query, (anno, ))
            for row in cursor:
                result.append(State(row["StateAbb"], row["CCode"], row["StateNme"]))
            cursor.close()
            cnx.close()
        return result

    def get_all_stati(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore nella ricerca del database")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select StateNme from country 
                        """
            cursor.execute(query)
            for row in cursor:
                result.append(row["StateNme"])
            cursor.close()
            cnx.close()
        return result
