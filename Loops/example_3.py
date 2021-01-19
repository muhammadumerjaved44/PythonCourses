# -*- coding: utf-8 -*-
raining = False
while not raining:
    print("It's not raining.")
if input("Is it raining? (y/n) ") == 'y':
    raining = True
    print("It's raining!")
