# -*- coding: utf-8 -*-
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
for index, letterpair in enumerate(zip(uppercase, lowercase), start=1):
    upper, lower = letterpair
print(index, upper, lower)
