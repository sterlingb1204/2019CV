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

df = pd.read_excel('BRH.xls') # Reads the Excel File and creates a dataframe 
# Column Headers
df = df[['street#', 'street', 'city', 'state', 'zip','hoa','mStreet#','mStreet','mCity','mState','mZip','account','first','last','home','work','cell','email', 'Address Type']]

#This uses the Strip method to clean up the data
df = df.apply(lambda x: x.str.strip().str.lower() if x.dtype == "object" else x)

df['street1'] = df['street#'] + " " + df['street']




df['mStreet'] = df['street']
df['mState'] = df['state']
df['mZip'] = df['zip']
df['mCity'] = df['city']

next_address_attributes = df[['Address Type', 'street', 'city', 'state', 'zip']].shift(-1)

# Create a series to indicate whether information should be drawn from next row
# All the decision-making is right here
get_attributes_from_next_address = ((df['Address Type'] == 'Property Address')
    & (next_address_attributes['Address Type'] != 'Property Address'))

df.loc[get_attributes_from_next_address, 'mStreet'] = next_address_attributes.loc[get_attributes_from_next_address, 'street']
df.loc[get_attributes_from_next_address, 'mCity'] = next_address_attributes.loc[get_attributes_from_next_address, 'city']
df.loc[get_attributes_from_next_address, 'mState'] = next_address_attributes.loc[get_attributes_from_next_address, 'state']
df.loc[get_attributes_from_next_address, 'mZip'] = next_address_attributes.loc[get_attributes_from_next_address, 'zip']
#Fixes all capitalization for viewing purposes on the excel export

df = df.apply(lambda x: x.str.title() if x.dtype == "object" else x)
df['email'] = df['email'].str.lower()
df['state'] = df['state'].str.upper()
df['mState'] = df['mState'].str.upper()

df['difStreet'] = df['street'] != df['mStreet']
df['duplicates'] = df.duplicated(subset = 'last', keep = False)

df['RedFlag'] = df['duplicates'].equals(df['difStreet'])


#Exports to Excel
df.to_excel('BRHOut.xls')
print('operation complete in:', time.process_time(), 'ms')
