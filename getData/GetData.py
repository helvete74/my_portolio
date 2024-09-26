from connect_sqlite import Connectdb
from yfinance_API import Quote

from datetime import datetime, timedelta

if __name__ == '__main__':
    # Calcul de la date du jour précédent
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_date_str = yesterday.strftime('%Y-%m-%d')  # Formater en 'YYYY-MM-DD'

    my_db = Connectdb("../portfolioDB.db")
    conn, cur = my_db.connect()

    res = cur.execute("SELECT symbol FROM my_quote ORDER BY symbol")
    rows = res.fetchall()
    print("rows:", rows)

    for row in rows:

        symbol = row[0]
        quote = Quote(symbol)
        info = quote.info()
        print("1 symbol:", quote.get_symbol())
        #print(quote.get_name())

        #(last_close_value, last_close_date) = quote.get_last_close() # from historical value
        last_close_value = quote.get_previous_close()
        # insert info in quote_info

        cur.execute("DELETE FROM quote_info WHERE symbol=?", (quote.get_symbol(),) )
        cur.execute("INSERT into quote_info(symbol, exchange, last_close_price, last_close_date, short_name, currency)"
                    "VALUES(?,?,?,?,?,?)",(quote.get_symbol(), quote.get_exchange(),last_close_value, yesterday_date_str, quote.get_name(), quote.get_currency()) )

    conn.commit()
    cur.close()
    my_db.close()
