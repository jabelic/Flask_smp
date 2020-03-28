from app.main import app
import sqlite3


try:
    conn = sqlite3.connect('./app/sample1.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS board")
    cur.execute("CREATE TABLE IF NOT EXISTS board(id INTEGER PRIMARY KEY,datetime TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')), name TEXT, article TEXT)")
    conn.commit()
    cur.close()
    conn.close()
except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])


if __name__ == "__main__":
    app.run()