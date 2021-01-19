# -*- coding: utf-8 -*-
# Nested If
# You can have if statements inside if statements, this is called nested if statements.
x = 41
if x > 10:
    print("Above ten,")
if x > 20:
    print("and also above 20!")
else:
    print("but not above 20.")
# if statements cannot be empty, but if you for some reason have an if statement
# with no content, put in the pass statement to avoid getting an error
a = 33
b = 200
if b > a:
    pass

