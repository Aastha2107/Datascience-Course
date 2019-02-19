# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:25:00 2018

@author: aastha
"""

#db_university
from pymongo import MongoClient
from datetime import datetime
#import json
#in this database are getting access again and again so we will use insert many fucntion
client = MongoClient('localhost', 27017)
mydb = client.db_University

def add_Students(student_name, student_age,i, Student_branch):
    mydb.Students.insert(
                {
                "Student Name" : student_name,
                "Student Age" : student_age,
                "Student roll no":i+1,
                "Student branch" :Student_branch,
                "Date-Time" : datetime.now()
                })
    return "Client added successfully"
n=int(input("enter the number of students"))
for i in range(0,n):
    name = input("Enter Student Name: ")
    age = int(input("Enter age: "))
    #roll = int(input("Enter roll number: "))
    branch =input("Enter branch: ")
    print(add_Students(name,age,i,branch))


    
#insert many 
#database will be accessed only once
client = MongoClient('localhost', 27017)
myentry = client.db_Student
l=[]
def add_Stu(student_name, student_age,i, Student_branch):
    #global l
    
    k= {
        "Student Name" : student_name,
        "Student Age" : student_age,
        "Student roll no":i+1,
        "Student branch" :Student_branch,
        "Date-Time" : datetime.now()
        }
    l.append(k)
    return "Client added successfully"

n=int(input("enter the number of students"))
for i in range(0,n):
    name = input("Enter Student Name: ")
    age = int(input("Enter age: "))
    #roll = int(input("Enter roll number: "))
    branch =input("Enter branch: ")
    print(add_Stu(name,age,i,branch))
myentry.university.insert_many(l)