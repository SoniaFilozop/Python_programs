import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("""UPDATE films 
        SET duration = duration * 2
         WHERE genre IN (
    SELECT id FROM genres 
        WHERE title = 'фантастика')""").fetchall()

    con.commit()
