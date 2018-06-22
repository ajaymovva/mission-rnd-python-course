__author__ = 'Kalyan'

max_marks = 35 # 15 marks for encode and 20 for decode

problem_notes ='''
 This problem deals with number conversion into a custom base 5 notation and back.
 In this notation, the vowels a e i o u are used for digits 0 to 4.

 E.g. decimal 10 in this custom base 5 notation is "ia", decimal 5 is "ea" etc.

 Your job is to write encoding and decoding (both) routines to deal with this notation.
'''

# Notes:
# - If number is not a valid int raise TypeError
# - Negative numbers should result in a - prefix to the result similar to how bin works
#  use lower case letters in your result [aeiou].
def to_custom_base5(number):
    dict1={0:'a',1:'e',2:'i',3:'o',4:'u'}
    if type(number)!=int or number==None:
        raise TypeError
    elif number==0:
        return "a"
    else:
        list1=[]
        sign=0
        base=5
        if(number<0):
            sign=1
            number=-number
        temp=number
        while True:
            if(temp==0):
                break
            else:
                rem=temp%base
                list1.append(rem)
                temp=temp//base

        list1.reverse()
        str1=""
        if sign==1:
            str1=str1+'-'
        for i in list1:
            str1=str1+dict1[i]
        return str1

# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int that corresponds to the number.
def from_custom_base5(s):
    if type(s)!=str:
        raise TypeError
    elif len(s)==0:
        raise ValueError
    else:
        dict1={'a':0,'e':1,'i':2,'o':3,'u':4,'A':0,'E':1,'I':2,'O':3,'U':4}
        list1=[]
        k=0
        sign=0
        for i in range(len(s)):
            if(s[i]==" "):
                i+=1
            elif s[i]=='-' or s[i]=='+':
                if s[i]=='-':
                    sign=1
                k=i+1
                break
            else:
                k=i
                break
        for i in range(k,len(s)):
            if s[i]!=' ':
                try:
                    list1.append(dict1[s[i]])
                except KeyError:
                    raise ValueError
                k=i
            else:
                break
        k+=1
        for i in range(k,len(s)):
            if(s[i]!=' '):
                raise ValueError
        i=len(list1)-1
        if len(list1)==0:
            raise ValueError
        ans=0
        pow=1
        while i>=0:
            ans=ans+(pow*list1[i])
            pow=pow*5
            i-=1
        if sign==1:
            ans=-ans
        return ans

# a basic test is given, write your own tests based on constraints.
def test_to_custom_base5():
    assert "ia" == to_custom_base5(10)
    assert "ea" == to_custom_base5(5)
    assert "-ea" == to_custom_base5(-5)
    assert "uaa" == to_custom_base5(100)
    assert "a" == to_custom_base5(0)

# a basic test is given, write your own tests based on constraints.
def test_from_custom_base5():
    assert 10 == from_custom_base5("ia")
    assert 5 == from_custom_base5("    +ea     ")
    assert -100 == from_custom_base5("-uaa")