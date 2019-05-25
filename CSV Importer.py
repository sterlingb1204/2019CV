#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jul 11 20:48:45 2018

@author: sterling

Remember to Trim Before Uploading!
"""
import pandas as pd
import time
#import numpy as np

df = pd.read_excel('mosaic.xls') # Reads the Excel File and creates a dataframe 
# Column Headers
df = df[['street', 'city', 'state', 'zip','hoa','mStreet','mCity','mState','mZip','account','first','last','home','work','cell','email']]
#This uses the Strip method to clean up the data
df = df.apply(lambda x: x.str.strip().str.lower() if x.dtype == "object" else x)


df['difStreet'] = df['street'] != df['mStreet']
df['duplicates'] = df.duplicated(subset = 'last', keep = False)

df['RedFlag'] = df['difStreet'] == True or df['duplicates'] == False 


#Fixes all capitalization for viewing purposes on the excel export
df = df.apply(lambda x: x.str.title() if x.dtype == "object" else x)
df['email'] = df['email'].str.lower()
df['state'] = df['state'].str.upper()
df['mState'] = df['mState'].str.upper()




#Exports to Excel
df.to_excel('MosaicOutNew1.xls')
print('operation complete in:', time.process_time(), 'ms')
