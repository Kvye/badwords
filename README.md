# badwords

A simple web application that displays chat messages and filters out words considered to be "bad" and replaces them with the best alternative using Levenshtein distance.

Prequisites
-----------
* Python
* Packages from [requirements.txt](requirements.txt)
* Flask

Installing
----------
Clone the repository just about anywhere.

Setup
-----
Make sure you have the prerequisites installed and have the repository on your machine.

With flask installed you will first want to set a variable for flask to know which file to look for when it wants to run, this can be done by changing your terminal's current directory to the root of the repository and then typing
```
set FLASK_APP=app.py
```
With that done you can then run flask to locally host the web app using app.py
```
flask run
```
With flask running you can now access it from a web browser by entering the following in the URL bar:
```
localhost:5000
```

Example Usage
-------------
Here you will have a screen that should look something like this:
![defaultimage](https://github.com/kvye/badwords/blob/master/static/img/Default.png)

At the bottom here is a text field where you can enter your message and submit the message:
![textfield](https://github.com/kvye/badwords/blob/master/static/img/textfield.png)
Here is a basic example:
![firstpost](https://github.com/kvye/badwords/blob/master/static/img/firstpost.png)

An example of what happens when you enter a bad word:
![bwtextfield](https://github.com/kvye/badwords/blob/master/static/img/badwordtextfield.png)
![bwpost](https://github.com/kvye/badwords/blob/master/static/img/badwordpost.png)

An example of the way the message will be displayed based on each type of severity:
![finalpost](https://github.com/kvye/badwords/blob/master/static/img/finalpost.png)

When you are done using the web app you can then close the connection to the app by returning back to your terminal and pressing ctrl+C

Built with
----------
* [Flask](https://github.com/pallets/flask)

Testing
-------
```
#repository root
pytest
```
