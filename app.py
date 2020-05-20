import os
from flask import Flask 
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://afra:Hellothere8@myfirstcluster-ji6z9.mongodb.net/recipes?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

    