from flask import Flask, flash, redirect, render_template, request
import sqlite3


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        connection = sqlite3.connect('bd.db')
        cursor = connection.cursor()
        bdd = cursor.execute('SELECT * FROM bd').fetchall()
        return render_template('index.html', bdd=bdd)

    else:
        name = request.form.get('Name')
        birthday = request.form.get('Birthday')

        connection = sqlite3.connect('bd.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO bd (name,bd_date)  VALUES(?,?)', (name, birthday))

        connection.commit()
        connection.close()
        return redirect('/')

@app.route("/edit_user/<string:id>",methods=['GET','POST'])
def edit_user(id):
    if request.method=='GET':
        uname=request.form['Name']
        ubd=request.form['Birthday']
        con=sqlite3.connect("bd.db")
        cur=con.cursor()
        cur.execute("update bd set name=?,bd_date=? where id=?",(uname,ubd,id))
        con.commit()
        flash('User Updated','success')
        return render_template('index.html')
    else:
     con=sqlite3.connect("bd.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from bd where id=?",(id,))
    data=cur.fetchone()
    return render_template("edit.html",data=data)

@ app.route('/deletebdd/<string:name>', methods=['POST'])
def deletebdd(name):
    name = request.form('Name')
    connection = sqlite3.connect('bd.db')
    cursor = connection.cursor()
    dlt1 = cursor.execute('DELETE FROM bd WHERE name=?', (name,)).fetchall()
    connection.commit()
    connection.close()
    return render_template('index.html', dlt1=dlt1)


