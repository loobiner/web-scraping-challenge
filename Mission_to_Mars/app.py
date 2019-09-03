from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap   
import scrape_mars
    
app = Flask(__name__)

#I found out about a library that installs the Bootstrap js directly into html
Bootstrap(app)
mongo = PyMongo(app, url="mongodb://localhost:27017/mars_app")

@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)
 
@app.route('/scrape')
def scrape():
    surfing = mongo.db.mars
    data = scrape_mars.scrape()
    surfing.update(
        {},
        data,
        upsert=True
    )
    return redirect("/", code=302)