import pandas as pd
import os
import xlwings as xw
#https://docs.xlwings.org/en/stable/

#Set path to 'data' folder'
path_to_data_in_current_directory = os.getcwd() + '\\data\\'

# Assign filename to variable: fullFileName
fullFileName = path_to_data_in_current_directory+'titanic_sub.csv'

#read file
df = pd.read_csv(fullFileName)

df.info()

#group data
groupedData = df.groupby(['Sex']).sum().reset_index()



def main():
    xw.sheets('data').activate()
    xw.Range('A1', index=False).value = df
    xw.sheets('grouped_data').activate()
    xw.Range('A1', index=False).value = groupedData