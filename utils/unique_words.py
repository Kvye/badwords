import re
import json

with open("../data/childrensstory1.txt") as fr: # open childrens story txt file
    story = fr.read() # take everything from it
    wordlist = re.sub("[^\w]", " ", story).split() # replace non alpha numericals with space and split
    wordset = set(wordlist) # put it into a set to get rid of duplicates
    uniquegoodwords = list(wordset) # turn it back into a list

with open("../data/good_words.json", "w") as fw:
    json.dump(uniquegoodwords, fw) # dump the list into a good_words.json
    
