# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:22:45 2018

@author: aastha

"""

#function definition
def addition(**kwargs):
    print (type(kwargs))
    print (kwargs)
    
    for i in kwargs.values():
        print (i)
    
    return "End"
    
print (addition(a=2, b=3, c=4))

    
'''
Program Specification

Write following functions for list operations.
 Take list as input from the User

Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()

Only call Print() function to display the results in the below displayed 
format (i.e all the functions must be called inside the print() function 
and only the Print() is to be called in the main script).

Input

5,2,6,2,3



'''
a=[5,2,6,2,3]


def add():
    return sum(a)
def mult():
    m=1
    for i in a:
        m=m*i
    return m
def largest():
    return max(a)
def larg():
    m=0
    for i in a:
        if(i>m):
            m=i
    return m
def smallest():
    return min(a)
def sorted():
    a.sort()
    return a
def duplicate():
    return set(a)

print("sum=",add(),"multiply=" ,mult(),"maximum=",largest())
print("minimun=",smallest(),"sorted list=",sorted(),"duplicatelist=",duplicate())


'''
We want to make a row of bricks that is target inches long.
 We have a number of small bricks (1 inch each) and big bricks (5 inches each).
 Make a function that prints True if it is possible to make the exact target by 
 choosing from the given bricks or False otherwise. Take list as input from user 
 where its 1st element represents number of small bricks, middle element represents
 number of big bricks and 3rd element represents the target.

Input

2, 2, 11
'''
#birckproblem
#x+5y=target
def brick(x,y,target):
    for i in range(x+1):
        for j in range(y+1):
            if(i+5*j==target):
                return True
    return False
                

a,e,c = input("enter:").split(",")
answer = brick(int(a),int(b),int(c))
print(answer)


def brick(s,b,t):
    if t%5 > s:
        return False
    num = b*5+s
    if num >= t:
        return True
    else:
        return False
a,e,c = input("enter:").split(",")
print (brick(int(a),int(e),int(c)))


'''
Program Specification

Write a Python program to construct the following pattern. Take input from User.

Input

 5

Output

Below is the output of execution of this program.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*



'''

a=int(input("enter:>"))
def pattern(a):
    for i in range(a+1):
        for j in range(i):
            print("*",end=" ")
        print("\n")
    for i in range(a-1,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print("\n")
pattern(a)



a=int(input("enter:>"))
for i in range(a):
    print("*"*i)
for i in range(a,0,-1):
    print("*"*i)
    
    
    
'''
Take dictionary as input from user with keys, a b c,
 with some integer values and print their sum.
 However, if any of the values is a teen -- in the range 13 to 19 inclusive -- then
 that value counts as 0, except 15 and 16 do not count as a teens.
 Write a separate helper "def fix_teen(n):"that takes in an int value
 and returns that value fixed for the teen rule. In this way, you avoid
 repeating the teen code 3 times (i.e. "decomposition"). 

Input

 {"a" : 2, "b" : 15, "c" : 13}

Output

Below is the output of execution of this program.

Sum = 17


'''

keys=input("enter: ").split(",")
val=input("Enter numbers: ").split(",")
dic={}
for i in range(len(keys)):
    dic[keys[i]]=int(val[i])
print(dic)
teen()
def teen():
    p=0
    for i in val:
        if(int(i)>=13 and int(i)<=19):
            if(int(i)==15 or int(i)==16):
                p=p+int(i)
                print(int(i))
            else:
                i=0
        else:
            p=p+int(i)
    print(p)