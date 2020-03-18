from flask import Flask, render_template, url_for 
import os

bookstore = Flask(__name__, template_folder='templates')           

#render home page
@bookstore.route("/")                  
def index(): 
    #main directory of folder
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    main_dir = os.path.dirname(working_dir) 
    return render_template('index.html')

#render store page
@bookstore.route("/store")                  
def index(): 
    #store directory of folder
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    main_dir = os.path.dirname(working_dir) 
    return render_template('store.html')            

if __name__ == "__main__":  
    bookstore.run()   