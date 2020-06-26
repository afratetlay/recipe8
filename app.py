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

@app.route('/task', methods=['GET'])
def task():
    """recipes = mongo.db.recipes"""
    """recipes.insert_one(request.form.to_dict())"""
    """return redirect(url_for('recipes'))"""
    return render_template("task.html", name=mongo.db.recipes.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('recipes.html'))


@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

"""@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = request.form.to_dict()
    # for loop with if statement prevents user from submitting a blank form with only space characters
    for field in recipes:
        if recipes[field].isspace() == True:
            return render_template('error_addrecipe.html', types=mongo.db.recipes.find())
    for recipe_by in recipes:
        if recipes[recipe_by].lower() == "admin":
            return render_template('error_adminaddrecipe.html', types=mongo.db.recipes.find())
    recipes = mongo.db.recipes.insert(recipes)
    #after adding the recipe to the database it redirects the user to the newly added recipe to view the full recipe
    return redirect(url_for('recipes', recipe_id=recipes))"""

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    return render_template('recipes.html', recipes=the_recipes,)

@app.route('/update_task/<task_id>', methods=['POST'])
def update_task(task_id):
    recipes = mongo.db.recipes
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_description': request.form.get('recipe_description'),
        'nutrition': request.form.get('nutrition'),
        'ingredients': request.form.get('ingredients'),
        'recipe_preparation': request.form.get('recipe_preparation'),
        'recipe_cook': request.form.get('recipe_cook'),
        'recipe_method': request.form.get('recipe_method')
    }
    return redirect(url_for('recipes'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
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