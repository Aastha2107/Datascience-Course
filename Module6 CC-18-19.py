# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:20:52 2018

@author: aastha
"""
'''
Write a Python function to check whether a string is PANGRAM or not.  Take input from User and give the output as PANGRAM or NOT PANGRAM. 
Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.

Input

The five boxing wizards jumps.

Output

Below is the output of execution of this program.

NOT PANGRAM

'''
string="The quick brown fox jumps over the lazy dog".lower()
count=0
for i in set(string):
   if (i.isalpha()):
        count+=1
print(count)
if(count==26):
    print("PANGRAM")
else:
    print("NOT PANGRAM")
        
import string
low_abcd = string.ascii_lowercase
    
'''
Program Specification

Define a function reverse() that computes the reversal of a string.
(Without using Python's inbuilt function, Take input from User)

Input

I am testing

Output

Below is the output of execution of this program.

gnitset ma I

'''
def reverse(t):
      print(sen[::-1])
      
sen="i am testing"      
reverse(sen)