# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:40:25 2018

@author: aastha
"""


'''
Objective:-Learn to use a RESTful API.

Task:-

Create a client REST API that sends and receives some information from the Server by calling server's REST API.
You are expected to create two functions each for Sending and Receiving data.


You need to make two api calls, one with POST method for sending data and the other with GET method to receive data
All the communication i.e. sending and receiving of data with the server has to be in JSON format
First send the data to cloud using the "http://13.127.155.43/api_v0.1/sending" api with the following fields (Field names should be same as shown ):
Phone_Number (pass phone number as string and not as integer)
Name
College_Name
Branch
Now receive the data from cloud using the "http://13.127.155.43/api_v0.1/receiving" api with     “Phone_Number” along with the number you are looking for as query parameter
Print the server responses from both the cases. The first one will give response-code : 200 and response-message : "Data added Successfully", if all goes well. The second one will give all the details stored with the phone number you provided as query parameter. Both the responses will be in JSON format.
Output

response-code : 200 
response-message : Data added Successfully 


Submitted_at : Mon, 11 Sep 2017 13:32:30 GMT
Phone Number : 7877757144
Name : Kunal Vaid
Branch : B.Tech CSE
College_Name : Amity University


'''

import requests
URL="http://13.127.155.43/api_v0.1/sending"
data={
	"Phone_Number": "999888777",
	"Name": " Aastha jain",
	"Branch": "B.Tech CSE",
	"College_Name": "JECRC University"
}
url3="http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"
r=requests.get(url3)
print(r.json)
#first need to import json and then we can data and header is neeeded  in  this
#dumps fuction used to convert dic into json
#loads funtion used to convert json into dic
import json
new_data = json.dumps(data)

r = requests.post(url = URL , data = new_data, headers={"Content-Type":"application/json"}) 
print (r.text )


#easy way to add the data
r = requests.post(url=URL,json=data) 
print (r.text )


URL2="http://13.127.155.43/api_v0.1/receiving"
PARAMS={"Phone_Number": "999888777"}
r = requests.get(url = URL2 , params=PARAMS) 
data = r.json() 
print(data)


#without using params  
URL2="http://13.127.155.43/api_v0.1/receiving?Phone_Number=999888777"
r = requests.get(url = URL2) 
data = r.json() 
print(data)

for k,v in data.items():
    print (k+" : "+v)

