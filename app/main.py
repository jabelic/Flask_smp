#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template
import sqlite3

#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"


#「/index」へアクセスがあった場合に、「thread.html」を返す
@app.route("/thread")
def index():
    return render_template("thread.html")

class Article:
    def __init__(self, id, datetime, name, article):
        self.id = id
        self.datetime = datetime
        self.name = name
        self.article = article
    def register(self, datetime, name, article):
        conn = sqlite3.connect('sample1.db')
        cur = conn.cursor()
        insert_sql = 'insert into board(datetime, name, article) values (?,?,?)'
        users = [datetime, name, article]
        cur.executemany(insert_sql, users)
        conn.commit()





#main.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)