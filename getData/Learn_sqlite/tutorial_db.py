# read and write in the databse
"""
a lire :
https://docs.python.org/fr/3/library/sqlite3.html
https://pynative.com/python-sqlite/

"""

import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")

# verifie si la table a bien été crée
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())

# insert data in table movie
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()

res = cur.execute("SELECT score FROM movie")
print(res.fetchall())

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)


con.close()

new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()

print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
new_con.close()