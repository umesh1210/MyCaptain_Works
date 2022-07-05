
# Project 3
# Task 1
# Decreasing order of frequency

Input=input("Enter the string:")
from collections import Counter
req_str = Input

res = {}
def most_frequent(User_string):
    g = dict()
    for x in User_string:
        if x not in g:
            g[x] = 1
        else:
            g[x] += 1
    return g


for i in req_str:
    res[i] = res.get(i, 0) + 1
res = Counter(req_str)

print("Decreasing order of frequency  : \n"
      + str(res))