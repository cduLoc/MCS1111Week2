#"I have neither given nor received unauthorized aid in completing this work, nor have I presented someone else's work as my own."
#Carl Wilburn
#30 Jan 21
#Assignment 1

#takes user input and stores it as variable "name"
name = input("Hello User! Would you be so kind as to tell me your name? Please type it surrounded by double quotes(e.g.-''John Doe''): ")
print("Welcome, " + name + ", how many centimeters would you like to be converted to inches? ") #uses the "name" variable acquired from previous line and asks for a user input as a number
numIn=float(input("Please input desired amount of converted centimeters without any quotation (e.g.- 90): "))#stores user input to numIn and is ensured the data type is correct
convertNum= numIn * 0.393701 #conversion of centimeters to inches
print("The amount of inches converted from the centimeters that you entered is equal to: " + str(convertNum) + " inches")#prints converted number from previous line
r = 6 #r = radius
print("The area of a circle of radius 6 is equal to: " + str(3.14*r*r)) #calculates area of circle using radius 6 and is converted to string so that it can be concatenated
print("For my final trick, we will be completing the exciting act of addition!")#small bit of dramatic flare. as a treat
add1=eval(input("Please input the first number that you would like added without quotation marks: ")) 
add2=eval(input("Please input the second number that you would like added without quotation marks: "))
print("The sum of " + str(add1) + " and " + str(add2) + " is equal to " + str(add1 + add2))#calculates the sum of the above two user inputed numbers and converts the numbers to strings so that they can be concatenated