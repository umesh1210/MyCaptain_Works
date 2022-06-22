

# Project 3
# Task 1

# Write python code to create a function called most_frequent...
# Give the input as "Mississippi"

Input=input("Please enter a string:")
def most_frequent(User_string):
    g = dict()
    for x in User_string:
        if x not in g:
            g[x] = 1
        else:
            g[x] += 1
    return g


print(most_frequent(Input))