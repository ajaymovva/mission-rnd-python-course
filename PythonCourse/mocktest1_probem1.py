__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given 2 strings str1 and str2, find out the minimum number of right rotations str1 needs to undergo
to create str2. If is not possible, return -1

Notes:
1. Assume inputs are either None or valid strings
2. Write plain brute force code.
3. result should be -1 if not possible
4. If it is possible then give the 'minimum rotations' required.
5. No need for type checking.
'''

def get_right_rotations(str1, str2):
    if str1==None or str2==None:
        return -1
    elif str1==str2:
        return 0
    else:
        count=0
        str3=str1
        list1=list(str1)
        list1.sort()
        list2=list(str2)
        list2.sort()
        if list1 ==list2:
            while True:
                if str3 == str2 or count==len(str1):
                    break
                else:
                    str3=str3[-1]+str3[:-1]
                    count+=1
            if count==len(str1):
                return -1
            else:
                return count
        else:
            return -1


# basic test given, write more tests to ensure correctness.
def test_get_right_rotations():
    assert 1 == get_right_rotations("abcd", "dabc")
    assert 2 == get_right_rotations("abcd", "cdab")
    assert 3 == get_right_rotations("abcd", "bcda")
    assert 0 == get_right_rotations("abcd", "abcd")
    assert -1 == get_right_rotations("abcd", "cadb")
    assert -1 == get_right_rotations("abcd", "")
    assert -1 == get_right_rotations("abcd", None)
    assert -1 == get_right_rotations(None, "abcd")
