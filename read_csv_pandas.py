import pandas as pd
import os

#Set path to 'data' folder'
path_to_data_in_current_directory = os.getcwd() + '\\data\\'

#Set full path name
fullFileName = path_to_data_in_current_directory+'titanic_sub_just_numbers.csv'

#read file
data = pd.read_csv(fullFileName)