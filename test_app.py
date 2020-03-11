import pytest
import app

def test_check_bad_word():
    """Test to check if checkbadword function works correctly"""
    examplemessage = "this is a shit example"

    # assert that example message will detect "shit" with "suit" as replacement, index being 3 and severity of 1
    assert app.checkbadword(examplemessage) == [{"replacement": "suit", "original_index": 3, "severity": 1}]

def test_find_severity():
    """Test to check if findseverity function works correctly"""
    examplemessage = "this is a shit example"

    # assert severity of "shit" in examplemessage is 1 
    assert app.findseverity(3, app.checkbadword(examplemessage)) == 1

def test_replacer():
    """Test to check if replacer function works correctly"""
    examplechat = [
        {
            "date/time": "03-03-2020 00:25:35",
            "message": "this is what i call a fucking australian bitch example",
            "bad_word_info": [
                {
                    "replacement": "Australia",
                    "original_index": 7,
                    "severity": 0
                },
                {
                    "replacement": "Fetch",
                    "original_index": 8,
                    "severity": 1
                },
                {
                    "replacement": "funding",
                    "original_index": 6,
                    "severity": 2
                }
            ]
        }
    ]
    replacedchat = app.replacer(examplechat)

    # assert that replacing the message in examplechat will replace "fucking" and "bitch" with "funding" and "Fetch"
    assert replacedchat[0]["words"] == ["this", "is", "what", "i", "call", "a", "funding", "australian", "Fetch", "example"]
