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
        chatbadwords = checkbadword(chatfield) # get bad word info from our message
        with open("data/messages.json") as fr:# open messages.json
            discussiondata = json.load(fr)# and load the json from it
            temp = discussiondata["discussion"]# take just the list
            entry = {"date/time" : str(posttime), "message" : chatfield}# create an entry
            entry["bad_word_info"] = chatbadwords # add the bad word info to the entry we're going to add
            temp.append(entry)# append the entry to the list
            
        with open("data/messages.json", "w") as fw:
            json.dump(discussiondata, fw, indent=4)# now write the file with the newly appended json
        
        with open("data/messages.json") as fr:
            chatdata = json.load(fr)# assign the newly appended json to something we can return
            chat = chatdata["discussion"]
            replacer(chat)
        return render_template("index.html", chat=chat) # return index.html along with the json file info
    
    with open("data/messages.json") as fr:
            chatdata = json.load(fr)# load up json messages for the chat
            chat = chatdata["discussion"]# take only the chat discussion
            replaced_chat = replacer(chat)#replacer
    return render_template("index.html", chat=replaced_chat) # otherwise just GET request for index.html and show chat

def checkbadword(message):
    """checks the message for bad words and returns replacement, index in the message for the bad word and the severity of it"""
    messagelist = message.split() # put the message into a list of words
    finalresult = [] # create a list to put all our bad word info
    with open("data/bad_words.json") as fr: # open badwords json file
        badworddict = json.load(fr) # open and get a dict of all bad words
    with open("data/good_words.json") as fr:
        goodwordlist = json.load(fr) # open and get a list of good words
    for x,y in badworddict.items(): # go through both keys and values to get bad word and severity
        for index, z in enumerate(messagelist): # loop through our messagelist and get the index
            if z == x: # if our message in messagelist is a badword
                simdict = dict() # make an empty dict to use  
                for a in goodwordlist: # loop through good words and get the index
                    simnumber = normalized_levenshtein.similarity(z, a) # compare the similarity of our bad word and good word
                    simdict.update({a : simnumber}) # append the good words index and the similarity number 
                sorteddict = (sorted(simdict.items(), key=lambda v: v[1], reverse=True)) # sort the dict by the similarity number
                finalsort = sorteddict[0] # get the most similar good word so we can replace it
                result = {"replacement": str(finalsort[0]), "original_index": index, "severity": y}
                finalresult.append(result) # append our result to finalresult
    return finalresult # return all the bad word info

def replacer(chat):
    """goes through all the messages and replaces bad words"""
    for discussion in chat: # loop through discussion
        for badwordinfo in discussion["bad_word_info"]: # loop through the bad word info in each message
            index = badwordinfo["original_index"] # take the bad word index for the message
            replacement = badwordinfo["replacement"] # take the bad word replacement for the message
            severity = badwordinfo["severity"] # take the bad word severity for the message
            if severity > 0: # if the severity of the message is greater than 0 (1 or 2)
                messagecopy = discussion["message"].split() # copy the message and turn it into a list
                messagecopy[index] = replacement # use the bad word index we got to access the bad word and replace it
                newmessage = " ".join(messagecopy) # turn the list back into a string
                discussion["message"] = newmessage # turn the actual message into our copy with the replaced words
    return chat

if __name__ == "__main__":
    app.run()