import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/task')
def task():
    return render_template("task.html")

@app.route('/recipes')
def recipes():
    return render_template("recipes.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/chickenkorma')
def chickenkorma():
    return render_template("chickenkorma.html")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)