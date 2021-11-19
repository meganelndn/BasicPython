# Small Python examples

import math 

print("Hello World!")
print()

print("Hello")
print("World!")
print()

print("I say 'hello world'")
print()

print("A lucky number:", 3 + 4, "; an unlucky number:", int("13"))
print()

BOTTLEVOLUME = 0.7  # a constant (a convention that capital letters should be treated as a constant by other programmers)
# BOTTLEVOLUME = "abc"  # --> i can change the value if i want, and data type too.
bottles = 5
totalvolume = bottles * BOTTLEVOLUME
print("Bottle volume = " + str(BOTTLEVOLUME))
print("Total volume =", totalvolume)
print()

FIRSTNAME = "Hugo"
LASTNAME = "Smith"
name = FIRSTNAME + " " + LASTNAME 
print("Name: ", name, "\nIt starts with ", name[0])
print("Length of name = ", len(name))
print()

print("7/4 = ", 7 / 4)
print("7 // 4 = ", 7 // 4)
print("7 % 4 = ", 7 % 4)
print("sqrt(4) = ", math.sqrt(4))
print("sqrt(2) = ", math.sqrt(2))
print("sqrt(2) = %4.2f" % math.sqrt(2)) # %... is a parameter with a format, so that we can format it the way we like
print()

yourname = input("What is your name?") # input {name}
print("Hello " + yourname) # output Hello {name}
print()

userinput = input("Enter first number: ")
firstnumber = int(userinput)
userinput = input("Enter second number: ")
secondnumber = int(userinput)
sum = firstnumber + secondnumber
print()
print("%-15s %5d" % ("First number", firstnumber)) # s = string, d = decimal number, - = left-adjust text
print("%-15s %5d" % ("Second number", secondnumber))
print("%-15s %5d" % ("Sum", sum))
print()

print("-" * 25)
print()