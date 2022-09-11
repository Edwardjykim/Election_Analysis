temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

# Import the datetime class from the datetime module.
import datetime
from inspect import formatannotationrelativeto

# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()

# Print the present time.
print("The time right now is", now) 

import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we wil write data to the file.
#open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:


    # write some data to the file.
    #txt_file.write("Hello World")

# Write three counties to the file.
#or txt_file.write("Arapahoe, ")
#   txt_file.write("Denver, ")
#   txt_file.write("Jefferson, ")
    txt_file.write("Counties in the Election\n-------------------------------\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()

# Close the file.
election_data.close()