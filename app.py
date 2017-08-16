from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
import datetime
from sqlalchemy import create_engine

engine = create_engine('sqlite:///tutorial.db', echo=True)
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('FrontPage.html')
    else:
        return render_template('FrontPage.html')
        #return "Hello " + session['user'] + "!  <a href='/logout'>Logout</a>"
 
@app.route('/lesson1')
def go_to_lesson1():
    return render_template('JavaLesson1.html')

@app.route('/lesson2')
def go_to_lesson2():
    return render_template('JavaLesson2.html')

@app.route('/lesson3')
def go_to_lesson3():
    return render_template('JavaLesson3.html')

@app.route('/lesson4')
def go_to_lesson4():
    return render_template('JavaLesson4.html')

@app.route('/lesson5')
def go_to_lesson5():
    return render_template('JavaLesson5.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
        session['user'] = POST_USERNAME
    else:
        flash('Wrong password')
    return home()

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()

@app.route('/newUser', methods=['POST'])
def newUser():
    POST_USERNAME1 = str(request.form['username1'])
    POST_PASSWORD1 = str(request.form['password1'])
    Session = sessionmaker(bind=engine)
    s = Session()
    user = User(POST_USERNAME1, POST_PASSWORD1)
    s.add(user)
    s.commit()
    s.commit()
    session['logged_in'] = True
    #TODO: LOG PERSON IN WHEN THEY CREATE AN ACCOUNT.  ESSENTIALLY CREATE NEW DO_ADMIN_LOGIN() METHOD
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
