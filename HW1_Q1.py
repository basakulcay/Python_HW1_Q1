#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:40:24 2020

@author: basakulcay
"""
#Q1: Write a program that reads a five-digit integer number, determines and prints how many
#digits in the number are 7s.

num=int(input('Enter 5 digit integer number: '))
counter=0
count=0

for i in str(num):
    counter+=1
if(counter==5):
    for n in str(num):
        if n=='7':
            count+=1
    print("There are",count,"7(s) in the number you typed")
else:
    print("You haven't typed a 5-digit number, run the program again")
        
    