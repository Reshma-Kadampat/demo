# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 09:55:27 2024

@author: abrut
"""

def comp(p,r,t):
    amt=p*(pow((1+r/100),t))
    ci=amt*p
    print("compount interest is ",ci)
    
comp(1000,3,2)