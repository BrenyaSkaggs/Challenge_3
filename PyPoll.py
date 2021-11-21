#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote. 

#Add our dependencies.
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv") 

#Assign a variable to save the file to a path.
file_to_save= os.path.join("Analysis","election_analysis.txt") 

#Open the election results and read the file.
with open(file_to_load) as election_data:
    File_reader=csv.reader(election_data)

    #Read the header row.
    header=next(File_reader)
    print(header)

    #Print each row in the CSV file.
    for row in File_reader:
        print(row)

     
#Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

#Creat a filename variable to a direct or Indirect path 
file_to_save= os.path.join("analysis","election_analysis.txt")

#Using the with statement open statement to file as text file.
with open(file_to_save, "w") as txt_file:
    #write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")

    
  


































