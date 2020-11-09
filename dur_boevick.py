import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("""DELETE from films
        WHERE genre IN (
    SELECT id FROM genres 
        WHERE title = 'боевик') AND duration >= 90 """).fetchall()

    con.commit()
