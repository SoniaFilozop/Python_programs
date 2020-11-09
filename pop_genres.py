import sqlite3

name = input()
con = sqlite3.connect(name)
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT title FROM Genres
    WHERE id IN (
SELECT genre FROM Films 
    WHERE year = 2010 OR year = 2011)""").fetchall()
for elem in result:
    print(list(elem)[0])

con.close()
