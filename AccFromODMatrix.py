# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:05:22 2019

@author: dvale
"""

# Libraries used
import pandas as pd
import numpy
import os

# Option to make sure that we don't get an alert
# that we are trying to create a number out of a string
pd.options.mode.chained_assignment = None

print ('Working directory is: ' + os.getcwd()) # get directory
print ('')


##### 1) Read OD Matrix ###################################
print ('Reading OD matrix...')

# OD Matrix (with 3 columns: Origin, Destination, Travel)
OD_Matrix = 'OD_Matrix.csv'

# Read OD matrix 
df = pd.read_csv(OD_Matrix , index_col=False)

# If Matrix has more than 3 columns, only the first 3 will be used
df = df.iloc[:,0:3]

# We assume that the OD matrix is in fomat Origin, Destination, ODCost (time, money, CO2, etc)
df.columns = ['Origin', 'Destination', 'ODCost']

# Force string on destination field
df['Destination']=df['Destination'].astype(str)

# Force float on ODCost
df['ODCost']=df['ODCost'].astype(float)

print ('OD matrix read!')
print ('It has ' + str(len(df.index)) + ' rows' )
print ('')



##### 2) Calculate impedance function #####################
print ('Calculating impedance function...')

###### 2a) Exponential 
# Formula used: e ^ (beta * Cij)

# define beta
beta = -0.0384

# calculate exponential function
df['fCij_exp'] = numpy.exp(beta * df['ODCost']).astype(float)

###### 2b) Cumulative opportunities 
# 1 if Cij < MaxValue ; 0 if Cij >= MaxValue

# define threshold
MaxCost = 30

# calculate rectangular function
df['fCij_cum'] = 0
df['fCij_cum'].loc[df['ODCost'] < MaxCost] = 1

print ('Impedance functions calculated!')



##### 3) Read Destination Data ############################
print ('')
print ('Reading destination data...')

# Table with data for opportunities (jobs, hospitals, retail, population, etc)
OppData = 'DestinationData.csv'

#### Read table with data for destinations (opportunities)
df_opportunities = pd.read_csv(OppData, index_col=False)

# Identify Name of column with ID for each destination
DestinationIDColumn = 'Destination_Code'

# Rename column and force string
df_opportunities['Destination'] = df_opportunities[DestinationIDColumn].astype(str)

# Identify Name of column with relevant destination data (eg jobs, hospitals, retail, population)
DataColumn = 'Residents'

# force float on data column
df_opportunities['OppData'] = df_opportunities[DataColumn].astype(float)

print ('Destination data read!')
print ('It has ' + str(len(df_opportunities.index)) + ' rows' )



##### 4) Join dataframes and calculate accessibility ######
print ('')
print ('Merging tables and calculating accessibility (this might take some time)...')

# merge tables (Join based on destination field)
df = df.merge(df_opportunities, on='Destination')

## Calculate Ojf(Cij)
# exponential 
df['Opp_exp'] = df['fCij_exp'] * df[DataColumn]

# cumulative 
df['Opp_cum'] = df['fCij_cum'] * df[DataColumn]

# Sum jobs by origin
# sum (Ojf(Cij))
df_Results = df.groupby('Origin')[['Opp_exp', 'Opp_cum']].sum()

# Rename accessibility fields
df_Results = df_Results.rename(columns={'Opp_exp': 'Acc_exponential', 'Opp_cum': 'Acc_cumulative'})

print ('Accessibility values calculated!')
print ('Final table has ' + str(len(df_Results.index)) + ' rows' )



##### 5) Save results to csv file #########################
print ('')
print ('Saving output to csv')

# Define Output file name
OutputFile = 'AccResults.csv'

# Write csv file
df_Results.to_csv(OutputFile)

print ('')
print('Results saved at ' + os.getcwd())
print('Filename: ' + OutputFile)

##################################################
