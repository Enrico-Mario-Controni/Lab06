import mysql.connector


class User:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database="autonoleggio"
        )
        self.cursor = self.connection.cursor()


    def get_list_automobili(self):
        self.cursor.execute("SELECT * FROM automobile")
        return self.cursor.fetchall()

    def ricerca(self, valore):
        self.cursor.execute("SELECT * FROM automobile WHERE modello = %s", (valore,))
        return self.cursor.fetchall()

