#!/usr/bin/env python
# coding: utf-8

# # Exercise 1, sprint 2

# In[42]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#survey = pd.read_csv("survey.csv")


# In[43]:


#survey.head()


# In[44]:


#steps = pd.read_csv("steps.csv", sep =";")

#steps.head()


# In[45]:


survey = pd.read_csv("survey.csv")
steps = pd.read_csv("steps.csv", sep =";")

new = pd.merge(steps, survey, on = 'id')

new.head()


# In[59]:


def above_150(x):
    if(x > 150.0): 
        return float('NaN')
    else: 
        return x
    
def under_40(x):
    if(x < 40.0): 
        return float('NaN')
    else: 
        return x
    
def under_420(x):
    if x > 150.0 or x < 40.0: 
        return float('NaN')
    else: 
        return x 
    
new['weight'] = new['weight'].apply(under_420)

sns.histplot(new['weight'].dropna(), kde=True) #Selecting the rating column. I need to drop the NA's for the plot
plt.title('Weight of the data')
plt.xlabel('Weight (kilograms)')
plt.show()


# In[51]:


new['weight'].value_counts()

new['height'].value_counts()

