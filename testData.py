import os
import sys
import logging
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# from PIL import Image
import uuid
from array import array
from pymongo import MongoClient
from statistics import mode
from env import MONGO_URI


app = Flask(__name__)

# app.config["MONGO_DBNAME"] = ""
app.config["MONGO_URI"] = MONGO_URI


mongo = PyMongo(app)

print("Sarting program")


def wipeDataBase():
    mongo.db.recipe_project.drop()
    mongo.db.fs.chunks.drop()
    mongo.db.fs.files.drop()


def insertRecipe(recipeName, ingredients, how_to, vegetarian, pathImage, author):
    try:
        extention = os.path.splitext(pathImage)
        if extention:
            randomFileName = str(uuid.uuid1()) + str(extention[1])
        else:
            randomFileName = str(uuid.uuid1()) + ".jpg"
        # recipeImage = open(pathImage,'rb')
        with open(pathImage, "rb") as recipeImage:
            imageId = mongo.save_file(randomFileName, recipeImage)

        # r = fs.get(recipeImage).read()
        print(imageId)
        mongo.db.recipe_project.insert_one(
            {"recipeName": recipeName,
             "ingredients": ingredients,
             "how_to": how_to,
             "vegetarian": vegetarian,
             "recipe_image_Id": randomFileName,
             "author": author.lower()})
    except Exception as exception:
        exception_message = str(exception)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        print(exception_message)


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
wipeDataBase()
insertRecipe("Apple Tart", ["4 apple's", "pastery"],
             ["Push them all togeather", "mash them up", "eat"],
             False, "./testData/apple.jpg", "billy joel")
insertRecipe("Pancake", ["100g plain flour", "Pinch of salt", "1 Bord Bia Quality Assured egg", "300 ml milk", "1 tablsp. melted butter or sunflower oil"],
             ["Sift the flour and salt into a mixing bowl and make a well in the centre.",
              "Crack the egg into the well; add the melted butter or oil and half the milk. Gradually draw the flour into the liquid by stirring all the time with a wooden spoon until all the flour has been incorporated and then beat well to make a smooth batter.",
              "Stir in the remaining milk. Alternatively, beat all the ingredients together for 1 minute in a blender or food processor.", "Leave to stand for about 30 minutes, then stir again before using.",
              "To make the pancakes, heat a small heavy-based frying until very hot and then turn the heat down to medium.",
              "Lightly grease with oil and then ladle in enough batter to coat the base of the pan thinly (about 2 tablsp.), tilting the pan so the mixture spreads evenly.",
              "Cook over a moderate heat for 1-2 minutes or until the batter looks dry on the top and begins to brown at the edges. Flip the pancake over with a palette knife or fish slice and cook the second side.",
              "Turn onto a plate, smear with a little butter, sprinkle of sugar and a squeeze of lemon juice and serve."],
             True,
             "./testData/pancake.jpg", "Sam Smith")

insertRecipe("Scones", ["350g self-raising flour, plus more for dusting", "¼ tsp salt", "1 tsp baking powder",
                        "85g butter and cut into cubes", "3 tbsp caster sugar", "175ml milk", "1 tsp vanilla extract", "squeeze lemon juice", "beaten egg to glaze",
                        "jam and clotted cream, to serve"],
             ["Heat oven to 220C/fan 200C/gas 7.",
              "Tip 350g self-raising flour into a large bowl with ¼ tsp salt and 1 tsp baking powder, then mix.",
              "Add 85g butter cubes, then rub in with your fingers until the mix looks like fine crumbs then stir in 3 tbsp caster sugar.",
              "Put 175ml milk into a jug and heat in the microwave for about 30 secs until warm, but not hot.",
              "Add 1 tsp vanilla extract and a squeeze of lemon juice, then set aside for a moment.",
              "Put a baking sheet in the oven.",
              "Make a well in the dry mix, then add the liquid and combine it quickly with a cutlery knife – it will seem pretty wet at first.",
              "Scatter some flour onto the work surface and tip the dough out. Dredge the dough and your hands with a little more flour, then fold the dough over 2-3 times until it’s a little smoother. Pat into a round about 4cm deep.",
              "Take a 5cm cutter (smooth-edged cutters tend to cut more cleanly, giving a better rise) and dip it into some flour. Plunge into the dough, then repeat until you have four scones. You may need to press what’s left of the dough back into a round to cut out another four.",
              "Brush the tops with a beaten egg, then carefully place onto the hot baking tray.",
              "Bake for 10 mins until risen and golden on the top. Eat just warm or cold on the day of baking, generously topped with jam and clotted cream. ",
              "If freezing, freeze once cool. Defrost, then put in a low oven (about 160C/fan140C/gas 3) for a few mins to refresh."],
             True,
             "./testData/scones.jpg", "billy joel")
insertRecipe("Chorizo & mozzarella gnocchi bake", ["1 tbsp olive oil", "1 onion finely, chopped", "2 garlic cloves, crushed",
                                                   "120g chorizo, diced", "2 x 400g cans chopped tomatoes",
                                                   "1 tsp caster sugar", "600g fresh gnocchi",
                                                   "125g mozzarella ball, cut into chunks",
                                                   "small bunch of basil, torn",
                                                   "green salad, to serve"],
             ["Heat the oil in a medium pan over a medium heat. Fry the onion and garlic for 8-10 mins until soft. Add the chorizo and fry for 5 mins more. Tip in the tomatoes and sugar, and season. Bring to a simmer, then add the gnocchi and cook for 8 mins, stirring often, until soft. Heat the grill to high.",
              "Stir ¾ of the mozzarella and most of the basil through the gnocchi. Divide the mixture between six ovenproof ramekins, or put in one baking dish. Top with the remaining mozzarella, then grill for 3 mins, or until the cheese is melted and golden. Season, scatter over the remaining basil and serve with green salad."],
             False,
             "./testData/chorizoPasta.jpg", "Sam Smith")

# wipeDataBase()
print(insertRecipe)
print("ending program")
# if __name__ == "__main__":
#     app.run(host=os.environ.get("IP"),
#             port=(os.environ.get("PORT")),
#             debug=True)
