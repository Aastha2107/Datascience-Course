
#just basic


hello = 'hello'    # String literals can use single quotes
world = "world"    # or double quotes; it does not matter.
print(hello)       # Prints "hello"
print(len(hello))  # String length; prints "5"
hw = hello + ' ' + world  # String concatenation
print(hw)  # prints "hello world"
hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formatting
print(hw12)  # prints "hello world 12"# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 10:23:39 2018

@author: aastha
"""
'''
To create an array of random e-commerce data of total amount spent per transaction. Execute the code snippet below.

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
Print incomes
Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
Find the mean and median of this data using NumPy package.
Add outliers (outlier is an observation that lies an abnormal distance from other 
values in a random sample from a population) to it to see their effect.


'''
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes)

plt.hist(incomes, 50)
plt.show()
print("mean of the incomes", np.mean(incomes))

print("median of the incomes",np.median(incomes))

incomes = np.append(incomes,[10000000000])


'''
Create a normally distributed random data with parameters:

1.     Centered around 150.

2.     Standard Deviation of 20.

3.     Total 1000 data points.

Plot the histogram using matplotlib (bucket size =100) and observe the shape.
Calculate Standard Deviation and Variance.



'''
graph=np.random.normal(150.0,20.0,1000)
print(graph)
plt.hist(graph,100)
plt.show()
print(graph.var())
print(graph.std())

'''
Create a random array of 40 integers from 5 - 15 using NumPy. 
Find the most frequent value with and without Numpy.

'''

arr=np.random.randint(5,15,40)
print(arr)
from collections import Counter
print(Counter(arr).most_common(1))


#another method 
import numpy as np
a = np.random.randint(5,15,40)
d={}
fin=[]
for i in a:
    d[i] = d.get(i,0)+1
    print(d)
for i in d.items():
    j,k = i
    i = k,j
    fin.append(i)

fin.sort()
freq,num = fin[-1]
print("ferqueny",freq,"num",num)


'''
You are given a 9 space separated numbers. Write a python code to convert it into a 3x3 NumPy array of integers.

Input

6 9 2 3 5 8 1 5 4

Output

[[6 9 2]
[3 5 8]
[1 5 4]]


'''
inp=input("enter the number:").split(" ")
x = np.array(inp )
x = x.reshape(3,3)
print (x)
