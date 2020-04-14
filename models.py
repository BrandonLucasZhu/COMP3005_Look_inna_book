#import database connection
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager


db = SQLAlchemy()
login_manager = LoginManager()

class Books(db.Model):

    __tablename__ = "books"
    book_id = db.Column(db.Integer(), primary_key=True)
    isbn = db.Column(db.String(), primary_key=True)
    title = db.Column(db.String())
    publication_date = db.Column(db.String())
    price = db.Column(db.String())
    book_stock = db.Column(db.Integer())

    def __init__(self, book_id, title, isbn, genre, publication_date, price,book_stock):
        self.book_id = book_id
        self.title = title
        self.isbn = isbn
        self.publication_date = publication_date
        self.price = price
        self.book_stock = book_stock

    def __repr__(self):
        return '<title %r>' % (self.title, self.isbn, self.publication_date)
        

class Users(db.Model,UserMixin):

    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    street_num = db.Column(db.String())
    street_name = db.Column(db.String())
    postalcode = db.Column(db.String())
    country = db.Column(db.String())
    province = db.Column(db.String())
    phone_number = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, id, firstname, lastname, street_num,street_name, postalcode, country, province, phone_number, email, username, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.street_num = street_num
        self.street_name = street_name
        self.postalcode = postalcode
        self.country = country
        self.province = province
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return self.id

class Published(db.Model):
    __tablename__ = "published"
    p_id = db.Column(db.Integer(), primary_key=True)
    book_id = db.Column(db.Integer(), primary_key=True)
    isbn = db.Column(db.String(), primary_key=True)

class Publisher(db.Model):

    __tablename__ = "publisher"
    p_id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(), unique=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    street_num = db.Column(db.String())
    postalcode = db.Column(db.String())
    country = db.Column(db.String())
    province = db.Column(db.String())
    phone_number = db.Column(db.String())
    province = db.Column(db.String())
    publisher_name = db.Column(db.String())
    bank_acc = db.Column(db.String())

    def __init__(self, id, email, street_num, postalcode, country, province, phone_number,publisher_name, bank_acc):
        self.p_id = p_id
        self.email = email
        self.street_num = street_num
        self.postalcode = postalcode
        self.country = country
        self.province = province
        self.phone_number = phone_number
        self.publisher_name = publisher_name
        self.bank_acc = bank_acc

    def __repr__(self):
        return self.id



class Wrote(db.Model):

    __tablename__ = "wrote"
    a_id = db.Column(db.Integer(), primary_key=True)
    book_id = db.Column(db.String(), primary_key=True)
    isbn = db.Column(db.String(), primary_key=True)



class Author(db.Model):

    __tablename__ = "author"
    a_id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())

class Views(db.Model):

    __tablename__ = "views"
    id = db.Column(db.Integer(), primary_key=True)
    c_out_id= db.Column(db.String(), primary_key=True)

    def __init__(self, id, c_out_id):
        self.id = id
        self.c_out_id = c_out_id
       
class Checkout(db.Model):

    __tablename__ = "checkout"
    c_out_id = db.Column(db.Integer(), primary_key=True)
    creditcard= db.Column(db.String())
    date = db.Column(db.String())
    shipping_price = db.Column(db.String())
    total = db.Column(db.String())

    def __init__(self, c_out_id, creditcard, date, shipping_price, total):
        self.c_out_id = c_out_id
        self.date = date
        self.shipping_price = shipping_price
        self.total = total


class Confirm_purchase(db.Model):

    __tablename__ = "complete_purchase"
    c_out_id = db.Column(db.Integer(), primary_key=True)
    order_id= db.Column(db.Integer(), primary_key=True)
    total= db.Column(db.Integer())

    def __init__(self, c_out_id, order_id, total):
        self.c_out_id = c_out_id
        self.order_id = order_id
        self.total = total

class Order_track(db.Model):

    __tablename__ = "order_track"
    order_id= db.Column(db.Integer(), primary_key=True)
    orderdate = db.Column(db.String())
    depart_date = db.Column(db.String())
    est_arrival = db.Column(db.String())
    current_location = db.Column(db.String())

    def __init__(self, order_id, orderdate, depart_date, est_arrival, current_location):
        self.order_id = order_id
        self.orderdate = orderdate
        self.depart_date = depart_date
        self.est_arrival = est_arrival
        self.current_location = current_location





