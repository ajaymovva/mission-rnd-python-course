__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given a string of digits, you must return a list of all (substring, count) in the input string such that count >=2 and 
len(substring) >= 2. count represents the number of times the substring repeats in the input string (non-overlapping 
occurances).

The result must be sorted by count first (descending) and then in case of a tie the numerical value of 
substring (descending)

For e.g. if input is "123451236786712" you must return [("12", 3), ("123", 2), ("67", 2), ("23", 2)]

Notes:
1. if input is not a str, raise TypeError
2. Write clean bruteforce code to do this using python features. Do not devise new algorithms in the exam!
3. Write your own test cases 
'''

def repeats(digits):
    if(type(digits)!=str):
        raise TypeError
    else:
        ans=[]
        k=2
        while(k<len(digits)):
            i=0;j=k
            while(j<=len(digits)):
                str1=digits[i:j]
                count1=digits.count(str1)
                if(count1>=2):
                    ans.append((str1,count1))
                j+=1
                i+=1
            k+=1
        ans=list(set(ans))
        ans.sort(key=lambda x:(x[1],int(x[0])),reverse=True)
        return ans


def test_repeats():
    assert [("12", 3), ("123", 2), ("67", 2), ("23",2)] == repeats("123451236786712")
    x=repeats("123451234534512")
    print(x)