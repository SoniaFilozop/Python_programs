import sqlite3

name = input()
con = sqlite3.connect(name)
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films
    WHERE title LIKE '%Астерикс%' AND title NOT LIKE '%Обеликс%'""").fetchall()
for elem in result:
    print(list(elem)[0])

con.close()
