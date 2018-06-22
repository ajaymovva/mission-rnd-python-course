__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    if sentence==None:
        return None
    else:
        x=sentence.find(" either ")
        y=sentence.find(" or ")
        if(x!=-1 and y!=-1 and x+7!=y):
            y=sentence[:x]+sentence[x+7:y]
            return y
        else:
            return  sentence


def test_prune_either_or_student():
    assert "we could go to a movie"==prune_either_or("we could either go to a movie or a hotel")
    assert "we could go to a" == prune_either_or("we could either go to a or a hotel")
    assert "we could go to a movie or a hotel" == prune_either_or("we could go to a movie or a hotel")
    assert "we couldeither go to a movieor a hotel"==prune_either_or("we couldeither go to a movieor a hotel")
    assert "we could" == prune_either_or("we could")
    assert "we can go either a way" == prune_either_or("we can go either a way")
    assert "either this or that" == prune_either_or("either this or that")
    assert "Two mythical cities eitheron and oregon" == prune_either_or("Two mythical cities eitheron and oregon")
    assert "you can visit eitheron in summer or winter"==prune_either_or("you can visit eitheron in summer or winter")
    assert None == prune_either_or(None)



# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
