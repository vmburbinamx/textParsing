import os

#Set path to 'data' folder'
path_to_data_in_current_directory = os.getcwd() + '\\data\\'

# Open a file
file = open(path_to_data_in_current_directory+'tweets3.txt', 'r')
# Print it
print("File is closed? ", file.read())
# Check whether file is closed
print(file.closed)
# Close file
file.close()
# Check whether file is closed
print("File is closed? ", file.closed)