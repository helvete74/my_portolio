from tools.connect_sqlite import Connectdb

if __name__ == '__main__':
    my_db = Connectdb("../portfolioDB_create.db")
    conn, cur = my_db.connect()

    # my_quote
    cur.execute("CREATE TABLE 'my_quote'('symbol' TEXT, 'my_name' TEXT, PRIMARY KEY('symbol') )")
    conn.commit()

    # quote_info
    cur.execute("CREATE TABLE 'quote_info'("
                " 'symbol' TEXT NOT NULL UNIQUE,"
                " 'exchange' TEXT, "
                " 'last_close_price' NUMERIC, "
                " 'last_close_date' INTEGER, "
                " 'short_name' TEXT, "
                " 'currency' TEXT, "
                "PRIMARY KEY('symbol'), "
                "FOREIGN KEY('symbol') REFERENCES 'my_quote'('symbol')"
                ")"
    )
    conn.commit()

    cur.close()
    my_db.close()