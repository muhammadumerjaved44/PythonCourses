# -*- coding: utf-8 -*-
weight = 0.2
animal = "newt"
# Concatenate a number and a string in one print statement
print(str(weight) + " kg is the weight of the " + animal + ".")
# Use format() to print a number and a string inside of another string
print("{} kg is the weight of the {}.".format(weight, animal))
# Use formatted string literal (f-string) to reference objects inside a string
print(f"{weight} kg is the weight of the {animal}.")
