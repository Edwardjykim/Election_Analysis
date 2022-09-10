#The data we need to retrieve.
# 1.  The total number of votes cast
# 2.  A complete list of cadidates who received votes
# 3.  The percentage of votes each candidate won
# 4.  The total number of votes each candidate won
# 5.  The winner of the election based on popular vote.

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



# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file.
   # for row in file_reader:
    #    print(row)

# Close the file
txt_file.close()

# Close the file.
election_data.close()


