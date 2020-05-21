import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def tasks():
    return render_template("tasks.html")

@app.route('/contact')
def contact():
    return render_template("contact-us.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)