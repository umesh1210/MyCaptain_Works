# project 2


#Task 1:
# Fibonacci numbers

x=int(input("Enter the terms:"))
first=0                                    # directly taking the fist and second term as 0,1
second=1
if x<=0:
    print("Given input series is",first)
else:
    print(first,second,end=" ")
    for h in range(2,x):
        next=first+second
        print(next,end=" ")
        first=second
        second=next