from flask import Flask, render_template, request
import datetime
import json
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """returns the index html page"""
    if request.method == "POST": # if we get a POST request
        chatfield = request.form["chatfield"] # take what we got from the chatfield form's request
        posttime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") # get current datetime
        
        postdict = { # put the chatfield form info and posttime into a dict
            "date/time" : str(posttime),
            "message" : chatfield
        }
        postdata = json.dumps(postdict) # write it into a json file
        with open("data/messages.json", "w") as f:
            f.write(postdata)

        with open("data/messages.json", "r") as f: # read the json file
            chat = json.load(f)

        return render_template("index.html", chat=chat) # return index.html along with the json file info
    
    return render_template("index.html") # otherwise just GET request for index.html


if __name__ == "__main__":
    app.run()