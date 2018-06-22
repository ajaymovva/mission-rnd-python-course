__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys

def writingtofile(ans,inputfile):
    outputfile=inputfile[:len(inputfile)-4]+"-results"+inputfile[len(inputfile)-4:]
    f=open(outputfile,"w")
    for i in ans:
        for j in i:
            f.write(j)
            f.write("\n")
    return

def sortinginlists(ans):
    for i in ans:
        i.sort(key=lambda x:x.lower())
    temp = []
    ans1 = []
    p = len(ans[0])
    for i in range(p, 0, -1):
        for j in ans:
            if (len(j) == i):
                temp.append(j)
        temp.sort(key=lambda x: x[0].lower())
        for p in temp:
            ans1.append(p)
        temp = []
    return ans1



def grouping(list1):
    ans=[]
    for i in list1:
        sign=0
        for j in ans:
            for k in j:
                list1=list(k.lower())
                list1.sort()
                list2=list(i.lower())
                list2.sort()
                if(list1==list2):
                    j.append(i)
                    sign=1
                    break
            if(sign==1):
                break
        if(sign==0):
            ans.append([i])
    ans.sort(key=len,reverse=True)
    return ans


def datatolist(inputfile):
    f=open(inputfile,'r')
    list1=[]
    lines=f.readlines()
    for i in lines:
        if(i[0]!='#' and i[0]!=' '):
            list1.extend(i.strip().split())
    return list1

if __name__ == "__main__":
    inputfile = sys.argv[1]
    list1 = datatolist(inputfile)
    ans = grouping(list1)
    ans1 = sortinginlists(ans)
    writingtofile(ans1, inputfile)