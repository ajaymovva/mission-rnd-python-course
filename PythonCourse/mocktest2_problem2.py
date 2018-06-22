__author__ = 'Kalyan'

max_marks = 25  # encrypt -> 13, decrypt 12

problem_notes = '''
Write encryption and decryption routines according to the given scheme. 

A secret key is used to encrypt a text message in the following manner: 
- key is a string of letters in which each letter represents the right displacement of the source character (a -> 0, z-> 25)
- text -> input text to be sent 

Letters of the input text are mapped to the letters in the key in a round robin manner. For e.g:

For: key = "abcde", text="hi there", the mapping is 
h->a, i -> b, (space is ignored) t ->c, h -> d, e-> e, (go back to starting a here) r -> a, e->b 

now to get the encrypted text, you move h by 0, i by 1, t by 2, h by 3 etc. So you finally get the text "hj vkirf"

The decryption works in the reverse way and returns the original text.

Notes:
- Preserve the casing(lower case remains lower case, Upper case remains Upper case).
- Ignore non-letters and punctuations, i.e., leave them as is in the final result
- For displacement, both small and large letters represent the same displacement. For e.g. b and B both represent 1
- raise TypeError if text and key are not strings.
- raise ValueError if key is empty or has non alphabet characters

Write helper sub routines as required. Make good use of the available datatypes!
'''

# do type checking, non-str should raise TypeException
def encrypt(text, key):
    if type(text)!=str or type(key)!=str:
        raise TypeError
    import string
    dict1=dict(zip(list(string.ascii_uppercase),list(range(26))))
    dict2=dict(zip(list(string.ascii_lowercase),list(range(26))))
    set2=set(list(string.ascii_lowercase))
    set2=set2|set(list(string.ascii_uppercase))
    for i in key:
        if i not in set2:
            raise ValueError
    dict1.update(dict2)
    length=len(key)
    k=0
    list1=[]
    for i in range(len(text)):
        if text[i] in set2:
            x=chr(ord(text[i])+dict1[key[k]])
            if(ord(x)>122):
                p=ord(x)-122
                p=96+p
                x=chr(p)
            elif(ord(x)<97 and ord(x)>90):
                p = ord(x) - 90
                p = 64+ p
                x = chr(p)
            list1.append(x)
            k=k+1
            k=k%length
        else:
            list1.append(text[i])
    return "".join(list1)

def decrypt(text, key):
    if type(text)!=str or type(key)!=str:
        raise TypeError
    import string
    dict1 = dict(zip(list(string.ascii_uppercase), list(range(26))))
    dict2 = dict(zip(list(string.ascii_lowercase), list(range(26))))
    set2 = set(list(string.ascii_lowercase))
    set2 = set2 | set(list(string.ascii_uppercase))
    for i in key:
        if i not in set2:
            raise ValueError
    dict1.update(dict2)
    length = len(key)
    k = 0
    list1 = []
    for i in range(len(text)):
        if text[i] in set2:
            x=(ord(text[i])-dict1[key[k]])
            if(ord(text[i])>96 and x<96):
                x=122-(96-x)
            elif(ord(text[i])>64 and x<64):
                x=90-(64-x)
            x=chr(x)
            list1.append(x)
            k=k+1
            k=k%length
        else:
            list1.append(text[i])
    return "".join(list1)


def test_encrypt():
    x1=encrypt("My Secret 10:20 Message", 'Secret')
    assert "hj vkirf" == encrypt("hi therb", "abcdz")

def test_decrypt():
    x=decrypt('EcUvgkwxOvwlskg', 'SEcret')
    assert "abc de" == decrypt("ace gi", "abcde")

