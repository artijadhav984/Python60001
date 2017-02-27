#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:13:07 2017

@author: Arti
"""
import numpy #math

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
z = x ** y
print("X ** y = {}".format(z))

lg= numpy.log2(x) #int(math.log(x, 2))
print("log(x) =  {}".format(lg))