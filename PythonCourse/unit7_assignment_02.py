__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys

import string
def function():
    list1=sys.argv[1:]
    set3={',','.'}
    set2=set(string.ascii_lowercase)|set(string.ascii_uppercase)
    set1={'a','e','i','o','u','A','E','O','I','U'}
    set2=set2-set1
    for i in range(len(list1)):
        if list1[i][0] in set2:
            str=""
            k=0
            for j in range(len(list1[i])):
                if(list1[i][j] in set1):
                    break
                str=str+list1[i][j]
                k=j
            if (list1[i][len(list1[i]) - 1]) in set3:
                x = list1[i][len(list1[i]) - 1]
                list1[i] = list1[i][k+1:len(list1[i]) - 1] +str+ 'ay' + x
            else:
                list1[i] = list1[i][k+1:] +str+ 'ay'
        elif list1[i][0] in set1:
            if(list1[i][len(list1[i])-1]) in set3:
                x=list1[i][len(list1[i])-1]
                list1[i]=list1[i][:len(list1[i])-1]+'ay'+x
            else:
                list1[i]=list1[i]+'ay'
    list1[0]=list1[0].capitalize()
    str=" ".join(list1)
    return str

if __name__ == "__main__":
    str=function()
    try:
        while True:
            print(str)
    except KeyboardInterrupt:
        pass
