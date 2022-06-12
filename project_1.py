#Task 1
# Radius of a circle from the user and computer area;

radius=float(input("Enter the radius of the circle:"))
pi=3.14
print("Area of the circle with radius",radius,"is:",pi*radius**2)




# Task 2
file_name= input("Enter the Filename: ")

d= file_name.split(".")

print ("Extension of the file is : " + d[-1])
