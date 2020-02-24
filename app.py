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
        
        with open("data/messages.json") as fr:# open messages.json
            discussiondata = json.load(fr)# and load the json from it
            temp = discussiondata["discussion"]# take just the list
            entry = {"date/time" : str(posttime), "message" : chatfield}# create an entry
            temp.append(entry)# append the entry to the list
        
        with open("data/messages.json", "w") as fw:
            json.dump(discussiondata, fw, indent=4)# now write the file with the newly appended json
        
        with open("data/messages.json") as fr:
            chatdata = json.load(fr)# assign the newly appended json to something we can return
            chat = chatdata["discussion"]
        
        return render_template("index.html", chat=chat) # return index.html along with the json file info
    
    return render_template("index.html") # otherwise just GET request for index.html


if __name__ == "__main__":
    app.run()