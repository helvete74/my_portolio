from connect_sqlite import Connectdb
from yfinance_API import Quote

if __name__ == '__main__':
    my_db = Connectdb("../portfolioDB.db")
    conn, cur = my_db.connect()

    res = cur.execute("SELECT symbol FROM quote ORDER BY symbol")
    rows = res.fetchall()
    print(rows)

    for row in rows:

        symbol = row[0]
        quote = Quote(symbol)
        info = quote.info()
        print(quote.get_symbol())
        print(quote.get_name())
        # insert name
        cur.execute("UPDATE quote set name=? WHERE symbol=?", (quote.get_name(), quote.get_symbol()) )
    conn.commit()
    cur.close()
    my_db.close()
