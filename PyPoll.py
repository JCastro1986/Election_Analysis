#The data we need to retrive.
#1. The total number of votes cast
#2. A complete list of candidates who recieve votes
#3. The percentage of votes each candidate won
#4. The total of votes each candidate won
#5. The winner of the elction based on polpular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
        








###Practice Code

    #etrieve the first item from each row
    #print(row[0])

    # # Print each row in the CSV file.
    # for row in file_reader:
    #    print(row)

####
# import csv
# import os

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write three counties to the file.
#      txt_file.write("Counties in the Election\n------------------\nArapahoen\nDenvern\nJefferson")

    # # Write three counties to the file.
    #  txt_file.write("Arapahoe ,")
    #  txt_file.write("Denver ,")
    #  txt_file.write("Jefferson ,")

    # Write some data to the file.
    #txt_file.write("Hello World")

# # Assign a variable for the file to load and the path.
# ##Direct PAth Variable
# #file_to_load = 'Resources/election_results.csv'
# ##Indirect PAth Variable
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Open the election results and read the file.
# #election_data = open(file_to_load, 'r')
# with open(file_to_load) as election_data:
#     # To do: perform analysis.
#     print(election_data)

# # Close the file.
# election_data.close()

###
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")
# # Close the file
# outfile.close()
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")