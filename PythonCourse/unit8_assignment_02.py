__author__ = 'Kalyan'

from placeholders import *


profiling_timeit = '''
Python also gives a helpful timeit module that can be used for benchmarking a given piece of code

Reading material:
 http://docs.python.org/3/library/timeit.html
 http://stackoverflow.com/questions/8220801/how-to-use-timeit-correctly
 http://www.dreamincode.net/forums/topic/288071-timeit-module/

Try out on sample code snippets from above links on your own before you get to the assignment.

Generally you will study performance as you vary the input across a range e.g. count = 10, 100, 1000, 10000

profile the 4 methods in unit7_conversion_methods.py using timeit in this assignment.

for each value of count, execute the method 5 times using timeit and print out the min value and the actual 5 values.
output should look like (a total of 16 lines):
numbers_string1, count = 10, min = 0.0001, actuals = [0.0001, 0.0002, 0.0001, ...]
numbers_string1, count = 100, min = 0.002, actuals = [0.002, 0.002, 0.003, ...]
....
numbers_string4, count = 10000, min = 0.1 actuals = [....]

'''

from unit8_conversion_methods import *
import timeit

def profile_timeit():
    funclist = [numbers_string1,numbers_string2,numbers_string3,num_strings4]
    for func in funclist:
        count = 10
        while count <= 10000:
            actuals = []
            i = 0
            while i < 5:
                x=timeit.timeit(stmt=func(count),number=1)
                actuals.append(x)
                i += 1
            #actuals=timeit.repeat(stmt=func(count),repeat=5,number=1)
            actuals = ["%.6f" % k for k in actuals]
            print(func.__name__, count, min(actuals), actuals)
            count = count * 10

# write your findings on what you learnt about timeit, measuring perf and how the results here compare to
# values in assignment1
summary = '''


'''

if __name__ == "__main__":
    profile_timeit()
