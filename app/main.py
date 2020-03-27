#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template, request
import sqlite3
from datetime import datetime
#import pymysql.cursors




#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"


#「/thread」へアクセスがあった場合に、「thread.html」を返す
@app.route("/thread")
def index():
    return render_template("thread.html", thread='hoge')

class Article:
    def __init__(self, datetime, name, article):
        #self.id = id
        self.datetime = datetime
        self.name = name
        self.article = article


''' 
def register(self, datetime, name, article):
    conn = sqlite3.connect('sample1.db')
    cur = conn.cursor()
    insert_sql = 'insert into board(datetime, name, article) values (?,?,?)'
    users = [datetime, name, article]
    cur.executemany(insert_sql, users)
    conn.commit()
'''

@app.route("/thread", methods=["POST"])
def result():
    time = datetime.now()
    article = request.form['article']
    name = request.form['name']
    #register(time, name, article)
    conn = sqlite3.connect('sample1.db')
    cur = conn.cursor()
    insert_sql = 'insert into board(datetime, name, article) values (?,?,?)'
    users = [datetime, name, article]
    cur.executemany(insert_sql, users)
    conn.commit()





#main.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)