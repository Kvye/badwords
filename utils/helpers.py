import re
def alphaBet(word):
    """Reformats word passed through to cut out everything non-lowercase alphabetical"""
    return re.sub(r'[^a-z]', '', word)