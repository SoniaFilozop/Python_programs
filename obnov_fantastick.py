import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("""DELETE from films
        WHERE genre IN (
    SELECT id FROM genres 
        WHERE title = 'фантастика') AND duration > 90 AND year < 2000""").fetchall()

    con.commit()