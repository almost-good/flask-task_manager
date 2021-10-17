import os
    # step 2 imports
from flask_pymongo import PyMongo
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from bson.objectid import ObjectId
    # /step 2
if os.path.exists("env.py"): # once its deployed on heroku then it wont be able to find the file, thats why if
    import env


app = Flask(__name__) # instance of Flask

    # step 2 config
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
    # /step 2


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = mongo.db.tasks.find() 
    return render_template("tasks.html", tasks=tasks)



if __name__ == "__main__":  
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)