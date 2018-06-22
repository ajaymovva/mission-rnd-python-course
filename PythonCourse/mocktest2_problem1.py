max_marks = 20

problem_notes = '''
Given a sentence in which words are separated by spaces.

Re-arrange it so that words are reordered according to the following criteria.
 - longer words come before shorter words
 - if two words have same length, the one with smaller vowel occurance count comes first (feeel counts as 3 vowel occurances)
 - if even that is same, then order them lexicographically (case insensitive). For e.g. a comes before b

Constraints:
- Only allowed characters are a-zA-Z in the words
- raise a ValueError if the sentence contains any characters beyond the above
- raise a TypeError if input is not a string
- The result should preserve the words as is without changing case etc. but the sentence should be sorted so that
longer words precede shorter words. In case of tie, the word with fewer vowels comes first, if there is a tie even there,
preserve the original order.
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.


Note: 
1. use the features of python to solve this problem, DON'T WRITE YOUR OWN SORT ROUTINE!
2. You can write additional routines as you see fit.
'''
def vowelcount(x):
    import string
    list1=['a','e','i','o','u','A','E','I','O','U']
    k=0
    for i in x:
        if(i in list1):
            k=k+1
    return k
def transform(sentence):
    import string
    if type(sentence)!=str:
        raise TypeError
    else:
        list2 = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        list2.append(" ")
        for i in sentence:
            if i not in list2:
                raise ValueError
    list1=sentence.strip().split(" ")
    list1=list(filter(lambda x:len(x)>0,list1))
    ans=sorted(sorted(sorted(list1,key=lambda x:x.lower()),key=vowelcount),key=len,reverse=True)
    return " ".join(ans)

def test_transform():
    assert "Elephants fast tour pat run" == transform("run tour pat fast Elephants")
    assert "Elephants fast tour got Pat Run" == transform("Run tour Pat fast got Elephants")
    assert "Elephant fast runs the" == transform(' fast   runs   the  Elephant ')