from flask import Flask, render_template, request
import datetime
import json
import re
from similarity.normalized_levenshtein import NormalizedLevenshtein
app = Flask(__name__)
normalized_levenshtein = NormalizedLevenshtein()

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
    
    with open("data/messages.json") as fr:
            chatdata = json.load(fr)# load up json messages for the chat
            chat = chatdata["discussion"]# take only the chat discussion

    return render_template("index.html", chat=chat) # otherwise just GET request for index.html and show chat

def checkandreplace(message):
    """checks the message for bad words and returns replacement, index in the message for the bad word and the severity of it"""
    messagelist = message.split() # put the message into a list of words
    with open("data/bad_words.json") as fr: # open badwords json file
        badworddict = json.load(fr) # get the data
    for x,y in badworddict.items(): # go through both keys and values to get bad word and severity
        for index, z in enumerate(messagelist): # loop through our messagelist and get the index
            if z == x: # if our message in messagelist is a badword
                with open("data/good_words.json") as fr:
                    goodwordlist = json.load(fr) # open and get a list of good words
                simdict = dict() # make an empty dict to use  
                for a in goodwordlist: # loop through good words and get the index
                    simnumber = normalized_levenshtein.similarity(z, a) # compare the similarity of our bad word and good word
                    simdict.update({a : simnumber}) # append the good words index and the similarity number 
                sorteddict = (sorted(simdict.items(), key=lambda v: v[1], reverse=True)) # sort the dict by the similarity number
                finalsort = sorteddict[0] # get the most similar good word so we can replace it
                result = {"replacement": str(finalsort[0]), "original index": index, "severity": y}
            
    return result

if __name__ == "__main__":
    #app.run()
    print(checkandreplace("hey fuck bitch")) # just testing if the function works