import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)



"""This creates a link to MongoDB"""

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://recipe8:Hellothere@myfirstcluster-ji6z9.mongodb.net/recipes?retryWrites=true&w=majority'

mongo = PyMongo(app)

""" This is for the index page """
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/task', methods=['POST'])
def task():
    recipes = mongo.db.recipes
    recipes.insert_one(request.gform.to_dict())
    return redirect(url_for('recipes'))
    return render_template("task.html", page_name="Task")

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    recipes = mongo.db.recipes.find()
    return render_template('recipes.html', recipes=the_recipes,)

@app.route('/update_task/<task_id>', methods=['POST'])
def update_task(task_id):
    recipes = mongo.db.recipes
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_description':request.form.get('recipe_description'),
        'nutrition': request.form.get('nutrition'),
        'ingredients': request.form.get('ingredients'),
        'recipe_preparation': request.form.get('recipe_preparation'),
        'recipe_cook': request.form.get('recipe_cook'),
        'recipe_method': request.form.get('recipe_method') 
    }
    return redirect(url_for('recipes_tasks'))

@app.route('/delete_recipe/<recipe_id>')
def recipe_task(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipes_task'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)