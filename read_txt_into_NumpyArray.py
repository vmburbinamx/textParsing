# Import package
import numpy as np
import os

#Set path to 'data' folder'
path_to_data_in_current_directory = os.getcwd() + '\\data\\'

# Assign filename to variable: fullFileName
fullFileName = path_to_data_in_current_directory+'titanic_sub_just_numbers.csv'

# Load file as array: titanic
titanic = np.loadtxt(fullFileName, delimiter=",", dtype=str)

# Print datatype of titanic
print(type(titanic))
print(titanic)