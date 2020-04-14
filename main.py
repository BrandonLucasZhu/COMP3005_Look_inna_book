from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import os
from models import db, Books, Users, login_manager, Published, Publisher, Author, Wrote ,Order_track, Confirm_purchase, Checkout , Views
from flask_login import current_user, login_user
from datetime import datetime, timedelta
from datetime import date

bookstore = Flask(__name__, template_folder='templates')           

app = Flask(__name__, template_folder='templates')
app.config.from_object('config.Config')
app.config.from_pyfile('config.py')
#the set up url -----> postgresql://username:pass@localhost/database_name    
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root619@localhost/bookstore_project_v1'


db.init_app(app)
#initiate login manager
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_info):
    
    return user_info

#render home page
@app.route("/",methods=['GET', 'POST'])                  
def index(): 
    #main directory of folder
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    main_dir = os.path.dirname(working_dir) 

    #check if user is logged in
    if session.get('logged_in_user') is None:
        username = "guest"
    else:
        username = session.get('logged_in_user')

    return render_template('index.html', username=username)

#render store page
@app.route("/store",methods=['GET', 'POST'])                  
def store(): 
    #store directory of folder
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    main_dir = os.path.dirname(working_dir)
    
    #Query all books in books relation 
    bookstock = db.session.query(Books.title,Books.book_id, Books.isbn, Author.firstname, Author.lastname, Publisher.publisher_name,  Books.book_stock, Books.price)\
    .filter(Books.book_id == Wrote.book_id).filter(Books.isbn == Wrote.isbn).filter(Author.a_id == Wrote.a_id) \
    .filter(Published.book_id == Books.book_id).filter(Published.isbn == Books.isbn).filter(Publisher.p_id == Published.p_id)


    #Check is user is logged in
    if session.get('logged_in_user') is None:
        username = "guest"
    else:
        username = session.get('logged_in_user')

        if request.method == 'POST':  
            if request.form['add_to_cart'] == "Add To Cart":
                #print(request.form['bookisbn'])
                #print(request.form['bookid'])

                #store isbn's into the cart
                temp_cart = session['user_cart']
                temp_cart.append(request.form['bookisbn'])
                session['user_cart'] = temp_cart
                
    #print(bookstock)
    return render_template('store.html', bookstock=bookstock, username=username)

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
                #save instance of user and id of user
                session['logged_in_user'] = request.form['username']
                session['user_id'] = loginval.first().id
                session['user_cart'] = []
                return redirect(url_for('index'))

        #if signup button is clicked on HTML side name == button value(Sign Up)
        if  request.form['submit_but'] == "Sign Up": 
            return redirect(url_for('signup_page'))          
    
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session['logged_in_user'] = None
    session['user_id'] = None
    session['user_cart'] = None
    return redirect(url_for('index'))    

#render signup page
@app.route("/signingup",methods=['GET', 'POST'])                  
def signup_page():

    if request.method == 'POST':
       
        #if login button is clicked on HTML side name == button value(Login)
        if request.form['submit_but'] == "Complete Sign Up":
            id = db.session.query(Users.id).count() + 1
            print(id)
            user_signup = Users(id,request.form['firstname'], request.form['lastname'], request.form["street_num"],\
            request.form["street_name"], request.form["postalcode"],\
            request.form["country"], request.form["province"],\
            request.form["phone_number"], request.form["email"],\
            request.form["username"], request.form["password"])
            
            #print(request.form["firstname"])
            db.session.add(user_signup)
            db.session.commit()
            return redirect(url_for('login'))

    return render_template('signup.html')     

#render Cart
@app.route("/cart",methods=['GET', 'POST'])                  
def cart(): 
    #store directory of folder
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    main_dir = os.path.dirname(working_dir)
    showbooks = []
    #Check is user is logged in
    len_books = 0
    if session.get('logged_in_user') is None:
        username = "guest"
    else:
        username = session.get('logged_in_user')
        disp_cart = session['user_cart']
        
        for i in range(len(disp_cart)):
            showbooks.append(db.session.query(Books.title, Books.isbn, Books.price).filter_by(isbn = disp_cart[i]).first())
       
        len_books = len(showbooks)

    if request.method == 'POST':
        if request.form['checkout'] == "Checkout":
            return redirect(url_for('checkout'))    

    return render_template('cart.html', username=username, showbooks=showbooks, len_books=len_books)


@app.route("/checkout",methods=['GET', 'POST'])                  
def checkout():
    #store directory of folder
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    main_dir = os.path.dirname(working_dir)
    showbooks = []
    len_books = 0
    disp_cart = session['user_cart']
    print(disp_cart)
    username = session.get('logged_in_user')
    sub_total = 0
    for i in range(len(disp_cart)):
        showbooks.append(db.session.query(Books.title, Books.isbn, Books.price).filter_by(isbn = disp_cart[i]).first())
    
        sub_total += float(db.session.query(Books.price).filter_by(isbn = disp_cart[i]).first().price)

    sub_total = round(sub_total + 5.99,2)
    total = round(sub_total*1.13,2)
    #print(sub_total)
    #print(total)
    len_books = len(showbooks)

    if request.method == 'POST':
        if request.form['confirm'] == "Confirm Purchase":
            #update tables views, checkout, and confirm-purchase
            #and update-order track
            
            
            checkoutid = db.session.query(Checkout.c_out_id).count() + 1
            #add checkout
            add_checkout = Checkout(checkoutid, request.form['credit_card'], date.today(),"5.99",request.form['total'])
            db.session.add(add_checkout)
            db.session.commit()

            #add order_track
            orderid = db.session.query(Order_track.order_id).count() + 1
            add_order_track = Order_track(orderid, date.today(), str(datetime.now() + timedelta(hours=5)), str(datetime.now() + timedelta(hours=200)), "Seattle")
            db.session.add(add_order_track)
            db.session.commit()


            #add a view for this customer
            id = session['user_id']
            
            add_viewer = Views(id,checkoutid)
            db.session.add(add_viewer)
            db.session.commit()

            #add complete purchase
            add_cp = Confirm_purchase(checkoutid, orderid, request.form['total'])
            db.session.add(add_cp)
            db.session.commit()

            return redirect(url_for('ordercomplete')) 


    return render_template('checkout.html', username=username, showbooks=showbooks, len_books=len_books,\
    sub_total=sub_total, total=total)

@app.route("/ordercomplete",methods=['GET', 'POST'])                  
def ordercomplete():
    username = session.get('logged_in_user')
    return render_template('ordercomplete.html', username=username)


if __name__ == "__main__":  
    app.run()   