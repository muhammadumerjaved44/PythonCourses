# -*- coding: utf-8 -*-
# Create and print a dictionary:
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict)
# Duplicate values will overwrite existing values:
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"year": 2020
}
print(thisdict)
# String, int, boolean, and list data types:
thisdict = {
"brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]
}
# Nested way
child1 = {
"name" : "Emil",
"year" : 2004
}
child2 = {
"name" : "Tobias",
"year" : 2007
}
child3 = {
"name" : "Linus",
"year" : 2011
}
myfamily = {
"child1" : child1,
"child2" : child2,
"child3" : child3
}
print(myfamily)
