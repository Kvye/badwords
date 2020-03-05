import re
def alphaBet(word):
    return re.sub(r'[^a-z]', '', word)