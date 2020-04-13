#import database connection
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager


db = SQLAlchemy()
login_manager = LoginManager()

class Books(db.Model):

    __tablename__ = "books"
    book_id = db.Column(db.Integer(), primary_key=True)
    publisher = db.Column(db.String())
    author = db.Column(db.String())
    title = db.Column(db.String())
    isbn = db.Column(db.String())
    publication_date = db.Column(db.String())
    price = db.Column(db.String())
    book_stock = db.Column(db.Integer())

    def __init__(self, book_id, author, publisher, title, isbn, genre, publication_date, price,book_stock):
        self.book_id = book_id
        self.author = author
        self.publisher = publisher
        self.title = title
        self.isbn = isbn
        self.publication_date = publication_date
        self.price = price
        self.book_stock = book_stock

    def __repr__(self):
        return '<title %r>' % (self.title, self.author, self.publisher, self.isbn, self.publication_date)
        

class Users(db.Model,UserMixin):

    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    street_num = db.Column(db.String())
    postalcode = db.Column(db.String())
    country = db.Column(db.String())
    province = db.Column(db.String())
    phone_number = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, id, firstname, lastname, street_num, postalcode, country, province, phone_number, email, username, password):
        self.id = cust_id
        self.firstname = firstname
        self.lastname = lastname
        self.street_num = street_num
        self.postalcode = postalcode
        self.country = country
        self.province = province
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return self.id




