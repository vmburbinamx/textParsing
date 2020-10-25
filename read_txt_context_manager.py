import os

#Set path to 'data' folder'
path_to_data_in_current_directory = os.getcwd() + '\\data\\'

# Read & print the first 3 lines
with open(path_to_data_in_current_directory + 'tweets3.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())