# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:32:42 2020

@author: NAIDU
"""

string = ')()()('
count=0
marks=0
lst=[]
for s in string:
    print(s)
    if s=='(':
        lst.append(s)
    elif s== ')':
        lst.pop()
print((len(string)-len(lst)) //2)