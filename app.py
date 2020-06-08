import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://recipe8:Hellothere@myfirstcluster-ji6z9.mongodb.net/recipes?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/task')
def task():
    return render_template("task.html", page_name="Task")

@app.route('/recipes')
def recipes():
    return render_template("recipes.html", page_name="Recipes")

@app.route('/contact')
def contact():
    return render_template("contact.html", page_name="Contact")

@app.route('/chickenkorma')
def chickenkorma():
    return render_template("chickenkorma.html")

@app.route('/garlicchicken')
def garlicchicken():
    return render_template("garlicchicken.html")

@app.route('/creamychicken')
def creamychicken():
    return render_template("creamychicken.html")

@app.route('/pastachicken')
def pastachicken():
    return render_template("pastachicken.html")

@app.route('/chillichicken')
def chillichicken():
    return render_template("chillichicken.html")

@app.route('/thaichicken')
def thaichicken():
    return render_template("thaichicken.html")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)