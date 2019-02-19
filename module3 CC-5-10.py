# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:07:11 2018

@author: aastha
"""
'''
This program accepts a sequence of comma separated 
numbers from user and generates a list and tuple with those numbers.
'''
a=input("enter the number: ")

li=a.split(",")
print(li)
tup=tuple(li)
print(tup)

'''
This program prints even numbers from a given numbers list in the same order and stops the
 printing if any numbers that comes after 237 in the sequence.(No user input required)
'''

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for i in numbers:   
    if i==237:
        break;
    else:
        if(i%2==0):
            print(i)
            
            
'''
This program accepts a string from User and counts the number
 of characters (character frequency) in the input string.'''
 


string="aasthajain0721"
letter=0
num=0
for i in string:
    if(i.isalpha()):
        letter=letter+1
    else:
        num=num+1
 '''
 Program Specification

This program accepts a string from User and counts the
 number of characters (character frequency) in the input string.

Input

www.google.com
 
 
 '''

a="www.google.com"
for i in set(a):
    dict((i,a.count(i)))
    

dict((letter,a.count(letter)) for letter in set(a))


'''
Return the "centered" average of an array of integers,
 which we'll say is the mean average of the values, except
 ignoring the largest and smallest values in the array.
 If there are multiple copies of the smallest value, ignore just one copy,
 and likewise for the largest value. Use int division to produce the final average.
 You may assume that the array is length 3 or more.(Take input from user)

Input

1, 2, 3, 4, 100

Output

3

'''
#long method
a=[1, 2, 3, 4, 100,6,4,7,4,54,6,4,6,7,3,1234,534,5]
min=a[0]
max=a[0]
for i in a:
    if(min>i):
        min=i
    if(max<i):
        max=i
print(min) 
print(max)
a.remove(max)
a.remove(min)
sum=0
for i in a:
    sum=sum+i
avg=sum/len(a)
print(avg)
    
#sort method
a.sort()
print (sum(a[1:-1])/len(a[1:-1]))




'''Program Specification

Return the sum of the numbers in the array, 
returning 0 for an empty array. Except the number 13 is very unlucky, 
so it does not count and numbers that come immediately after a 13 also do not count.(Take input from user)

Input

13, 1, 2, 13, 2, 1, 13

Output

3




'''










a=[13,1,2,13,2,1,13,13,3,5]
sum=0
i=0
while i<len(a):
    if( i==(len(a)-1) or i==(len(a)-2)):
        if(a[i]==13):
            break
        else:
            sum=sum+a[i]
       # print("end")
        #print(sum)
    elif(a[i]==13):
        i=i+2
        sum=sum+a[i]
        #print("second" )
        #print(sum)
        i=i+1
    else:
        sum=sum+a[i]
        #print("third")
        #print(sum)
        i=i+1
        
print(sum)        


flag, total = 0,0

for i in a:
    if i == 13:  # Itself 13
        flag = 1
    elif i != 13 and flag == 1:  # Previous number is 13
        flag = 0
    else:
        total += i

print (total)  


new_total = 0
for i in range(len(a)):
    if a[i] == 13 or a[i-1]==13:
        continue
    new_total += a[i]
print (new_total)