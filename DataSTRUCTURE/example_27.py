# -*- coding: utf-8 -*-
# Get the value of the "model" key
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict["model"]
print(x)
y = thisdict.get("model")
print(y)
# Get a list of the keys:
x = thisdict.keys()
# Get a list of the values:
x = thisdict.values()
# Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the chang
