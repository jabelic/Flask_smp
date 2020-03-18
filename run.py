from app.main import app
import sqlite3

'''conn = sqlite3.connect('sample1.db')
c = conn.cursor()
c.execute("create table board(id integer primary key autoincrement,datetime numeric,name text not null,article text not null)")

conn.commit()'''

if __name__ == "__main__":
    app.run()