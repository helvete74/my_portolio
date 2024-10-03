import sqlite3
from sqlite3 import Connection

"""
a lire :
https://docs.python.org/fr/3/library/sqlite3.html
https://pynative.com/python-sqlite/

"""
class Connectdb:
    def __init__(self, database_name):
        self.database_name = database_name
        self.sqlite_connection = None
        self.cursor = None

    def connect(self):
        try:
            sqlite_connection: Connection = sqlite3.connect(self.database_name)
            cursor = sqlite_connection.cursor()
            print("Database created and Successfully Connected to SQLite")

            """
            sqlite_select_query = "select sqlite_version();"
            cursor.execute(sqlite_select_query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            cursor.close()
            """
            self.sqlite_connection = sqlite_connection
            self.cursor = cursor
            return sqlite_connection, cursor
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

    def close(self):
        self.sqlite_connection.close()
        print("The SQLite connection is closed")

if __name__ == '__main__':
    my_db = Connectdb("testDB.db")
    conn, cur = my_db.connect()

    cur.execute("CREATE TABLE quote(symbol, name)")
    cur.execute("""
        INSERT INTO quote(symbol) VALUES
            ('MSFT'),
            ('GOOGL'),
            ('AAPL')
    """)
    conn.commit()


    for row in cur.execute("SELECT symbol, name FROM quote ORDER BY symbol"):
        print(row)
        symbol = row[0]
        if symbol =="GOOGL" :
            # insert name
            cur.execute("UPDATE quote set name=? WHERE symbol=?", ("GOOGLE from my", "GOOGL") )
            conn.commit()

    cur.close()
    my_db.close()

