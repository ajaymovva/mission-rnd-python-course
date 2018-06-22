__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Palindrome is a word which spells the same from both ends.

Create the smallest palindrome from a given word by appending characters to its end.

Examples:
- Malayalam -> Malayalam
- Malayal -> Malayalam (we want smallest palindrome)


Notes:
1. Don't change the letters of the initial word, only add new small letters
2. The palindrome is case-insensitive (ie) Tat is a valid palindrome
3. Only letters are allowed, any other characters should raise a ValueError
4. Non strings should raise a TypeError
5. Empty string is considered as a palindrome.
'''

def smallest_palindrome(word):
    import string
    if type(word)!=str:
        raise TypeError
    elif len(word)==0:
        return word
    else:
        word1=word
        word2=word
        cap=list(string.ascii_uppercase)
        small=list(string.ascii_lowercase)
        for i in word:
            if i not in cap:
                if i not in small:
                    raise ValueError
        a=0
        word=word2.lower()
        while True:
            word1=word[a:]
            i=0;j=len(word1)-1
            k=0
            while i<j:
                if(word1[i]!=word1[j]):
                    k=1
                    break
                i+=1;j-=1
            if(k==0):break
            a+=1
        s=word[:a]
        s=s[::-1]
        word2=word2+s
        return word2



# write your own tests
def test_smallest_palindrome():
    assert "dudedud" == smallest_palindrome("duded")
    assert "RoTator" == smallest_palindrome("RoTator")
    assert "dudedud" == smallest_palindrome("duded")
    assert "RORaror" == smallest_palindrome("RORar")
    assert "" == smallest_palindrome("")
    # pass
