#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#In this jupyter notebook we will be tasked with taking data in one form and transforming it for easier downstream analysis. 
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
pd.set_option('display.notebook_repr_html',True) 
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None) 
# We will read in the 'class', 'odor', and 'cap-color' columns and we will be adding meaningful names to each column. 
dfFungi = pd.read_csv("data/agaricus-lepiota.data.txt",                       header = None,                       usecols = [0, 3, 5,],                       names = ['poisonous', 'cap-color', 'odor'])
dfFungi.head(5)
# We will be creating a dictionary to hold the values for the replacement of the strings to integers. 
dictNewValues = {
    'e' : 0, \
    'p' : 1
}
dfFungi.replace({'poisonous': dictNewValues}, inplace=True)
dfFungi.head(5)
# We will be using the same dictionary variable number for the cap-color dictionary
dictNewValues = {
    'n' : 0, \
    'b' : 1, \
    'c' : 2, \
    'g' : 3, \
    'r' : 4, \
    'p' : 5, \
    'u' : 6, \
    'e' : 7, \
    'w' : 8, \
    'y' : 9, \
}
dfFungi.replace({'cap-color': dictNewValues}, inplace=True)
dfFungi.head(5)
#We will be using the same dictionary variable numbers for the odor dictionary
dictNewValues = {
    'a' : 0, \
    'l' : 1, \
    'c' : 2, \
    'y' : 3, \
    'f' : 4, \
    'm' : 5, \
    'n' : 6, \
    'p' : 7, \
    's' : 8
}
dfFungi.replace({'odor': dictNewValues}, inplace=True)
dfFungi.head(5)
dfFungi.dtypes

poisonous    int64
cap-color    int64
odor         int64
dtype: object
# We will be creating a scatterplot that shows the relationship between odor and poisonous
#It appears that odor can be an effective indicator as to weather or not a mushroom is edible. 
sns.set(style='whitegrid',font_scale=4)
sns.set_color_codes('pastel')
sns.lmplot('odor', 'poisonous', data=dfFungi, size=30, aspect=1.294, scatter_kws={"s": 1200}).savefig('Output/Poisonous v cap-color.pdf')
# We will be creating a scatterplot that shows the relationship between cap-color and poisonous
# It appears that cap color can be an effective indicator as to weather or not a mushroom is edible. 
sns.lmplot('cap-color', 'poisonous', data=dfFungi, size=30, aspect=1.294, scatter_kws={"s": 1200}).savefig('Output/Poisonous v cap-color.pdf')

