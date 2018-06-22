__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
This problem is the reverse of problem3. Given the jumbled text created 
according to the rules given in problem 3 and number of steps, create the original text.

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Do not search for mathematical patterns, solve this programatically
'''


def unjumble(jumbled_text, n):
    if(type(jumbled_text)!=str):
        raise TypeError
    elif(n<=0):
        raise ValueError
    else:
        list1=[0]*n
        j=0
        flag=0
        while(True):
            for i in range(n,0,-1):
                if(j+i)<=len(jumbled_text):
                    list1[i-1]=list1[i-1]+i
                else:
                    flag=1
                    list1[i-1]=list1[i-1]+len(jumbled_text)-j
                    break
                j=j+i
            if(flag==1):
                break
            for i in range(1,n+1):
                if(j+i)<=len(jumbled_text):
                    list1[i-1]=list1[i-1]+i
                else:
                    flag=1
                    list1[i-1]=list1[i-1]+len(jumbled_text)-j
                    break
                j=j+i
            if(flag==1):
                break
        list2=[0]*n
        p=len(jumbled_text)

        for i in range(n,0,-1):
            list2[i-1]=p-list1[i-1]
            p=list2[i-1]
        ans=""
        flag=0
        while(True):
            for i in range(n,0,-1):
                if(list1[i-1]>=i):
                    ans=ans+jumbled_text[list2[i-1]:list2[i-1]+i]
                    list2[i-1]=list2[i-1]+i
                    list1[i-1]=list1[i-1]-i
                else:
                    ans = ans + jumbled_text[list2[i - 1]: list2[i - 1] + list1[i-1]]
                    flag=1
                    break
            if(flag==1):
                break
            for i in range(1,n+1):
                if(list1[i-1]>=i):
                    ans=ans+jumbled_text[list2[i-1]:list2[i-1]+i]
                    list2[i - 1] = list2[i - 1] + i
                    list1[i-1]=list1[i-1]-i
                else:
                    ans = ans + jumbled_text[list2[i - 1]: list2[i - 1] + list1[i-1]]
                    flag=1
                    break
            if(flag==1):
                break
        return ans



def test_unjumble():
    assert "ramdeepak" == unjumble("epdeakram", 3)
    assert "ajaykumarisagoodboy" == unjumble("odgoboisayumarajayk", 5)
