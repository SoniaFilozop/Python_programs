import sqlite3

name = input()
con = sqlite3.connect(name)
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT year FROM Films
    WHERE title LIKE 'Х%'""").fetchall()
for elem in result:
    print(list(elem)[0])

con.close()