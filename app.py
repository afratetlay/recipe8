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


""" This allows me to add new recipes to my website"""


@app.route('/task', methods=['GET'])
def task():
    recipes = mongo.db.recipes
    """recipes.insert_one(request.form.to_dict())"""
    """return redirect(url_for('recipes'))"""
    return render_template("task.html")


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    """recipes.insert_one(request.form.to_dict())"""
    recipes.insert({ 'image_source': request.form.get('image_source'),
        'recipe_name': request.form.get('recipe_name'),
        'serves': request.form.get('serves'),
        'due_time': request.form.get('due_time'),
        'calories': request.form.get('calories'),
        'fat': request.form.get('fat'),
        'saturates': request.form.get('saturates'),
        'sugars': request.form.get('sugars'),
        'salt': request.form.get('salt'),
        'recipe_description': request.form.get('recipe_description'),


        # Get List as my Ingredients and Methods are in an array in MongoDB 


        'ingredients': request.form.getlist('ingredients'),
        'recipe_method': request.form.getlist('recipe_method')})
    print('hello',  request.form.getlist('ingredients'))
    return redirect(url_for('recipes'))

@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/edittask/<recipes_id>')
def edittask(recipes_id):
    the_recipes = mongo.db.recipes.find_one({"_id":ObjectId(recipes_id)})
    return render_template('edittask.html', recipes=the_recipes)

@app.route('/update_recipe/<recipes_id>', methods=['POST'])
def update_recipe(recipes_id):
    recipes = mongo.db.recipes
    print (request.form)
    print(request.form.get('recipe_name'))
    recipes.update( {'_id': ObjectId(recipes_id)},
    {
        'image_source': request.form.get('image_source'),
        'recipe_name': request.form.get('recipe_name'),
        'serves': request.form.get('serves'),
        'time': request.form.get('due_time'),
        'calories': request.form.get('calories'),
        'fat': request.form.get('fat'),
        'saturates': request.form.get('saturates'),
        'sugars': request.form.get('sugars'),
        'salt': request.form.get('salt'),
        'recipe_description': request.form.get('recipe_description'),
        'ingredients': request.form.getlist('ingredients'),
        'recipe_method': request.form.getlist('recipe_method')
    })
    return redirect(url_for('recipes'))

@app.route('/delete_recipe/<recipes_id>')
def delete_recipe(recipes_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipes_id)})
    return redirect(url_for('recipes'))

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'views': 1}}
    )
    recipe_db = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("viewrecipe.html", recipe=recipe_db)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)