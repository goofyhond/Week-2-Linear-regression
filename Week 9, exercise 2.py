#!/usr/bin/env python
# coding: utf-8

# # Exercise 2

# In[30]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[31]:


survey = pd.read_csv("salary.csv")
#steps = pd.read_csv("steps.csv", sep =";")

#new = pd.merge(steps, survey, on = 'id')

survey.head()


# In[32]:


survey['age'].name = 'Age (years)' #Labeling the variable for plotting
file_size = survey['age'].dropna() #Selecting the size column. I need to drop the NA's, otherwise Seaborn won't plot
sns.histplot(file_size, kde=True) 
plt.title('Age + distribution')
plt.xlabel('Age (in years)')
plt.ylabel('Number of people')

plt.show()

mean_size = survey['age'].mean()
median_size = survey['age'].median()

print(f'The median filesize is: {median_size} year')
print(f'The mean filesize is: {mean_size} year')

sns.histplot(file_size, kde=True)
plt.title('Age + distribution')
plt.axvline(median_size, 0, 100, color='pink', label='median') #This adds a vertical line at x-position median_size, from y = 0 to y = 100 
plt.axvline(mean_size, 0, 100, color='yellow', label='mean') 
plt.legend() #This adds a legend. It works automatically because I've set the labels in the previous lines
plt.show()


# In[33]:


sns.boxplot(survey['capital-gain'])
plt.title('title')
plt.xlabel('x')
plt.ylabel('y')


plt.show()


# In[34]:


survey['capital-gain'].name = 'title' #Labeling the variable for plotting
file_size = survey['capital-gain'].dropna() #Selecting the size column. I need to drop the NA's, otherwise Seaborn won't plot
sns.histplot(file_size, kde=True) 
plt.title('title')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

mean_size = survey['capital-gain'].mean()
median_size = survey['capital-gain'].median()

print(f'The median filesize is: {median_size} amount')
print(f'The mean filesize is: {mean_size} amount')

sns.histplot(file_size, kde=True)
plt.title('title')
plt.axvline(median_size, -10000, 4000, color='orange', label='median') #This adds a vertical line at x-position median_size, from y = 0 to y = 100 
plt.axvline(mean_size, -10000, 4000, color='black', label='mean') 
plt.legend() #This adds a legend. It works automatically because I've set the labels in the previous lines
plt.show()


# In[35]:


age = survey[survey['age'] > 0] #Subsetting the dataframe to include only paid apps
sns.violinplot(age['age'])
sns.swarmplot(age['age'], color='orange') #default color doesn't stand out
plt.title('title')
plt.ylabel('y')
plt.xlabel('x')
plt.show()

