#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 09:11:06 2023

@author: arundhatipathrikar12
"""

import pandas as pd

# file_name= pd.read_csv('file.csv')<--- format od read_csv
data= pd.read_csv('transaction.csv')

data= pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()

#defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

ProfitPerItem = SellingPricePerItem-CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased* ProfitPerItem

CostPerTransaction = NumberOfItemsPurchased* CostPerItem

SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#CostPerTransaction column calculations
#CostPerTransaction CostPerItem * NumberOfItemPerchased 
#variable = dataframe[column_name]
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased= data['NumberOfItemsPurchased']
CostPerTransaction=CostPerItem * NumberOfItemsPurchased
 
#adding a new column to dataframe
# one way -> data['CostPerTransaction']= CostPerTransaction
data['CostPerTransaction']= data['CostPerItem'] * data['NumberOfItemsPurchased']
data['SalesPerTransaction']= data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
#Profit =Sales - Cost
data['ProfitPerTransaction']= data['SalesPerTransaction']- data ['CostPerTransaction']
#Markup =(Sales-Cost)/Cost
data ['Markup']= data['ProfitPerTransaction']/data['CostPerTransaction']

#Rounding Markup
roundmarkup= round(data['Markup'], 2)
data['Markup']= roundmarkup

#combining data fields
my_name = 'Aru'+'Path'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

#checking columns datatype
print(data['Day'].dtype)

#change column types
day = data['Day'].astype(str)
year=  data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day + '-'+ data['Month']+'-'+ year
data['date']=my_date

# using iloc to view specific information of rows/Columns
data.iloc[0] #views the row with index = 0
data.iloc[0:3] #views the row with index = 0,1,2---- first three rows
data.iloc[-5:] #last five rows

data.head(5) #brings first five rows

data.iloc[:,2] # brings all rows in the second column
data.iloc[4,2] # brings in 4th row and 2nd column

#using split to split client_keywords column
#new_var = column.str.split('sep', expand = True)
split_col= data['ClientKeywords'].str.split(',' , expand =True)

#creating new columns for the split n client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function(need to get rid of )
data['ClientAge']= data['ClientAge'].str.replace('[','')
data['LengthOfContract']= data['LengthOfContract'].str.replace(']','')

#how to merge files
#bringing in new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')

#merging files: merge_df=pd.merge(df_old, df_new, on='key')
data = pd.merge(data, seasons, on='Month') 

#dropping columns
#df = df.drop('Columnname', axis = 1)
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)



#Export into csv
data.to_csv('ValueInc_Cleaned.csv', index = False)
























