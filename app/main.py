#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template, request
import sqlite3
from datetime import datetime
#from sqlalchemy import Column, Integer, String, Text, DateTime, SQLAlchemy


#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"


#「/thread」へアクセスがあった場合に、「thread.html」を返す
@app.route("/thread", methods=["GET"])
def index():
    #conn = sqlite3.connect('./app/sample1.db')
    #cur = conn.cursor()
    #articles = cur.execute("select * from board")
    return render_template("thread.html", thread='hoge')


class Article:
    def __init__(self, datetime, name, article):
        self.datetime = datetime
        self.name = name
        self.article = article


@app.route("/thread", methods=["POST"])
def result():
    times = datetime.now()
    article = request.form['article']
    name = request.form['name']
    conn = sqlite3.connect('./app/sample1.db')
    cur = conn.cursor()
    insert_sql = 'insert into board (datetime, name, article) values (?,?,?)'
    users = [(times, name, article)]
    #users = [(datetime.now(), request.form['name'], request.form['article'])]
    cur.executemany(insert_sql, users)
    articles = cur.execute("select * from board")
    conn.commit()
    return render_template("thread.html",
                                articles=articles)



#main.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)