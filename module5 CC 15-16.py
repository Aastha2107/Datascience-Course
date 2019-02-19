# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:46:23 2018

@author: aastha
"""

'''
Program Specification

Write a Python program which iterates the integers from 1 to 50(included).
 For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
 For numbers which are multiples of both three and five print "FizzBuzz". (User Input not required).

Output

1
2
Fizz
4 
Buzz


'''
fb=open("number.txt",'w')
print (fb)
a=fb.readlines()


#with open("number.txt") as f:
    for line in range(1,51):
        if(int(line)%3==0 and int(line)%5==0):
            print("buzzfizz")
        elif(int(line)%3==0):
            print("fizz")
        elif(int(line)%5==0):
            print("buzz")
        else:
            print(line)

'''
Write a function translate() that will translate a text into "rövarspråket" 
(Swedish for "robber's language"). That is, double every consonant and place an occurrence
 of "o" in between. (Take Input from User)

Input

This is fun

Output

Below is the output of execution of this program.

ToThohisos isos fofunon



'''

def translate(string):
    b=[]
    for i in string:
        if i not in ["a","e","i","o","u"," "]:
            i=i+"o"+i
            b.append(i)
        else:
           b.append(i)
    return("".join(b))    
a="this is fun"
translate(a) 