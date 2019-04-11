# -*- coding: utf-8 -*-
"""


Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:

"""

import pandas as pd
import numpy as np
df=pd.read_csv("thanksgiving-2015-poll-data.csv")

df["US Region"].value_counts()
#person who celebrate thanksgiving
requireddataset=df["How much total combined money did all members of your HOUSEHOLD earn last year?"]

requireddataaset=requireddataset.replace("Prefer not to answer",value=np.nan,inplace=True)
a=list(requireddataset.values)
money=[]
for i in a:
    money.append(str(i))
newmoney=[]
import re
for i in money:
    i=i.replace("$", "")
    newmoney.append((i.replace(",","")).split("to"))
moneyinvest=[]   
for i in newmoney:
    if(len(i)==2):
        moneyinvest.append(int((int(i[0])/2+int(i[1])/2)))
    else:
        if(i[0]!=str(np.nan)):
            moneyinvest.append(int(re.search("[0-9]+",i[0]).group()))
        else:
            moneyinvest.append(float(i[0]))
df["income"]=(moneyinvest)
dataset=df[df["Do you celebrate Thanksgiving?"]=='Yes']

li=list(dataset.columns)
'''
import numpy as np
li.pop(np.arange(11,50,1))
'''
knowingnull=list(dataset.isnull().any(axis=0))

for i in range(2,51):
    dataset.iloc[:,i]=dataset.iloc[:,i].fillna("not opted")
    
dataset["Do you typically pray before or after the Thanksgiving meal?"]=dataset["Do you typically pray before or after the Thanksgiving meal?"].fillna("Yes")
dataset.iloc[:,52]=dataset.iloc[:,52].fillna("Thanksgiving is local--it will take place in the town I live in")
most_common_dish=dataset["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
region=dataset["US Region"].value_counts()

final=[]
for i in region.index:
    region2=dataset[["What is typically the main dish at your Thanksgiving dinner?"]][dataset["US Region"]==i]
    final.append(region2) 

South_Atlantic=final[0]["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
Middle_Atlantic=final[1]["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
East_North_Central=final[2]["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
Pacific=final[3]["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
West_South_Central=final[4]["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
West_North_Central=final[5]["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
East_South_Central=final[6]["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
New_England=final[7]["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
Mountain=final[8]["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


import numpy as np
import matplotlib.pyplot as plt


N = 9
Turkey=np.array([181,130,135,107,77,60,50,51,37])
HamPork=np.array([7,2,4,6,2,4,1,0,1])
Tofurkey=np.array([3,5,1,4,2,2,0,1,2])
Chicken=np.array([3,1,0,0,1,1,0,2,1])
Roastbeef=np.array([3,2,0,1,0,0,1,0,0])
Turducken=np.array([0,1,0,2,0,0,0,0,0])
Other=np.array([6,4,5,9,3,3,4,1,0])

fig, ax = plt.subplots()
ind = np.arange(N)    # the x locations for the groups
      # the width of the bars

p1 = ax.bar(ind, Turkey, color='r')
p2 = ax.bar(ind , HamPork, color='y',bottom = Turkey)
p3 = ax.bar(ind  ,Tofurkey,color='b',bottom = HamPork+Turkey)
p4 = ax.bar(ind ,Chicken, color='g',bottom = Tofurkey+HamPork+Turkey)
p5 = ax.bar(ind ,Roastbeef,  color='cyan',bottom = Chicken+Tofurkey+HamPork+Turkey)
p6 = ax.bar(ind ,Turducken, color='black',bottom = Roastbeef+Tofurkey+HamPork+Turkey+Chicken)
p7 = ax.bar(ind ,Other,color='grey',bottom = Turducken+Roastbeef+Tofurkey+HamPork+Turkey+Chicken)
ax.set_title('Scores by group and gender')
ax.set_xticklabels(('South_Atlantic', 'Middle_Atlantic', 'East_North_Central', 'Pacific', 'West_South_Central','West_North_Central', 'East_South_Central', 'New_england','mountain'),rotation=90,)

ax.legend((p1[0], p2[0],p3[0],p4[0],p5[0],p6[0],p7[0]), ('Turkey', 'Hampork','Tofurkey','Chicken','roatbeef','turducken','other'))
ax.autoscale_view()

plt.show()

#income based
#graph income vs food
income_ranges = dataset.iloc[:,-3].unique()[:-1]
x2 = []
for i in income_ranges:
    x2.append([i,dataset.iloc[:,2][dataset.iloc[:,-3]==i].value_counts()[:2]])
    
plt.bar(income_ranges,height=[x2[i][1][0] for i in range(0,10)],color='blue',edgecolor='black',label='Turkey')
plt.bar(income_ranges,height=[i[1][1] for i in x2],color='red',edgecolor='black',bottom=[i[1][0] for i in x2])
plt.title('Income vs Top 2 Food Items')
plt.xticks(rotation=60)
plt.xlabel('Income')
plt.show()


'''
compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    

'''
dataset["income"]=dataset["income"].fillna(dataset["income"].mean())       
cann=dataset[["What type of cranberry saucedo you typically have?","income","What type of cranberry saucedo you typically have? - Other (please specify)"]]
homemade=list(cann["income"][cann["What type of cranberry saucedo you typically have?"]=='Homemade'])
print("avg_homemade_cannberry", sum(homemade)/301)
canned=list(cann["income"][cann["What type of cranberry saucedo you typically have?"]=='Canned'])
print("avg_canned_cannberry", sum(canned)/502)
#faltu ki mehnat purani galti sudharne ki liye
home_canned=pd.DataFrame(homemade+canned)
home_canned["home/canned"]="homemade"
for i in range(len(home_canned["home/canned"])):
    if(i>301):
        home_canned["home/canned"][i]="canned"
    

n_bins = 5

# Generate a normal distribution, center at x=0 and y=5
x = homemade
y = canned

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg
plt.hist(x, bins=n_bins)
plt.hist(y, bins=n_bins)
plt.show()






