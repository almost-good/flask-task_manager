# step 1
import os
from flask import Flask
if os.path.exists("env.py"): # once its deployed on heroku then it wont be able to find the file, thats why if
    import env


app = Flask(__name__) # instance of Flask

@app.route("/") #test function 
def hello():
    return "Hello World ... again!"


if __name__ == "__main__":  
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)