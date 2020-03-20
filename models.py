#import database connection
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Books(db.Model):

    __tablename__ = "books"
    book_id = db.Column(db.Integer(), primary_key=True)
    publisher = db.Column(db.String())
    author = db.Column(db.String())
    title = db.Column(db.String())
    isbn = db.Column(db.String())
    genre = db.Column(db.String())
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
        

class Users(db.Model):

    __tablename__ = "users"
    cust_id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    street_num = db.Column(db.String())
    postalcode = db.Column(db.String())
    country = db.Column(db.String())
    province = db.Column(db.String())
    phonenum = db.Column(db.String())
    email = db.Column(db.String())
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, cust_id, firstname, lastname, street_num, postalcode, country, province, phonenum, email, username, password):
        self.cust_id = cust_id
        self.firstname = firstname
        self.lastname = lastname
        self.street_num = street_num
        self.postalcode = postalcode
        self.country = country
        self.province = province
        self.phonenum = phonenum
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<firstname %r>' % (self.firstname)
