__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    if first!=None and second!=None:
        list1=list(first.lower())
        list2=list(second.lower())
        list1.sort()
        list2.sort()
        if list1==list2:
            return True
        else:
            return False
    elif first==None and second!=None:
        return False
    elif first!=None and second==None:
        return False
    else:
        return False


# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert True==are_anagrams("AJAY","yaja")
    assert False==are_anagrams(None,None)
    assert False==are_anagrams("AJAY",None)
    assert False==are_anagrams(None,"Ajay")
    assert False == are_anagrams("bigg", "biig")


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)
