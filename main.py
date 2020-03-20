from flask import Flask, render_template, url_for, request, redirect 
from flask_sqlalchemy import SQLAlchemy
import os
from models import db, Books, Users
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

bookstore = Flask(__name__, template_folder='templates')           

app = Flask(__name__, template_folder='templates')
app.config.from_object('config.Config')
app.config.from_pyfile('config.py')
#the set up url -----> postgresql://username:pass@localhost/database_name    
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root619@localhost/bookstore_project_v1'
db.init_app(app)


#render home page
@app.route("/",methods=['GET', 'POST'])                  
def index(): 
    #main directory of folder
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    main_dir = os.path.dirname(working_dir) 

    return render_template('index.html')

#render store page
@app.route("/store",methods=['GET', 'POST'])                  
def store(): 
    #store directory of folder
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    main_dir = os.path.dirname(working_dir)

    #Query all books in books relation 
    bookstock = Books.query.all()
    
    return render_template('store.html', bookstock=bookstock)

#render login page
@app.route("/login",methods=['GET', 'POST'])                  
def login(): 
    #store directory of folder
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    main_dir = os.path.dirname(working_dir) 
    error = None
   
    if request.method == 'POST':
        #if login button is clicked on HTML side name == button value(Login)
        if request.form['submit_but'] == "Login":
            #login validation -> check if database has records
            loginval = Users.query.filter_by(username = request.form['username'], password = request.form['password'])
            if loginval.count() == 0:
                error = 'Invalid Credentials. Please try again.'
            else:
                return redirect(url_for('store'))
        #if signup button is clicked on HTML side name == button value(Sign Up)
        if  request.form['submit_but'] == "Sign Up": 
            return redirect(url_for('signup_page'))          
    
    return render_template('login.html', error=error)

#render signup page
@app.route("/signingup",methods=['GET', 'POST'])                  
def signup_page():
    return render_template('signup.html')               

if __name__ == "__main__":  
    app.run()   