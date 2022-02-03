#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import datetime


# In[3]:


#set to see more columns
pd.set_option('display.max_colwidth', 10)


# In[4]:


#read csv file
jeopardy = pd.read_csv('jeopardy.csv')


# In[5]:


#jeopardy DataFrame before pandas manipulating
print(jeopardy.head())


# In[6]:


#rename columns
jeopardy.rename(columns={
  ' Air Date': 'Air Date',
  ' Round': 'Round',
  ' Category': 'Category',
  ' Value': 'Value',
  ' Question': 'Question',
  ' Answer': 'Answer'
},inplace=True)


# In[7]:


#function that filters the dataset for questions that contains all of the words in a list of words
def data_filter(data, words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data['Question'].apply(filter)]


# In[8]:


#adding new column with a float value
jeopardy['Float Value'] = jeopardy['Value'].apply(lambda x: float(x.strip('$').replace(',','')) if x!= "None" else 0)


# In[9]:


#filtering for words: "King" and "England"
filtered = data_filter(jeopardy, ["King", "England"])
print(filtered)


# In[10]:


#filtering for an average difficulty
print(filtered.groupby('Question')['Float Value'].mean())


# In[11]:


#function that returns the count of the unique answers to all of the questions in a dataset
def unique_answers(data):
  return data.groupby('Answer').nunique()


# In[12]:


print(unique_answers(jeopardy))


# In[13]:


#adding new column year and decades
jeopardy['Year'] = pd.DatetimeIndex(jeopardy['Air Date']).year
jeopardy['Decades'] = jeopardy['Year'].apply(lambda x: '2000s' if x>=2000 else '90s')


# In[14]:


#filtering for a word in question by decades
by_decades_filtered = data_filter(jeopardy,['Computer'])


# In[15]:


#investinge how many questions from the 90s use the word "Computer" compared to questions from the 2000s
print(by_decades_filtered.groupby('Decades').Category.count())


# In[ ]:




