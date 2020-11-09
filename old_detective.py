import sqlite3

name = input()
con = sqlite3.connect(name)
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films 
    WHERE genre IN (
SELECT id FROM genres 
    WHERE title = 'детектив') AND year >= 1995 AND year <= 2000""").fetchall()
for elem in result:
    print(list(elem)[0])

con.close()